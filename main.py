import json
import argparse
import time
from Match import Match
from School import School   
from Student import Student

def parseArg():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='input_1.json')
    args = parser.parse_args()
    return args

def readData():
    with open(args.input,'r') as f:
        data=json.load(f)

    assert len(data['schoolList'])==len(data['acceptQuota'])        
    assert len(data['schoolList'])==len(data['schoolweighted'])
    assert len(data['schoolList'])==len(data['overquota'])
    assert len(data['studentList'])==len(data['score'])
    assert len(data['studentList'])==len(data['choice'])
    return data

def initialize(data):
    # Initialize
    # Put all the school and student data into the class Match
    schoolList=data['schoolList']
    acceptQuota=data['acceptQuota']
    schoolweighted=data['schoolweighted']
    overquota = data['overquota']
    studentList=data['studentList']
    score=data['score']
    choice=data['choice']

    match = Match()

    for i in range(len(schoolList)):
        match.schoolList[schoolList[i]] = School(schoolList[i],acceptQuota[i],schoolweighted[i],overquota[i])
        #print(schoolList[i],acceptQuota[i],schoolweighted[i],overquota[i])
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
    print('students without school:')
    for i in match.failedStudent:
        print(i,end = ' ')
    print('\n',end = '')

def outputResult(match):
    with open("output_1.txt", "w") as output:
        for i in match.schoolList.keys():
            output.write('college'+i+'\t')
            output.write('students ')
            for j in match.schoolList[i].accept.array:
                output.write(str(j)+' ')
            output.write('\n')
        output.write('students without school:')
        for i in match.failedStudent:
            output.write(str(i)+' ')
        output.write('\n')

if __name__=="__main__":

    args = parseArg()
    match=initialize(readData())

    t1=time.time()
    match.start_match()
    t2=time.time()

    printResult(match)
    outputResult(match)

    print("runtime:",t2-t1)



    

    