import common

def display_md(filename, scope):

    json_obj = common.load_json_from_file(filename)

    for item in json_obj.items():
        device_name = item[0]
        dataset = item[1][scope]

        template_file = 'templates/md/md_table.j2'
        header = common.get_headers(dataset)
        table = common.get_table(dataset)

    output = common.render_table_from_template(template_file, header, table, device_name, scope);
    print output
    return output

def main():
    filename = 'data/output.json'
    output_file = 'output/output.md'

    common.clear_file(output_file)
    common.append_to_file(output_file, display_md(filename, 'interfaces_counters'))
    common.append_to_file(output_file, display_md(filename, 'interfaces'))

if __name__ == "__main__":
    main()
