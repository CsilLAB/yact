import common

def display_md(filename, scope):

    json_obj = common.load_json_from_file(filename)

    for item in json_obj.items():
        device_name = item[0]
        print  device_name
        dataset = item[1][scope]

    template_file = 'templates/md/md_table.j2'
    header = common.get_headers(dataset)
    print header
    table = common.get_table(dataset)
    print common.render_table_from_template(template_file, header, table);

def main():
    filename = 'data/output.json'

    display_md(filename, 'interfaces')

if __name__ == "__main__":
    main()
