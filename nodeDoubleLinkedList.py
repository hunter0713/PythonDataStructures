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

    def getBefore(self):
        return(self.m_before)

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
        flag = 0
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
                    flag = 1
                    tempo.setNext(tempor)
                    tempor.setBefore(tempo)
                if(tempo.getNext().getNext() == None and flag == 0): #delete used when the value is the last element of the list
                    tempor = tempo.getNext()
                    tempo.setNext(None)
                    del tempor
            else:
                self.m_front = Node(None) #delete used when the value is the first and only Node

    def findSmallest(self): #returns the smallest element of the list
        smallest = self.m_front.getValue()
        temp = self.m_front
        while(temp.getNext() != None):
            temp = temp.getNext()
            if(temp.getValue() < smallest):
                smallest = temp.getValue()
        return(str(smallest))

    def findLargest(self):#returns the largest element of the list
        largest = self.m_front.getValue()
        temp = self.m_front
        while(temp.getNext() != None):
            temp = temp.getNext()
            if(temp.getValue() > largest):
                largest = temp.getValue()
        return(str(largest))

    def findAverage(self):#returns the average of the list numbers
        temp = self.m_front
        count = 1
        avg = self.m_front.getValue()
        while(temp.getNext() != None):
            temp = temp.getNext()
            avg += temp.getValue()
            count += 1
        return(str(avg/count))

    def reverseList(self):
        temp = DoubleLinked()
        temporary = self.m_front
        while(temporary.getNext() != None):
            temporary = temporary.getNext()
        while(temporary != None):
            temp.insert(temporary.getValue())
            temporary = temporary.getBefore()
        self.m_front = temp.m_front



###########Menu Code###################################################
end = 0
print("Welcome to my Doubly Linked List simulator!")
s = DoubleLinked()
while(end == 0):
    print("\n1.)Print List \n" + "2.)Insert Value\n" + "3.)Delete value \n" + "4.)Find Smallest Value\n" + "5.)Find Largest Value\n"+"6.)Find Average\n"+"7.)Reverse List\n"+"8.)Exit\n")
    menuInput = input("Pick a Menu Option: ")
    menuInput = int(menuInput)
    if(menuInput == 1):
        print("\n============\nYour List: ")
        s.printList()
        print("============\n")
    elif(menuInput == 2):
        pushVal = input("What value would you like to Insert?: ")
        s.insert(pushVal)
    elif(menuInput == 3):
        pushVal = input("What value would you like to Delete?: ")
        pushVal = int(pushVal)
        s.delete(pushVal)
    elif(menuInput == 4):
        print("smallest: " + s.findSmallest())
    elif(menuInput == 5):
        print("largest: " + s.findLargest())
    elif(menuInput == 6):
        print("Average: " + s.findAverage())
    elif(menuInput == 7):
        s.reverseList()
    elif(menuInput == 8):
        print("Exiting...")
        end = 1
    else:
        print("Please choose a valid menu option")
