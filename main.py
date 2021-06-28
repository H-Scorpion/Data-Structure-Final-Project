from Match import Match
from School import School   
from Student import Student

schoolList=["A","B","C","D"]
acceptQuota=[1, 1, 1, 1]

studentList=[1,2,3,4]
score=[100 ,95, 83, 90 ]
choice=[["A","B","C"],["A","B","C"],["A","B","C"],["A","B","C"]]


if __name__=="__main__":
    # Initialize
    # Put all the school and student data in to the class Match
    match = Match()
    assert len(schoolList)==len(acceptQuota)
    assert len(studentList)==len(score)
    assert len(studentList)==len(choice)
    for i in range(len(schoolList)):
        match.schoolList[schoolList[i]] = School(schoolList[i],acceptQuota[i])
    for i in range(len(studentList)):
        match.studentQueue.append(Student(studentList[i],score[i],choice[i]))
    match.start_match()
    #列印榜單
    for i in match.schoolList.keys():
        print('college',i,end = '\t')
        print('students',end = ' ')
        for j in match.schoolList[i].accept.array:
            print(j,end = ' ')
        print('')


    

    