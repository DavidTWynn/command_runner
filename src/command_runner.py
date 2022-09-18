import getpass
import netmiko


def main():
    username, password = get_login_info()
    devices = import_devices("input/devices.txt")
    device_inventory = create_device_inventory(username, password, devices)
    commands = ["show ip int b | e una"]
    command_outputs = send_commands(device_inventory, commands)
    print_command_output(command_outputs)


def get_login_info() -> tuple[str][str]:
    pass


def import_devices(filename: str) -> list[str]:
    pass


def create_device_inventory(
    username: str, password: str, devices: list[str]
) -> list[dict]:
    pass


def _send_command(device_details: dict, command: str) -> str:
    pass


def send_commands(
    multi_device_details: list[dict], commands: list[str]
) -> dict[str:str]:
    pass


def print_command_output(command_ouput: dict[str]) -> bool:
    pass


if __name__ == "__main__":
    main()
