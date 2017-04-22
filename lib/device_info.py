import time
import logging
import json

from napalm_base import get_network_driver

logger = logging.getLogger('yact')


def get_device_information(device_name, device_details):
    driver = get_network_driver(device_details["driver"])

    try:
        with driver(device_details["ip"], device_details["username"], device_details["password"]) as device:
            device_facts = device.get_facts()
            device_interfaces = device.get_interfaces()
            device_interfaces_counters = device.get_interfaces_counters()

    except:
        logger.exception("Unexpected failure when connecting to device with IP %s", device_details["ip"])
        raise
    else:
        logger.info("Connection successful to {}, a {} device at {}"
                    .format(device_name, device_facts["model"], device_details["ip"]))

    device_details["interfaces"] = device_interfaces
    device_details["interfaces_counters"] = device_interfaces_counters
    return device_details

def build_json(devices):
    devices_information = {}
    for device in devices.keys():
        device_details = devices[device]
        device_information = get_device_information(device, device_details)
        devices_information[device] = device_information

        with open("data/output.json", "w") as f:
            f.write(json.dumps(devices_information, indent=4))

