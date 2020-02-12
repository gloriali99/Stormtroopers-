import json

class KVStore():

    def __init__(self, collection, key='id'):
        # Format headers, store auth and collection data.
        self.collection = collection
        self.key = key
        with open(self.collection + '.json') as in_file:
            self.data = json.load(in_file)
        

    def post_one(self, data):
        self.data.append(data)
        with open(self.collection + '.json', 'w') as json_file:
            json.dump(data, json_file)


    def post_all(self, data):
        with open(self.collection + '.json', 'w') as json_file:
            json.dump(data, json_file)

    def get_all(self):
        return self.data

    def delete_all(self):
        self.data = []
        with open(self.collection + '.json', 'w') as json_file:
            json.dump(self.data, json_file)

    def put_one(self, id_, data):
        for index, item in enumerate(self.data):
            if id_ == self.data[index][self.key]:
                self.data[index] = data
                break
            

    def delete_one(self, id_):
        for index, item in enumerate(self.data[:]):
            if self.data[index][self.key] == id_:
                del self.data[index]
                break

    def get_one(self, id_):
        for index, item in enumerate(self.data):
            if id_ == self.data[index][self.key]:
                return self.data[index]