class Newnode:
    def __init__(self, data):
        self.data = data
        self.next = None

class MinStack:

    def __init__(self):
        self.head = None
        self.mi = None

    def push(self, x):
        temp = Newnode(x)
        if self.mi==None and temp!=None:
            self.mi = temp.data
            temp.next = self.head
            self.head = temp
        else:
            if temp.data<self.mi:
                temp.data = 2*(temp.data) - self.mi
                self.mi = x 
                temp.next = self.head
                self.head = temp
            else:
                temp.next = self.head
                self.head = temp
                
    def pop(self):
        temp = self.head
        if temp!=None:
            if temp.data < self.mi:
                self.mi = 2*(self.mi)-temp.data
        self.head = self.head.next
        if self.head==None:
            self.mi = None
        temp = None
        
    def top(self):
        if self.head != None:
            x = self.head.data
            if x<self.mi:
                x = self.mi
        else:
            x = None
        return x
    
    def getMin(self):
        return self.mi

stk = MinStack()
stk.push(10)
stk.push(12)
stk.push(8)
print(stk.getMin())
stk.pop()
print(stk.getMin())