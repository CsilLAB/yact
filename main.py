#!/usr/bin/env python
# import helpers
from napalm_base import get_network_driver
from lib.helpers import build_help
from lib.helpers import configure_logging
from lib.helpers import parse_optional_args
from lib.device_info import get_device_information
from lib.device_info import build_json

import sys
import yaml
import json
import logging

logger = logging.getLogger('yact')

def get_file_content(config):
    try:
        with open(config, 'r') as f:
            return yaml.load(f.read())
    except IOError:
        print "ERROR"

def get_devices_from_config(config, limit):
    devices = {}
    config = get_file_content(config)
    for device in config.get('devices'):
        temp = {}
        if limit and device.get('hostname') == limit:
            temp.update(config.get('credentials')[device['credentials']])
            temp['driver'] = device['driver']
            temp['ip'] = device['ip']
            break
        else:
            temp.update(config.get('credentials')[device['credentials']])
            temp['driver'] = device['driver']
            temp['ip'] = device['ip']
        devices[device['hostname']] = temp
    return devices

def run(config, limit, scope):
    devices = get_devices_from_config(config, limit)
    try:
        devices_info_bulk = build_json(devices)
    except:
        raise

def main():
    args = build_help()
    configure_logging(logger, args.debug)

    run(args.config_file, args.limit, args.scope)
    sys.exit(0)

if __name__ == '__main__':
    main()
