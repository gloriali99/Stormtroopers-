from json_parser import JSonParser

print("Starting application...\n")

test_json = 'test_files/alert_tree.json'
jsp_dict = JSonParser().parse_file_path_to_dict(test_json)
my_rule = JSonParser().convert_dict_to_rule(jsp_dict)


print("Parsed File:\n", my_rule)

print("Closing application...")