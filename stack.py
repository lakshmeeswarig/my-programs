class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items ==[]
    def push(self,data):
        self.items.append(data)
    def pop(self):
        return self.items.pop()
    def items_in_stack(self):
        for i in range(len(self.items)-1, -1, -1):
            print(self.items[i])

s=Stack()
while True :
    """ select one from the stack operations below
        1. push
        2. pop
        3. Display stack elements
        4. exit
        Enter your choice between 1 to 4 """
    ch=input()
    if ch=='1' :   
        d=int(input('enter an element to push into stack'))
        s.push(d)
    elif ch=='2' : 
        if s.is_empty():
            print('the stack is empty so there is nothing to delete')
        else :
            print('the deleted element is ',s.pop())
    elif ch=='3' : 
        if s.is_empty():
            print('the stack is empty so there is nothing to delete')
        else :
            print('the items in the stack are ')
            s.items_in_stack()
    else : break
