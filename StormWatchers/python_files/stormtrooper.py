from json_parser import JSONParser
from event import Event

class StormTrooper:
    '''
    Class that holds information on the app
    '''
    rules = None
    events = None


    def __init__(self):
        rules = []
        events = []
        pass

    def read_rules(self, file_path):
        json_parser = JSONParser()
        rules_raw = json_parser.parse_path_to_list(file_path, 'id')
        self.rules = json_parser.convert_list_to_rules(rules_raw)
    
    def read_events(self, events_path, event_info_path):
        json_parser = JSONParser()
        events_raw = json_parser.parse_path_to_list(events_path, 'issue_number')
        event_info_raw = json_parser.parse_path_to_list(event_info_path, '_key')
        self.events = self.generate_event_list(events_raw, event_info_raw)
    
    def generate_event_list(self, events_raw, event_info_raw):
        event_list = []
        for i, event_info_dict in enumerate(event_info_raw):
            event_dict = events_raw[i]
            e = Event(str(i))
            e.raw_chain = event_dict['alert-chain']
            e.process_alert_chain_attributes()
            e.add_cluster_id(event_info_dict['cluster_id'])
            event_list.append(e)
        return event_list
