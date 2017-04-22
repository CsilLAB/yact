# stdlib
import sys
import logging
import getpass
import argparse


def build_help():
    parser = argparse.ArgumentParser(
        description='Welcome to YACT!',
        epilog='Automate all the things!!!'
    )
    parser.add_argument(
        '--config_file', '-c',
        dest='config_file',
        action='store',
        help='Configuration file to use.',
        default='config.yml'
    )
    parser.add_argument(
        '--limit', '-l',
        dest='limit',
        action='store',
        help='Limit run to a single device.',
    )
    parser.add_argument(
        '--scope', '-s',
        dest='scope',
        action='store',
        help='Limit run to a single device.',
    )
    parser.add_argument(
        '--debug',
        dest='debug',
        action='store_true',
        help='Enables debug mode; more verbosity.'
    )

    args = parser.parse_args()
    return args


def configure_logging(logger, debug):
    if debug:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.INFO)

    ch = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger


def parse_optional_args(optional_args):

    if optional_args is not None:
        return {x.split('=')[0]: x.split('=')[1] for x in optional_args.replace(' ', '').split(',')}
    return {}
