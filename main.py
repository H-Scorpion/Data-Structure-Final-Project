from Match import Match
from School import School   
from Student import Student

schoolList=["A","B","C","D"]
acceptQuota=[5, 2, 1, 3]

studentList=[1,2,3,4]
score=[100 ,95, 83, 90 ]
choice=[["A","B","C"],["A","C","B"],["A","D","C"],["B","A","D"]]


if __name__=="__main__":
    # Initialize
    # Put all the school and student data in to the class Match
    match = Match()
    assert len(schoolList)==len(acceptQuota)
    assert len(studentList)==len(score)
    assert len(studentList)==len(choice)
    for i in range(len(schoolList)):
        match.schoolList.append(School(schoolList[i],acceptQuota[i]))
    for i in range(len(studentList)):
        match.studentQueue.append(Student(studentList[i],score[i],choice[i]))

    