class Newnode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def push(self, item):
        node = Newnode(item)
        node.next = self.head
        self.head = node

    def pop(self):
        temp = self.head
        self.head = self.head.next
        temp = None

    def isEmpty(self):
        if self.head==None:
            return 1
        return 0

    def peek(self):
        if(self.isEmpty()==1):
            return 1
        return self.head.data

stk = Stack()
stk.push(10)
stk.push(8)
stk.push(12)
stk.pop()
print(stk.peek())