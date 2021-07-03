class AcceptedStudentList:
    def __init__(self):
        #從小排到大
        self.array = []
        self.size = 0
    def insert(self,item):
        self.array.append(item)
        index = len(self.array)-1
        #比較學生的分數
        while (index > 0) and(item.weightedscore < self.array[index - 1].weightedscore):
            self.array[index],self.array[index - 1] = self.array[index - 1],self.array[index]
            index -= 1
        self.size = len(self.array)
    def peek(self):  #Find Minimum item
        if self.size == 0:
            return
        else:
            return self.array[0]
    def removeMin(self):
        if self.size > 0:
            self.size -= 1
            return self.array.pop(0)
        else:
            return