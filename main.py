import json
import argparse
import time
from Match import Match
from School import School   
from Student import Student

def parseArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_2.json')
    args = parser.parse_args()
    return args

def readData():
    with open(args.input,'r') as f:
        data=json.load(f)

    assert len(data['schoolList'])==len(data['acceptQuota'])        
    assert len(data['schoolList'])==len(data['schoolweighted'])
    assert len(data['studentList'])==len(data['score'])
    assert len(data['studentList'])==len(data['choice'])
    return data

def initialize(data):
    # Initialize
    # Put all the school and student data into the class Match
    schoolList=data['schoolList']
    acceptQuota=data['acceptQuota']
    schoolweighted=data['schoolweighted']
    studentList=data['studentList']
    score=data['score']
    choice=data['choice']

    match = Match()

    for i in range(len(schoolList)):
        match.schoolList[schoolList[i]] = School(schoolList[i],acceptQuota[i],schoolweighted[i])
    for i in range(len(studentList)):
        match.studentQueue.append(Student(studentList[i],score[i],choice[i]))
    return match

def printResult(match):
    #列印榜單
    for i in match.schoolList.keys():
        print('college',i,end = '\t')
        print('students',end = ' ')
        for j in match.schoolList[i].accept.array:
            print(j,end = ' ')
        print('')

if __name__=="__main__":

    args = parseArg()
    schoolList,acceptQuota,schoolweighted,studentList,score,choice=readData()
    match=initialize(readData())

    t1=time.time()
    match.start_match()
    t2=time.time()

    printResult(match)    

    print("runtime:",t2-t1)



    

    