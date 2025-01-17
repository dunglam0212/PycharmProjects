import json

class Employee:
    def __init__(self, fullname=None, gender=None, city=None):
        self.fullname = fullname
        self.gender=gender
        self.city=city
    def __str__(self):
        return json.dumps(self.__dict__)
