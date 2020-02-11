import json

class JSonParser:
    def parse_file_path_to_dict(self, file_path):
        f = open(file_path, 'r')
        fstr = f.read()
        loaded = json.loads(fstr)
        return loaded

    # def convet_dict_to_tree(self, parsed_dict):
