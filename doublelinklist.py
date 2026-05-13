from node import Node

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def print_multilista(self, level=0):
        if self. head is None:
            print("Lista vacia"); return
        current =self.head

        while current:
            