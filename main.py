import json
import argparse
from Match import Match
from School import School   
from Student import Student





if __name__=="__main__":
    # Initialize
    # Put all the school and student data in to the class Match
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_2.json')

    args = parser.parse_args()

    with open(args.input,'r') as f:
        data=json.load(f)
        schoolList=data['schoolList']
        acceptQuota=data['acceptQuota']
        schoolweighted=data['schoolweighted']
        studentList=data['studentList']
        score=data['score']
        choice=data['choice']


    match = Match()
    assert len(schoolList)==len(acceptQuota)
    assert len(schoolList)==len(schoolweighted)
    assert len(studentList)==len(score)
    assert len(studentList)==len(choice)
    for i in range(len(schoolList)):
        match.schoolList[schoolList[i]] = School(schoolList[i],acceptQuota[i],schoolweighted[i])
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


    

    