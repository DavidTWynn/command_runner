# Command Runner

Working on a basic command runner to run SSH commands to multiple devices.

Currently working with netmiko. Pulls list of hostnames or IPs from src/input/devices.txt
and runs commands against them.

# Getting started

## Basic install

```bash
git clone https://github.com/DavidTWynn/command_runner.git
cd command_runner
python -m pip install requirements.txt
```

## Config

1. devices.txt
2. commands.txt

Create a devices.txt file in the input directory based off of the devices_example.txt file.
These devices will be logged into via ssh and commands will be ran against them.

Can be IPv4 address or hostname

```bash
> cat devices.txt
127.0.0.1
127.0.0.2
127.0.0.3
localhost
localhost.localhost
```

Edit commands.txt with the commands you want sent to each device

```bash
> cat commands.txt
show int gi0/0 description
show int gi0/0 | i MTU
```

## Run script

```python
> python src/command_runner.py
[09/18/22 14:23:28] INFO     main() Starting Script                                                                                command_runner.py:18Username: david
Password:
===============================================================================
                                  10.0.100.27
===============================================================================
show int gi0/0 description
-------------------------------------------------------------------------------
Interface                      Status         Protocol Description
Gi0/0                          up             up
-------------------------------------------------------------------------------
show int gi0/0 | i MTU
-------------------------------------------------------------------------------
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,
===============================================================================
                                  10.0.100.46
===============================================================================
show int gi0/0 description
-------------------------------------------------------------------------------
Interface                      Status         Protocol Description
Gi0/0                          up             up
-------------------------------------------------------------------------------
show int gi0/0 | i MTU
-------------------------------------------------------------------------------
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,
===============================================================================
                                  10.0.100.45
===============================================================================
show int gi0/0 description
-------------------------------------------------------------------------------
Interface                      Status         Protocol Description
Gi0/0                          up             up
-------------------------------------------------------------------------------
show int gi0/0 | i MTU
-------------------------------------------------------------------------------
  MTU 1500 bytes, BW 1000000 Kbit/sec, DLY 10 usec,

[09/18/22 14:24:02] INFO     main() Script completed. Finished in 33.78 second(s)                                                  command_runner.py:41                    INFO     main() DONE
```
