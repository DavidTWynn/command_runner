import getpass
import netmiko

import sys


def main():
    """Runs script to send commands to multiple devices."""
    # Get list of devices to run against
    devices = import_devices("src/input/devices.txt")
    # Ask user for login info
    username, password = get_login_info()
    # Setup device inventory dicts for netmiko
    device_inventory = create_device_inventory(username, password, devices)
    # Commands to run against all devices
    commands = ["show ip int b | e una", "show ip ro"]
    # Execute commands
    command_outputs = send_commands(device_inventory, commands)

    # Handle formatting
    output = format_command_output(command_outputs)

    # Save output to file and print
    with open("output.txt", "w") as f:
        f.write(output)
    print(output)


def get_login_info() -> tuple[str, str]:
    """Requests login information from user to be used for all devices."""
    username = input("Username: ")
    password = getpass.getpass()
    return username, password


def import_devices(filename: str) -> list[str]:
    """Imports list of device hostnames or IP addresses from a file."""
    try:
        with open(filename, "r") as f:
            # splitlines instead of readlines to not include \n
            return f.read().splitlines()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        sys.exit()


def create_device_inventory(
    username: str, password: str, devices: list[str]
) -> dict[dict]:
    """Creates dictionary of device dictionaries for netmiko."""
    inventory = {}
    for device in devices:
        current_device = {
            "username": username,
            "password": password,
            "host": device,
            "device_type": "cisco_ios",
        }
        inventory[device] = current_device

    return inventory


def _send_command(device_details: dict, command: str) -> str:
    """Takes netmiko inventory dict and sends command to each device."""
    with netmiko.ConnectHandler(**device_details) as net_connect:
        output = net_connect.send_command(command)
        return output


def send_commands(
    multi_device_details: dict[dict], commands: list[str]
) -> dict[dict]:
    """Sends list of commands to dictionary of devices. The dictionary
    should contain the information needed to log into a device. In this
    case it is a netmiko inventory dict."""
    # Run against each device
    all_output = {}
    for device_details in multi_device_details.values():
        hostname = device_details["host"]
        all_output[hostname] = {}
        # Run all commands against each device
        for command in commands:
            device_output = _send_command(device_details, command)
            all_output[hostname][command] = device_output

    return all_output


def format_command_output(command_output: dict[dict:dict]) -> str:
    """Takes the output of each device and commands as dict and formats as string.
    To be used to print or send to file."""
    output = ""
    for device, commands in command_output.items():
        # Format header
        line_spacing = 79
        # Print header for each device
        header = (
            f"{'=' * line_spacing}\n"
            f"{device.center(line_spacing)}\n"
            f"{'=' * line_spacing}\n"
        )
        output += header
        # use enumerate to give the tuple of ndx and tuple
        for ndx, cmd_and_output in enumerate(commands.items()):
            # Unpack the command name, and the output of that command
            command, cmd_output = cmd_and_output
            # Format command output
            # Done print lines between commands if it is the first one
            if ndx != 0:
                output += f"{'-' * line_spacing}\n"
            output += command
            output += f"\n{'-' * line_spacing}\n"
            output += f"{cmd_output}\n"

    return output


if __name__ == "__main__":
    main()
