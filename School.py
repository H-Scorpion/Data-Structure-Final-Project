from AcceptedStudentHeap import AcceptedStudentHeap
class School():
    def __init__(self,schoolName,quota):
        self.name = schoolName
        self.quota = quota
        self.accept = AcceptedStudentHeap()
    def __str__(self):
        return str(self.name)