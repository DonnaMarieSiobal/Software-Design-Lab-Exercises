class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class Stack:
     def __init__(self):
         self.head = None
     def isempty(self):
         if self.head == None:
               return True
         else:
               return False
     def push(self, data):

         if self.head == None:
               self.head = Node(data)
         else:
               newnode = Node(data)
               newnode.next = self.head
               self.head = newnode
     def pop(self):

         if self.isempty():
               return None
         else:
               poppednode = self.head
               self.head = self.head.next
               poppednode.next = None
               return poppednode.data

     def peek(self):

         if self.isempty():
               return None
         else:
               return self.head.data

     def display(self):
         iternode = self.head
         if self.isempty():
               print("Stack Underflow")
         else:
               while (iternode != None):
                   print(iternode.data, "->", end=" ")
                   iternode = iternode.next
               return


MyStack = Stack()
MyStack.push(45)
MyStack.push(67)
MyStack.push(19)
MyStack.push(35)
MyStack.push(80)
MyStack.display()

print("\nThe left element is ", MyStack.peek())

MyStack.pop()
print("\nElement after pop:")
MyStack.display()

print("\nThe right element is ", MyStack.peek())

