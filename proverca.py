import json

class Proverca:
    def __init__(self):
        self.rules = []

    def load(self):
        with open('Rule.json', 'r',) as file:
            data = json.load(file)
            print(data)