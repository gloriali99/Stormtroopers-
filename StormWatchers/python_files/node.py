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

    def apply_comparison(self, event_attributes):  # boolean function: returns True or False
        if self._type == 'ConditionalNode':
            # check to see if attribute exists as an event attribute,
            # if it doesn't, return False
            # if it is true, we get the value of the event from the key (attribute)
            # append that with this node's operator and threshold
            # run python's function 'eval' on this string to evaluate into a boolean
            attribute_value = event_attributes.get(self.attribute, None)
            if not attribute_value:
                return False
            eval_str = str(attribute_value) + ' ' + str(self.operator) + ' ' + str(self.threshold)
            return eval(eval_str)

        if self._type == 'OperatorNode':
            for child_node in self.children:
                if self.value == 'OR' and child_node.apply_comparison(event_attributes):
                    return True
                elif self.value == 'AND' and not child_node.apply_comparison(event_attributes):
                    return False

            # if node is OR, node would've been early exited if any one is True
            # if none are true, (ie all is false) we will return false
            # similar logic for AND, if one is not true, we would have returned False
            # so we return True
            if self.value == 'OR':
                return False
            else:
                return True 


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
        ret = "<<{}>>:".format(self.value)
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
        ret = ''
        ret += str(self.attribute) + ' ' + self.operator + ' ' + self.threshold
        return ret