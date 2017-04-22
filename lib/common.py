import json
import os
from jinja2 import Environment, PackageLoader, FileSystemLoader, StrictUndefined

DIRECTORY = os.getcwd().replace('lib','');

def load_json_from_file(json_file):
    """ Return json data """
    with open(os.path.join(DIRECTORY, json_file)) as json_data:
        return json.load(json_data)

def render_table_from_template(template_file, header, table, device, scope):
    env = Environment(loader=FileSystemLoader(DIRECTORY), undefined=StrictUndefined)
    template = env.get_template(template_file)
    return template.render(header=header, table=table, device=device, scope=scope)

def get_headers(dataset):
    return [' <> '] + (dataset.items()[0][1].keys())

def get_table(dataset):
    table = []
    for i in range(0, len(dataset)):
        line = [dataset.items()[i][0]]
        for item in dataset.items()[i][1].items():
            line.append(item[1])
        table.append(line)
    return table

def append_to_file(filename, text):
    file = open(os.path.join(DIRECTORY, filename),'a')
    file.write(text.encode('utf8'))
    file.close()

def clear_file(filename):
    file = open(os.path.join(DIRECTORY, filename),'w')
    file.close()


