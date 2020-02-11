from kvstore import KVStore
from rule import Rule
from node import ConditionalNode, OperatorNode, RootNode

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
        OPERATOR_NODE_ITEMS = 1
        CONDITIONAL_NODE_ITEMS = 3
        # length of the dicts can be one or three
        # case length == 1, we have "OR" or "AND" keys - ie an OperatorNode
        # case length == 3, we have a ConditionalNode (3 items are: 'rule', 'comparator', 'value')

        if len(tree_as_dict) == OPERATOR_NODE_ITEMS:
            for key in tree_as_dict:
                root = OperatorNode(str(key))
                children = []  # list of Nodes (either OperatorNode or ConditionalNode)
                children_raw_list = tree_as_dict[key]

                # recursively apply to all children
                for c in children_raw_list:
                    node = self.convert_to_tree(c)
                    children.append(node)
                root.children = children
                return root

        # if len(dict) == 3, we have a ConditionalNode
        # convert it to a ConditionalNode and return that
        elif len(tree_as_dict) == CONDITIONAL_NODE_ITEMS:
            rule = tree_as_dict['rule']
            comparator = tree_as_dict['comparator']
            value = tree_as_dict['value']
            return ConditionalNode(rule, comparator, value)

        return None