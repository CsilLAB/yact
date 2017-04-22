from napalm_base import get_network_driver
import logging
import json

logger = logging.getLogger('yact')

GETTERS_MAPPER = {
    'get_interfaces': 'Interfaces',
    'get_facts': 'Facts'
}

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def validate(devices, debug):
    complies = False
    for device in devices:
        print '\n================================'
        print 'Validating {0}..'.format(device)
        print '================================\n'
        driver = get_network_driver(devices[device]["driver"])
        device_config = {
            "hostname": devices[device]["ip"],
            "username": devices[device]["username"],
            "password": devices[device]["password"]
        }
        dev = driver(**device_config)
        dev.open()
        validation_file = "validation_files/validate-{0}.yml".format(device)
        validation_results = dev.compliance_report(validation_file)

        for result in validation_results:
            if result in GETTERS_MAPPER:
                if validation_results[result].get('complies'):
                    print bcolors.OKGREEN + "{0}".format(GETTERS_MAPPER[result]) + bcolors.ENDC
                else:
                    complies = False
                    print bcolors.FAIL + "{0}".format(GETTERS_MAPPER[result]) + bcolors.ENDC

    if not complies:
        if debug:
            print bcolors.WARNING + "\nValidation results..." + bcolors.ENDC
            print bcolors.WARNING + json.dumps(validation_results, indent=4) + bcolors.ENDC
        else:
            print bcolors.BOLD + "Use --debug to get full information" + bcolors.ENDC
