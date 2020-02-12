import random
class Node:
    ID_LENGTH = 16
    _id = None
    _type = None
    
    def id_generator_str(self, length):
        value_str = ''
        for _ in range(length):
            value_str += str(random.randint(0,9))
        return value_str


class OperatorNode(Node):
    '''
    Class that holds information for an OperatorNode (extends Node):

    Fields:
    _id::str - randomly generated str
    _type::str - 'OperatorNode' or 'ConditionalNode'
    value::str - holds 'AND' or 'OR' or 'ROOT' (only single node)
    children::list - holds a list of Nodes (both types)

    Functions: 
    add_child(child::Node) - will add an OpNode or CondNode to children list 
    '''
    value = None
    children = None

    def __init__(self, value):
        self._id = self.id_generator_str(self.ID_LENGTH)
        self._type = 'OperatorNode'
        self.value = value
        self.children = []
    
    def add_child(self, child_node):
        self.children.append(child_node)

    def __str__(self):
        ret = "<<" + self._id + '::' + str(self.value) + ">>: "
        ret += "["
        for c in self.children:
            ret += str(c) + ', '
        ret = ret[:-2]
        ret += ']'
        return ret


class ConditionalNode(Node):
    '''
    Class that holds information for a ConditionalNode (extends Node):

    Fields:
    _id::str - randomly generated str
    _type::str - 'OperatorNode' or 'ConditionalNode'
    attribute::str - holds the attribute name, ie 'maxAnomalySeverity'
    operator::str - holds an operator in str form, ie '<' or '='
    threshold::str - holds threshold (some number), ie '5.5'
    '''
    attribute = None
    operator = None
    threshold = None

    def __init__(self, a, o, t):
        self._id = self.id_generator_str(self.ID_LENGTH)
        self._type = 'ConditionalNode'
        self.attribute = a
        self.operator = o
        self.threshold = t
    
    def __str__(self):
        ret = "<<" + self._id + ">>: "
        ret += str(self.attribute) + ' ' + self.operator + ' ' + self.threshold
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