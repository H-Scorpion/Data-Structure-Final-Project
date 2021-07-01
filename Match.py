from AcceptedStudentHeap import AcceptedStudentHeap
class Match():
    def __init__(self):
        self.studentQueue = []
        self.schoolList = {}
        # A list dealing with student without school
        self.failedStudent=[]

    def finish(self):
        #結束條件：申請序列學生數為0 or 申請序列中的學生都沒志願了
        if len(self.studentQueue) == 0:
            return 1
        else:
            for i in self.studentQueue:
                if len(i.choice) != 0:
                    return 0
            # As long as not all of the students run out of their choices
            # the matching continues
            # This results in the problem that we could run into the student
            # in matching with no choice
            # We'll fix it in start_match
            self.failedStudent+=self.studentQueue
            return 1

    def start_match(self):
        while self.finish() != 1:
            #抓出申請序列第一個學生以及他的第一志願
            student_now = self.studentQueue.pop(0)
            try:
                first_choice = self.schoolList[student_now.choice.pop(0)]
                student_now.weightedscore = first_choice.find_weighted(student_now)
            except:
                self.failedStudent.append(student_now)
                continue
            #若學校招生沒滿，直接錄取
            if first_choice.accept.size < first_choice.quota:
                first_choice.accept.insert(student_now)
            #若學校招生滿了，和目前錄取最低分作比較
            else:
                lowest_student = first_choice.accept.peek()
                #若申請者分數比原本的最低分高則錄取，並將原本最低分放回申請序列
                if student_now.weightedscore > lowest_student.weightedscore:
                    #若先前有同分超額則一次剔除
                    while first_choice.extraquota >= 0:
                        extreaquotaStudent=first_choice.accept.removeMin()
                        self.studentQueue.append(extreaquotaStudent)
                        first_choice.extraquota -= 1
                        first_choice.quota -= 1
                    first_choice.accept.insert(student_now)
                #加權分相同則看超額比序
                elif student_now.weightedscore == lowest_student.weightedscore:
                    if first_choice.find_overquota(lowest_student,student_now) == 1:
                        first_choice.accept.removeMin()
                        first_choice.accept.insert(student_now)
                        self.studentQueue.append(lowest_student)
                    elif first_choice.find_overquota(lowest_student,student_now) == 2:
                        first_choice.quota += 1
                        first_choice.extraquota += 1
                        first_choice.accept.insert(student_now)
                        print('overquotq occured at college',end = ' ')
                        print(first_choice)
                    else:
                        self.studentQueue.append(student_now)
                else:
                    self.studentQueue.append(student_now)



