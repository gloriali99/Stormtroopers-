from event import Event
from kvstore import KVStore
from node import ConditionalNode, OperatorNode
from rule import Rule
# from bootcamp_emails import send_emails

class StormTrooper:
    '''
    Class that holds information on the app
    '''
    rules = None
    events = None
    rules_to_be_emailed = None


    def __init__(self):
        rules = []
        events = []
        pass

    def read_rules(self, file_path):
        rules_raw = self.parse_path_to_list(file_path, 'id')
        self.rules = self.convert_list_to_rules(rules_raw)
    
    def read_events(self, events_path, event_info_path):
        events_raw = self.parse_path_to_list(events_path, 'issue_number')
        event_info_raw = self.parse_path_to_list(event_info_path, '_key')
        self.events = self.generate_event_list(events_raw, event_info_raw)
    
    def generate_event_list(self, events_raw, event_info_raw):
        event_list = {}
        for i, event_info_dict in enumerate(event_info_raw):
            event_dict = events_raw[i]
            e = Event(str(i))
            e.raw_chain = event_dict['alert-chain']
            e.process_alert_chain_attributes()
            e.add_cluster_id(event_info_dict['cluster_id'])
            e.add_duration(event_info_dict['duration'])
            event_list[e.key] = e
        return event_list

    def parse_path_to_list(self, file_path, key):
        events_kv = KVStore(file_path, key)
        return events_kv.data


    # turn JSON dict format into a python dict of rule objects
    def convert_list_to_rules(self, parsed_list):
        rules = {}
        for parsed_dict in parsed_list:
            my_rule = Rule()
            my_rule.rule_id = parsed_dict['id']
            my_rule.name = parsed_dict['name']

            # add a root node connected to the tree
            root = OperatorNode('ROOT')
            root._id = '0'
            root.add_child(self.convert_to_tree(parsed_dict['tree']))
            my_rule.root = root


            my_rule.to = parsed_dict['to']
            my_rule.cc = parsed_dict['cc']
            my_rule.bcc = parsed_dict['bcc']

            # set rule_dict
            my_rule.setup_conditions_index_dict()
            rules[my_rule.rule_id] = my_rule
        return rules

    def convert_to_tree(self, tree_as_dict):  # TODO:
        OPERATOR_NODE_ITEMS = 1
        CONDITIONAL_NODE_ITEMS = 3
        # length of the dicts can be one or three
        # case length == 1, we have "OR" or "AND" keys - ie an OperatorNode
        # case length == 3, we have a ConditionalNode (3 items are: 'rule', 'comparator', 'value')

        if len(tree_as_dict) == OPERATOR_NODE_ITEMS:
            for key in tree_as_dict:
                node = OperatorNode(str(key))
                children = []  # list of Nodes (either OperatorNode or ConditionalNode)
                children_raw_list = tree_as_dict[key]

                # recursively apply to all children
                for c in children_raw_list:
                    child_node = self.convert_to_tree(c)
                    children.append(child_node)
                node.children = children
                return node

        # if len(dict) == 3, we have a ConditionalNode
        # convert it to a ConditionalNode and return that
        elif len(tree_as_dict) == CONDITIONAL_NODE_ITEMS:
            rule = tree_as_dict['rule']
            comparator = tree_as_dict['comparator']
            value = tree_as_dict['value']
            return ConditionalNode(rule, comparator, value)

        return None


    # return {rule_id : [issue_number] } - dictionary with keys = rule_id, corresponding
    # to which issue_number (event) matches with that rule_id
    def get_rule_to_event_list(self):
        to_return = {}
        ops = 0
        for event_id in self.events:
            event = self.events[event_id]
            for rule_id in self.rules:
                ops += 1
                rule = self.rules[rule_id]
                node = rule.root.children[0]
                if node.apply_comparison(event.attributes):
                    rule_list = to_return.get(rule.rule_id, [])
                    rule_list.append(event.key)
                    to_return[rule.rule_id] = rule_list
        self.rules_to_be_emailed = to_return
        return to_return

    
    # def send_emails(self):
    #     rule_with_issues = self.get_rule_to_event_list()
    #     return_email = 'return@return.accenture_bootcamp.com'
    #     for r in rule_with_issues:
    #         rule = self.rules[r]
    #         issues_list = rule_with_issues[r]
    #         for issue_number in issues_list:

    #             # send emails with bootcamp_emails in format:
    #             # to_list, cc_list, return_email_str, issue_number, rule_id
    #             bootcamp_emails.send_emails(rule.to, rule.cc, return_email, issue_number, rule.rule_id)

