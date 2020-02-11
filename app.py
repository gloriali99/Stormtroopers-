from json_parser import JSonParser

print("Starting application...\n")

test_json = 'test_files/alert_tree'
jsp_list = JSonParser().parse_file_path_to_list(test_json)
rules = JSonParser().convert_list_to_rule(jsp_list)


print("Parsed File:\n", rules)

print("Closing application...")