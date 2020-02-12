from json_parser import JSONParser

class StormTrooper:
    '''
    Class that holds information on the app
    '''
    rules = None


    def __init__(self):
        pass

    def read_rules(self, file_path):
        json_parser = JSONParser()
        rules_raw = json_parser.parse_file_path_to_list(file_path)
        self.rules = json_parser.convert_list_to_rules(rules_raw)
    
    # def execute_and_email(self):
    # read rules
    # read events/issues
    
    # compare 
    