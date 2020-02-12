class Rule:
    rule_id, name, root, to, cc, bcc = None, None, None, None, None, None
    nodes_index = None


    def Rule(self):
        pass
    
    def delete_node(self, node_id):
        node = self.get_node(node_id)
        if not node:
            return

        parent = self.get_parent_of_id.get(node_id, None)
        if not parent:
            return
        
        # parent and node exists,
        # get index of where child exists
        index_to_remove = -1
        for index, child in enumerate(parent.children):
            if child._id == node_id:
                index_to_remove = index
                break
        
        if index_to_remove > -1:
            parent.children.pop(index_to_remove)
            del nodes_index[node_id]
        
        



    def add_node(self, parent_id, child):
        '''
            Find the node associated to a given id,
            then if it is an OperatorNode, add the given
            node child to the parent
        '''

        node_to_add_to = self.nodes_index.get_node(parent_id, None)
        if node_to_add_to:
            if node_to_add_to._type != 'OperatorNode':
                return
            
            node_to_add_to.add_child(child)

    def get_node(self, node_id):
        '''
            returns the node in the tree with corresponding id
        '''
        return self.nodes_index.get(node_id, None)
    
    def get_parent_of_id(self, node_id):
        '''
            returns the parent of the node in the tree from id
        '''

        # first we check for all nodes,
        # if parameter id exists in that node's children list
        # return the parent
        for node_key in self.nodes_index:
            node = node_key
            if node._type == 'OperatorNode':
                for child in node.children:
                    if child._id == node_id:
                        return node
        return None
        

    def setup_conditions_index_dict(self):
        conditions_index = {}
        to_explore = []
        to_explore.append(self.root)
        while to_explore:
            curr_node = to_explore.pop()
            conditions_index[curr_node._id] = curr_node
            if curr_node._type == 'OperatorNode':
                for child_node in curr_node.children:
                    to_explore.append(child_node)
        self.nodes_index = conditions_index
        


    def __str__(self):
        ret = '\n++++++++++++++++++++++++++++++++++++++++'


        ret += '\nRule class:\n'
        ret += 'id = ' + str(self.rule_id) + '\n'
        ret += 'name = ' + self.name + '\n'
        ret += 'conditions_tree = [[' + str(self.root) + ']]\n'
        ret += "to = " + str(self.to) + '\n'
        ret += "cc = " + str(self.cc) + '\n'
        ret += "bcc = " + str(self.bcc) + '\n'





        ret += '++++++++++++++++++++++++++++++++++++++++\n'
        
        return ret

    
