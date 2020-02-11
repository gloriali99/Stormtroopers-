# class Node:
#     node_operator = False
#     if its false:
#         means node is a condition
#         and will have {
#             attribute, opeartor, threshold
#         }
#     else:
#         node is an opeartor
#         look at its child 

#     name = "AND"
#     children = [Node("child1"), ... ]
#     left = Node("left1")
#     right = "right1"


class OperatorNode:
    # fields:
    # value: "AND" or "OR"
    # children = []
    value = None
    children = None

    def __init__(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        ret = str(self.value) + ": "
        ret += "["
        for c in self.children:
            ret += str(c) + ', '
        ret = ret[:-2]
        ret += ']'
        return ret


class ConditionalNode:
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

# TODO: DELETE
# EXAMPLE OF  WORKS

o1 = OperatorNode('OR')

o2 = OperatorNode('AND')
o2.add_child(ConditionalNode('cpu', '>', '60'))
o2.add_child(ConditionalNode('ram', '>=', '80'))
o2.add_child(ConditionalNode('heat', '>=', '100'))

o1.add_child(ConditionalNode('cpu', '<', '2'))
o1.add_child(o2)

print(o1)