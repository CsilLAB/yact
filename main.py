# import helpers
from napalm_base import get_network_driver
from helpers import build_help
from helpers import configure_logging
from helpers import parse_optional_args

import sys
import yaml
import json
import logging
logger = logging.getLogger('main.py')

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

def main():
    args = build_help()
    configure_logging(logger, args.debug)

    run(args.config_file, args.limit, args.scope)
    sys.exit(0)

if __name__ == '__main__':
    main()
