
#########################################################
class Stack:
    def __init__(self):
        self.m_top = Node("null")


    def push(self,value):
        if(self.m_top.value == "null"):
           self.m_top.setValue(value)


        else:

            temp = Node(self.m_top.getValue());
            temp.setNext(self.m_top.getNext());
            self.m_top = Node(value);
            self.m_top.setNext(temp);

    def printStack(self):
        temporary = self.m_top
        while(temporary.getNext() != "null"):
            print(temporary.getValue())
            temporary = temporary.getNext()
        print(self.m_top.getValue())

#########################################################

class Node:
    def __init__(self, value):
        self.value = value
        self.m_next = "null"

    def getValue(self):
        return self.value

    def getNext(self):
        return self.m_next
    def setValue(self,newVal):
        self.value = newVal
    def setNext(self,newNext):
        self.m_next = newNext


end = 0
print("Welcome to my Stack simulator!")
s = Stack()
while(end == 0):
    print("\n1.)Print Stack \n" + "2.)Push Value to Stack \n" + "3.)Pop value \n")
    menuInput = input("Pick a Menu Option: ")

    if(menuInput == 1):
        s.printStack()
    elif(menuInput == 2):
        pushVal = input("What value would you like to push?: ")
        s.push(pushVal)
    elif(menuInput == 3):
        print("#3")
