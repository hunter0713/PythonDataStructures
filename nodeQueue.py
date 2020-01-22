#@author: Hunter Cobb, University of Kansas , @file: nodeQueue.py , @date: 1/22/20, @brief: Node Based Queue object
#class. Includes building the stack and the Nodes that build the stack.
##########Node Class###############################################

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

############Stack Class#############################################
class Queue:
    def __init__(self):
        self.m_front = Node("null")
        self.m_back = Node("null")


    def enqueue(self,value):
        temp = self.m_back
        if(self.m_front.getValue() == "null"):
            self.m_front.setValue(value)
        else:
            if(self.m_back.getValue() == "null"):
                self.m_back.setValue(value)
                self.m_front.setNext(self.m_back)
            else:
                self.m_back = Node(value)
                temp.setNext(self.m_back)
    def dequeue(self):
        if(self.m_front != "null"):
            if(self.m_back == "null"):
                self.m_front.setValue("null")
            else:
                self.m_front = self.m_front.getNext()
    def peek(self):
        return(str(self.m_front.getValue()))

    def printQueue(self):
        temporary = self.m_front
        while(temporary != "null"):
            print(temporary.getValue())
            temporary = temporary.getNext()
###########Menu Code###################################################
end = 0
print("Welcome to my Stack simulator!")
s = Queue()
while(end == 0):
    print("\n1.)Print Queue \n" + "2.)Enqueue Value\n" + "3.)Dequeue value \n" + "4.)Peek Front Value\n" + "5.)Exit\n")
    menuInput = input("Pick a Menu Option: ")
    menuInput = int(menuInput)
    if(menuInput == 1):
        s.printQueue()
    if(menuInput == 2):
        pushVal = input("What value would you like to Enqueue?: ")
        s.enqueue(pushVal)
    if(menuInput == 3):
        s.dequeue()
    if(menuInput == 5):
        print("Exiting...")
        end = 1
    if(menuInput == 4):
        print("Top Value: " + s.peek())
