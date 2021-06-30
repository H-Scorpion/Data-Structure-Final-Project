import math
class AcceptedStudentHeap: #Please store and implement MinHeap data structure with an array
    def __init__(self):
        self.array = []
        self.size = 0
    def __str__(self):
        return str(self.array)
    def getSize(self):
        return self.size
    def getParentIndex(self,index):
        if index==0:
            print("root doesn't has parent")
            return -1
        else:
            return math.ceil((index-2)/2)
    def getLeftChildIndex(self,index):
        try:
            return 2*index+1
        except:
            print("has no left child")
            return -1
    def getRightChildIndex(self,index):
        try:
            return 2*index+2
        except:
            print("has no right child")
            return -1
    def hasParent(self,index):
        if index==0:return 0            
        else:return 1
    def hasLeftChild(self,index):
        if 2*index+1>len(self.array)-1:return 0
        else: return 1
    def hasRightChild(self,index):
        if 2*index+2>len(self.array)-1:return 0
        else:return 1
    
    def insert(self, item): #insert new item
        self.array.append(item)
        index = len(self.array)-1
        #比較學生的分數
        while((index != 0) and item.weightedscore < self.array[self.getParentIndex(index)].weightedscore):
            self.array[index],self.array[self.getParentIndex(index)] = self.array[self.getParentIndex(index)],self.array[index]
            index = self.getParentIndex(index)
        self.size = len(self.array)
    def peek(self):  #Find Minimum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMin(self):
        if len(self.array) == 1:
            return self.array.pop()
        else:
            item = self.array.pop() #get the last element of the heap
            old_first = self.array[0] #get the first element of the heap,i.e., originally the smallest value
            self.array[0] = item
            index = 0
            while(self.hasLeftChild(index)):
                smallerIndex = self.getLeftChildIndex(index)
                if self.hasRightChild(index): #wish to find the smaller one in the child
                    # We should compare the student's scores instead of student themselves
                    if self.array[self.getRightChildIndex(index)].weightedscore < self.array[self.getLeftChildIndex(index)].weightedscore:
                        smallerIndex=self.getRightChildIndex(index)
                #Same, compare the student's scores
                if item.weightedscore < self.array[smallerIndex].weightedscore:
                    break
                else:
                    self.array[index],self.array[smallerIndex] = self.array[smallerIndex],self.array[index]
                    index = smallerIndex
            self.size = len(self.array)
            #改為要回傳原本的min
            return old_first

    def showMinHeap(self):  #Show MinHeap with array
        return self.array
