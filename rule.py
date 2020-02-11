class Rule:
    rule_id, name, tree, to, cc, bcc = None, None, None, None, None, None

    def Rule(self):
        pass

    def __str__(self):
        ret = '\n++++++++++++++++++++++++++++++++++++++++'


        ret += '\nRule class:\n'
        ret += 'id = ' + str(self.rule_id) + '\n'
        ret += 'name = ' + self.name + '\n'
        ret += 'tree = ' + str(self.tree) + '\n'
        ret += "to =" + str(self.to) + '\n'
        ret += "cc =" + str(self.cc) + '\n'
        ret += "bcc =" + str(self.bcc) + '\n'





        ret += '++++++++++++++++++++++++++++++++++++++++\n'
        
        return ret

    
