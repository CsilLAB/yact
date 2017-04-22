""" Display text """

import common
import tabulate


def display_text(filename, scope):
    json_obj = common.load_json_from_file(filename)
    output = ''

    for item in json_obj.items():
        device_name = item[0]
        print "====" + device_name + "===="
        print "--" + scope + '--'
        dataset = item[1][scope]

        headers = common.get_headers(dataset)
        table = common.get_table(dataset)

        output += tabulate.tabulate(table, headers, tablefmt="fancy_grid")
    print output
    return output

def main():
    filename = 'data/output.json'
    output_file = 'output/output.txt'

    common.clear_file(output_file)
    common.append_to_file(output_file, display_text(filename, 'interfaces'))
    common.append_to_file(output_file, display_text(filename, 'interfaces_counters'))
    #display_text(filename, 'lldp_neighbors')

if __name__ == "__main__":
    main()
