import json
from Match import Match
from School import School   
from Student import Student

with open("input_2.json",'r') as f:
    data=json.load(f)
    schoolList=data['schoolList']
    acceptQuota=data['acceptQuota']

    studentList=data['studentList']
    score=data['score']
    choice=data['choice']



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


    

    