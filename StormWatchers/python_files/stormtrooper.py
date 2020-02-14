from python_files.event import Event
from python_files.kvstore import KVStore
from python_files.node import ConditionalNode, OperatorNode
from python_files.rule import Rule
# from python_files.bootcamp_emails import BootcampEmails

# from event import Event
# from kvstore import KVStore
# from node import ConditionalNode, OperatorNode
# from rule import Rule

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

        print("READING...")


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
        print("PARSED LIST = ", parsed_list)
        rules = {}
        for index, parsed_dict in enumerate(parsed_list):
            my_rule = Rule()
            my_rule.rule_id = parsed_dict['name']
            my_rule.name = parsed_dict['name']

            # add a root node connected to the tree
            root = OperatorNode('ROOT')
            root._id = '0'
            print("parsed_dict is", parsed_dict)
            root.add_child(self.convert_to_tree(parsed_dict['tree']))
            my_rule.root = root
            # print("root is", root, "parsed_dict is \n\n\n", parsed_dict)


            my_rule.to = parsed_dict['to']
            my_rule.cc = parsed_dict['cc']
            my_rule.bcc = parsed_dict['bcc']

            # set rule_dict
            my_rule.setup_conditions_index_dict()
            rules[my_rule.rule_id] = my_rule
        return rules

    def convert_to_tree(self, tree_as_dict):  # TODO:
        # print("tree as a dict passed in=", tree_as_dict)
        OPERATOR_NODE_ITEMS = 2
        CONDITIONAL_NODE_ITEMS = 6

        operator_conversion = {
            'equal':'==',
            'not equal':'!=',
            'less':'<',
            'less or equal':'<=',
            'greater':'>',
            'greater or equal':'>='
        }

        # length of the dicts can be one or three
        # case length == 1, we have "OR" or "AND" keys - ie an OperatorNode
        # case length == 3, we have a ConditionalNode (3 items are: 'rule', 'comparator', 'value')

        if len(tree_as_dict) == OPERATOR_NODE_ITEMS:
            op = tree_as_dict['condition']
            node = OperatorNode(op)
            children = []
            children_raw_list = tree_as_dict['rules']
            for c in children_raw_list:
                child_node = self.convert_to_tree(c)
                children.append(child_node)
            node.children = children
            return node


        elif len(tree_as_dict) == CONDITIONAL_NODE_ITEMS:
            attribute = tree_as_dict['field']
            comparator = operator_conversion[tree_as_dict['operator']]
            value = tree_as_dict['value']
            return ConditionalNode(attribute, comparator, value)



        print("TREE=", tree_as_dict)
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


    def send_dummy_email(self):
        bootcamp_emails.send_email(["stormtrooper2020labz@gmail.com"], [], "stormtrooper2020labz@gmail.com", 1, 1)

#     def write_rule_by_name(self, path, rule):
#         rule_kv = KVStore(path, 'name')
#         for r in rule_kv.data:
#             print(r)



# StormTrooper().write_rule_by_name("test_files/rules", "RULE2", )
    
    def send_emails(self):
        rule_with_issues = self.get_rule_to_event_list()
        return_email = 'stormtrooper2020labz@gmail.com'
        for r in rule_with_issues:
            rule = self.rules[r]
            issues_list = rule_with_issues[r]
            for issue_number in issues_list:
                print("sending email")
                # send emails with bootcamp_emails in format:
                # to_list, cc_list, return_email_str, issue_number, rule_id
                # BCE = BootcampEmails()
                
                # BCE.send_email(rule.to, rule.cc, return_email, int(issue_number), rule.rule_id)



    # def convert_rule_json_js_to_python(self, js_dict):
    #     to_return = {}
    #     to_return['id'] = js_dict['id']
    #     to_return['name'] = js_dict['name']
    #     to_return['tree'] = self.convert_tree_js_to_python(js_dict['tree'])

    #     return to_return

    # def convert_tree_js_to_python(self, js_tree):
    #     to_return = {}
    #     print("JS TREE = ", js_tree)
    #     # if len(js_tree) == 
    #     return to_return