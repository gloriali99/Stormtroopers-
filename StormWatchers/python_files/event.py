class Event:
    key, issue_number = None, None
    attributes = None
    raw_chain = None

    def __init__(self, key = None):
        self.key = key
        self.issue_number = key
        self.attributes = {}
        self.raw_chain = []
    
    def process_alert_chain_attributes(self):
        avg_severity, max_severity = 0, 0
        for alert_dict in self.raw_chain:
            severity = float(alert_dict["severity"])
            avg_severity += severity
            max_severity = max(max_severity, severity)
        avg_severity /= len(self.raw_chain)

        # add to attributes
        self.attributes['anomalyChainLength'] = len(self.raw_chain)
        self.attributes['avgAnomalySeverity'] = avg_severity
        self.attributes['maxAnomalySeverity'] = max_severity

    def add_cluster_id(self, cluster_id):
        self.attributes['cluster-id'] = cluster_id
