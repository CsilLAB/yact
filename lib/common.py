import json
import os

DIRECTORY = os.getcwd().replace('lib','');

def load_json_from_file(json_file):
    """ Return json data """
    with open(DIRECTORY + json_file) as json_data:
        return json.load(json_data)
