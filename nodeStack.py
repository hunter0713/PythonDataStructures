print("Welcome to my Stack simulator!" + "\n" + "1.)Print Stack \n" + "2.)Add Value to Stack \n" + "3.)Pop value \n")

menuInput = input("Pick a Menu Option: ")
if(menuInput == 1):
    printStack
elif(menuInput == 2):
    add to stack
elif(menuInput == 3):
    pop value
















#########################################################
class Stack:
    def __init__(self, m_top):
        self.m_top = Node(0,null)

    def push(self,value):
        if(self.m_top.value == 0):
           m_top = Node(value);
            
        
        else:
    
            temp = Node(m_top.getValue());
            temp.setNext(m_top.getNext());
            m_top = Node(value);
            m_top.setNext(temp);

#########################################################
        
class Node:
    def __init__(self, value, m_next):
        self.value = value
        self.m_next = m_next

    def getValue(self):
        return self.value

    def getNext(self):
        return self.m_next
    def setValue(self,newVal):
        self.value = newVal
    def setNext(self,newNext):
        self.m_next = newNext
