from AcceptedStudentHeap import AcceptedStudentHeap
class School():
    def __init__(self,schoolName,quota,weighted):
        self.name = schoolName
        self.quota = quota
        self.accept = AcceptedStudentHeap()
        self.weighted = weighted
    def __str__(self):
        return str(self.name)