import json
from rule import Rule

class JSonParser:
    def parse_file_path_to_dict(self, file_path):
        f = open(file_path, 'r')
        fstr = f.read()
        loaded = json.loads(fstr)
        return loaded

    def convert_dict_to_rule(self, parsed_dict):
        my_rule = Rule()
        my_rule.rule_id = parsed_dict['rule_id']
        my_rule.name = parsed_dict['name']
        my_rule.tree = self.convert_to_tree(parsed_dict['tree'])
        my_rule.to = parsed_dict['to']
        my_rule.cc = parsed_dict['cc']
        my_rule.bcc = parsed_dict['bcc']
        return my_rule
    
    def convert_to_tree(self, tree_as_dict):  # TODO
        return "ret"