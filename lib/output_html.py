import common

def display_html(filename, scope):

    json_obj = common.load_json_from_file(filename)

    for item in json_obj.items():
        device_name = item[0]
        print  device_name
        dataset = item[1][scope]

    template_file = 'templates/html/table1.html'
    header = common.get_headers(dataset)
    print header
    table = common.get_table(dataset)
    print common.render_table_from_template(template_file, header, table);

def main():
    filename = 'data/output.json'

    display_html(filename, 'interfaces')

if __name__ == "__main__":
    main()
