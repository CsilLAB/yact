""" Display text """

import common
import tabulate


def display_text():
    df = 'data/dummy.json'
    json_obj = common.load_json_from_file(df)

    # get headers
    headers = ['']
    headers = headers + (json_obj.items()[0][1].keys())

    table = []
    for i in range(0, len(json_obj)):
        line = [json_obj.items()[i][0]]
        for item in json_obj.items()[i][1].items():
            line.append(item[1])
        table.append(line)

    print tabulate.tabulate(table, headers, tablefmt="fancy_grid")

def main():
    display_text()

if __name__ == "__main__":
    main()
