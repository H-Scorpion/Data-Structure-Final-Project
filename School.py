from AcceptedStudentHeap import AcceptedStudentHeap
class School():
    def __init__(self,schoolName,quota,weighted):
        self.name = schoolName
        self.quota = quota
        self.accept = AcceptedStudentHeap()
        self.weighted = weighted
    def __str__(self):
        return str(self.name)
    def find_weighted(self,student):
        weighted_score = 0
        for i in range(len(self.weighted)):
            weighted_score += self.weighted[i]*student.score[i]
        return weighted_score