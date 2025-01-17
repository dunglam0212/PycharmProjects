class Employee:
    def __init__(self, id = None, name=None, age=None):
        self.id = id
        self.name=name
        self.age=age
    def __str__(self):
        return str(self.id)+' - '+self.name+' - '+str(self.age)
