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

    def OperatorNode(self, value):
        self.value = value
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)


class ConditionalNode:
    attribute = None
    operator = None
    threshold = None

    def ConditionalNode(self, a, o, t):
        self.attribute = a
        self.operator = o
        self.threshold = t
