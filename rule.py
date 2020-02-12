class Rule:
    rule_id, name, root, to, cc, bcc = None, None, None, None, None, None
    conditions_index = None


    def Rule(self):
        pass
    

    # def add(self, id, node):

    
    def get(self, id):
        '''
            returns the node in the tree with corresponding id
        '''
        return self.conditions_index.get(id, None)
        

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
        self.conditions_index = conditions_index
        


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

    
