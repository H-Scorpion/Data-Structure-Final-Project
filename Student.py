class Student():
    def __init__(self,studentName,score,choiceList):
        self.name=studentName
        self.score=score
        self.choice=choiceList
    def __str__(self):
        return str(self.name)


