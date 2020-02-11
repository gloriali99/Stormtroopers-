from kvstore import KVStore
from rule import Rule

class JSonParser:
    def parse_file_path_to_list(self, file_path):
        events_kv = KVStore(file_path, 'id')
        return events_kv.data

    def convert_list_to_rules(self, parsed_list):
        rules = []
        for parsed_dict in parsed_list:

            my_rule = Rule()
            my_rule.rule_id = parsed_dict['id']
            my_rule.name = parsed_dict['name']
            my_rule.tree = self.convert_to_tree(parsed_dict['tree'])
            my_rule.to = parsed_dict['to']
            my_rule.cc = parsed_dict['cc']
            my_rule.bcc = parsed_dict['bcc']
            rules.append(my_rule)
        return rules
    
    def convert_to_tree(self, tree_as_dict):  # TODO:

        return "ret"