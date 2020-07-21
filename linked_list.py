class linknode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.start = None
        self.end = None

    def insert_at_head(self, item):
        node = linknode(item)
        node.next = self.start
        self.start = node
        self.end = node.next

    def insert_at_end(self, item):
        node = linknode(item)
        if(self.start==None):
            node.next = self.start
            self.start = node
            self.end = node
        else:
            self.end.next = node
            node.next = None
            self.end = node

    def printList(self):
        node = self.start
        while node:
            print(node.data)
            node = node.next

arr = LinkedList()
arr.insert_at_end(5)
arr.insert_at_head(20)
arr.insert_at_end(8)
arr.insert_at_end(2)
arr.insert_at_head(16)
arr.printList()