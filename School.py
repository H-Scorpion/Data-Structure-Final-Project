from AcceptedStudentHeap import AcceptedStudentHeap
from AcceptedStudentList import AcceptedStudentList
class School():
    def __init__(self,schoolName,quota,weighted,overquota):
        self.name = schoolName
        self.quota = quota
        self.accept = AcceptedStudentHeap()
        self.weighted = weighted
        self.overquota = overquota  #超額比序項目
        self.extraquota = 0         #超額的人數
    def __str__(self):
        return str(self.name)
    def find_weighted(self,student):
        weighted_score = 0
        for i in range(len(self.weighted)):
            weighted_score += self.weighted[i]*student.score[i]
        return weighted_score
    #回傳 (0,1,2) 代表 (student_1 贏了,student_1 輸了,完全同分)
    def find_overquota(self,student_1,student_2):
        i = 0
        #完全同分則增額錄取
        # I don't quite understand what this means
        if student_1.score == student_2.score:
            return 2
        while i <= 4:
            subject = self.overquota[i]
            # run for each subject
            # if studentLow < studentNow then kick studentLow out
            if student_1.score[subject] < student_2.score[subject]:
                return 1
                # return 1 means studentNow wins
        return 0