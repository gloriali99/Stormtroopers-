class OperatorNode:
    '''
    Class that holds information for an OperatorNode:

    Fields:
    value::str - holds 'AND' or 'OR'
    children::list - holds a list of Nodes (both types)

    Functions: 
    add_child(child::Node) - will add an OpNode or CondNode to children list 
    '''
    value = None
    children = None

    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        ret = "OP < " + str(self.value) + " >: "
        ret += "["
        for c in self.children:
            ret += str(c) + ', '
        ret = ret[:-2]
        ret += ']'
        return ret


class ConditionalNode:
    '''
    Class that holds information for a ConditionalNode:

    Fields:
    attribute::str - holds the attribute name, ie 'maxAnomalySeverity'
    operator::str - holds an operator in str form, ie '<' or '='
    threshold::str - holds threshold (some number), ie '5.5'
    '''
    attribute = None
    operator = None
    threshold = None

    def __init__(self, a, o, t):
        self.attribute = a
        self.operator = o
        self.threshold = t
    
    def __str__(self):
        ret = str(self.attribute) + ' ' + self.operator + ' ' + self.threshold
        return ret



# EXAMPLE OF HOW TREE WORKS

# o1 = OperatorNode('OR')

# o2 = OperatorNode('AND')
# o2.add_child(ConditionalNode('cpu', '>', '60'))
# o2.add_child(ConditionalNode('ram', '>=', '80'))
# o2.add_child(ConditionalNode('heat', '>=', '100'))

# o1.add_child(ConditionalNode('cpu', '<', '2'))
# o1.add_child(o2)

# print(o1)