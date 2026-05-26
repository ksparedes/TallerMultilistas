class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.prev = None
        self.sub_list = None

class Country(Node):
    pass

class Department(Node):
    pass

class City(Node):
    def __init__(self, id, name, lat=None, lon=None):
        super().__init__(id, name)
        self.lat = float(str(lat).replace(",", ".")) if lat else None
        self.lon = float(str(lon).replace(",", ".")) if lon else None  
