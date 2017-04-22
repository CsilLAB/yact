""" Display text """

import common
import tabulate


def display_text(filename, scope):
    json_obj = common.load_json_from_file(filename)

    for item in json_obj.items():
        device_name = item[0]
        print  device_name
        dataset = item[1][scope]

        headers = common.get_headers(dataset)
        table = common.get_table(dataset)

    print tabulate.tabulate(table, headers, tablefmt="fancy_grid")

def main():
    filename = 'data/output.json'

    display_text(filename, 'interfaces')
    display_text(filename, 'interfaces_counters')
    #display_text(filename, 'lldp_neighbors')

if __name__ == "__main__":
    main()
