import pytest

from src.command_runner import import_devices


def test_len():
    devices = import_devices("src/input/devices.txt")
    assert len(devices) == 5


def test_10_0_100_27():
    devices = import_devices("src/input/devices.txt")
    assert "10.0.100.27" in devices


@pytest.mark.xfail
def test_bad_file():
    devices = import_devices("src/input/devices")
