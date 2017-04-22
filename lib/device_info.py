import time
import logging
import json
import jtextfsm as textfsm

from napalm_base import get_network_driver

logger = logging.getLogger('yact')

class NoDriverException(Exception):
    pass


def get_ospf_neighbors(driver, device):
    # TODO Normalize output dictionary
    if driver == "eos":
        command_output = device.cli(["show ip ospf neighbor"])["show ip ospf neighbor"]
        fsm_handler = textfsm.TextFSM(open('templates/textfsm/arista_eos_show_ip_ospf_neighbor.template'))
    elif driver == "junos":
        command_output = device.cli(["show ospf neighbor"])["show ospf neighbor"]
        fsm_handler = textfsm.TextFSM(open('templates/textfsm/juniper_junos_show_ospf_neighbor.template'))
    else:
        raise NoDriverException("Driver {} not supported by the get_ospf_neighbors method!".format(driver))

    textfsm_data = list()
    objects = fsm_handler.ParseText(command_output)

    for obj in objects:
        index = 0
        entry = {}
        for entry_value in obj:
            entry[fsm_handler.header[index].lower()] = entry_value
            index += 1
        textfsm_data.append(entry)

    return textfsm_data


def get_device_information(device_name, device_details):
    driver = get_network_driver(device_details["driver"])

    try:
        device = driver(device_details["ip"], device_details["username"], device_details["password"])
        device_facts = device.open()
        device_facts = device.get_facts()
        device_interfaces = device.get_interfaces()
        device_interfaces_ip = device.get_interfaces_ip()
        device_interfaces_counters = device.get_interfaces_counters()
        device_bgp_config = device.get_bgp_config()
        device_bgp_neighbors = device.get_bgp_neighbors()
        device_bgp_neighbors_detail = device.get_bgp_neighbors_detail()
        device_lldp_neighbors = device.get_lldp_neighbors()
        device_lldp_neighbors_detail = device.get_lldp_neighbors_detail()
        device_ospf_neighbors = get_ospf_neighbors(device_details["driver"], device)
    except:
        logger.exception("Unexpected failure when doing stuff to device with IP %s", device_details["ip"])
        raise
    else:
        logger.info("Connection successful to {}, a {} device at {}"
                    .format(device_name, device_facts["model"], device_details["ip"]))

    device_details["facts"] = device_facts
    device_details["interfaces"] = device_interfaces
    device_details["interfaces_ip"] = device_interfaces_ip
    device_details["interfaces_counters"] = device_interfaces_counters
    device_details["bgp_config"] = device_bgp_config
    device_details["bgp_neighbors"] = device_bgp_neighbors
    device_details["bgp_neighbors_detail"] = device_bgp_neighbors_detail
    device_details["lldp_neighbors"] = device_lldp_neighbors
    device_details["lldp_neighbors_detail"] = device_lldp_neighbors_detail
    device_details["ospf_neighbors"] = device_ospf_neighbors

    return device_details

def build_json(devices):
    devices_information = {}
    for device in devices.keys():
        device_details = devices[device]
        device_information = get_device_information(device, device_details)
        devices_information[device] = device_information

        with open("data/output.json", "w") as f:
            f.write(json.dumps(devices_information, indent=4))

    return devices_information
