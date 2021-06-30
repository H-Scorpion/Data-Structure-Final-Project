from AcceptedStudentHeap import AcceptedStudentHeap
class School():
    def __init__(self,schoolName,quota,weighted,overquota):
        self.name = schoolName
        self.quota = quota
        self.accept = AcceptedStudentHeap()
        self.weighted = weighted
        self.overquota = overquota
    def __str__(self):
        return str(self.name)
    def find_weighted(self,student):
        weighted_score = 0
        for i in range(len(self.weighted)):
            weighted_score += self.weighted[i]*student.score[i]
        return weighted_score
    #回傳 1 代表 student_1 超額比序輸了
    def find_overquota(self,student_1,student_2):
        i = 0
        while i <= 4:
            subject = self.overquota[i]
            if student_1.score[subject] < student_1.score[subject]:
                return 1
        return 0