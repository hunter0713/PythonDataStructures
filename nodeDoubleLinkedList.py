#@author: Hunter Cobb, University of Kansas , @file: nodeDoubleLinkedList.py , @date: 1/22/20, @brief: Node Based Doubly Linked list
#class. Is composed of nodes connecting to one another.
##########Node Class###############################################

class Node:
    def __init__(self, value):
        self.value = value
        self.m_next = None
        self.m_before = None

    def getValue(self):
        return self.value

    def getNext(self):
        return self.m_next

    def setValue(self,newVal):
        self.value = newVal

    def setNext(self,newNext):
        self.m_next = newNext

    def setBefore(self,newBefore):
        self.m_before = newBefore

############Stack Class#############################################
class DoubleLinked:
    def __init__(self):
        self.m_front = Node(None)

    def insert(self,value):
        if(self.m_front.getValue() == None):
            self.m_front.setValue(value)
        else:
            tempo = self.m_front
            newNode = Node(value)
            while(tempo.getNext() != None):
                tempo = tempo.getNext()
            tempo.setNext(newNode)
            temp2 = tempo
            tempo = tempo.getNext()
            tempo.setBefore(temp2)
    def printList(self):
        temp = self.m_front
        while(temp != None):
            print(temp.getValue())
            temp = temp.getNext()

    def delete(self,value):
        tempo = self.m_front

        if(self.m_front.getValue() == value and self.m_front.getNext() != None): #delete used when the first element is to be deleted
            self.m_front = self.m_front.getNext()                               #but is not the only element in the list
            self.m_front.setBefore(None)
        else:
            if(self.m_front.getNext() != None): #delete used when the value is between two other values
                while(tempo.getNext().getValue() != value):
                    tempo = tempo.getNext()
                if(tempo.getNext().getNext() != None):
                    tempor = tempo
                    tempor = tempor.getNext()
                    temp1 = tempor
                    tempor = tempor.getNext()
                    del temp1
                    tempo.setNext(tempor)
                    tempor.setBefore(tempo)
                if(tempo.getNext().getNext() == None): #delete used when the value is the last element of the list
                    tempor = tempo.getNext()
                    tempo.setNext(None)
                    del tempor
            else:
                self.m_front = Node(None) #delete used when the value is the first and only Node
###########Menu Code###################################################
end = 0
print("Welcome to my Doubly Linked List simulator!")
s = DoubleLinked()
while(end == 0):
    print("\n1.)Print Queue \n" + "2.)Insert Value\n" + "3.)Delete value \n" + "4.)Peek Front Value\n" + "5.)Exit\n")
    menuInput = input("Pick a Menu Option: ")
    menuInput = int(menuInput)
    if(menuInput == 1):
        s.printList()
    if(menuInput == 2):
        pushVal = input("What value would you like to Insert?: ")
        s.insert(pushVal)
    if(menuInput == 3):
        pushVal = input("What value would you like to Delete?: ")
        s.delete(pushVal)
    if(menuInput == 5):
        print("Exiting...")
        end = 1
    if(menuInput == 4):
        pass
