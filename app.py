from json_parser import JSonParser

print("Starting application...\n")

test_json = 'test_files/rules'
jsp_list = JSonParser().parse_file_path_to_list(test_json)
rules = JSonParser().convert_list_to_rules(jsp_list)
print("Parsed File:\n", rules)

print("Rules are:")
for r in rules:
    print("HERE:", r, "\nRoot:  ", r.get_node('0'))
    
    



print("Closing application...")