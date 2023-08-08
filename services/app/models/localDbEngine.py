import json

class localStorage:
    def __init__(self):
        """ Initializing the local storage as a database from the data.json file """
        self.__filePath = "data.json"
        self.__data = None

        with open(self.__filePath, 'r') as f:
            self.__data = json.load(f)

    def all(self):
        """ Returns all the data from the local storage """
        return self.__data

    def get(self, el):
        """ Returns a specific element from the local storage """
        obj = self.__data[el]
        return obj