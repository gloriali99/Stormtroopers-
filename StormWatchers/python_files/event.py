class Event:
    MAX_INT = 9223372036854775807
    key, issue_number = None, None
    attributes = None
    raw_chain = None

    def __init__(self, key = None):
        self.key = key
        self.issue_number = key
        self.attributes = {}
        self.raw_chain = []
    
    def process_alert_chain_attributes(self):
        avg_severity, max_severity, min_tier = 0, 0, self.MAX_INT
        for alert_dict in self.raw_chain:

            # severity
            severity = float(alert_dict["severity"])
            avg_severity += severity
            max_severity = max(max_severity, severity)

            # get lowest number tier (lower = more severe)
            tier = float(alert_dict["tier"])
            if tier < min_tier:
                min_tier = tier

        # divide sum of severity by number of items in chain to get avg
        avg_severity /= len(self.raw_chain)

        # add to attributes
        self.attributes['anomalyChainLength'] = len(self.raw_chain)
        self.attributes['avgAnomalySeverity'] = avg_severity
        self.attributes['maxAnomalySeverity'] = max_severity
        self.attributes['highestTier'] = min_tier

    def add_cluster_id(self, cluster_id):
        self.attributes['cluster_id'] = cluster_id
    
    def add_duration(self, duration):
        self.attributes['duration'] = duration
