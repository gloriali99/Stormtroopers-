from json_parser import JSonParser

print("Starting application...\n")

test_json = 'test_files/alert_tree.json'
jsp = JSonParser().parse_file_path_to_dict(test_json)

print("Parsed File:\n", jsp)

print("Closing application...")