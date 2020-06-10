class Queue:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return self.items==[]
    def insert(self,data):
        self.items.append(data)
    def delete(self):
        return self.items.pop(0)
    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else :
            print('The items in the queue are ')
            for i in range(0,len(self.items)):
                print(i)
#create an object for class Queue
q=Queue()
# insert elements into Queue
for i in range(10,15):
    q.insert(i)
#display the elements in the queue
q.display()
#delete the elements in the queue
while not q.is_empty():
    print(' the deleted element is ', q.delete())
#recheck the elements in the queue
q.display()