import random
import json
import argparse


def genData(schoolNum,studentNum,choiceNum):
    schoolList = [str(i) for i in range(1,schoolNum+1)]
    acceptQuota = [random.randint(1,studentNum*.3) for _ in range(schoolNum)]
    #5科加權比重
    schoolweighted = [[random.randint(0,3) for i in range(5)] for _ in range(schoolNum)]
    # acceptQuota=[1 for _ in range(schoolNum)]

    studentList = [str(i) for i in range(1,studentNum+1)]
    score = [[random.randint(0,100) for i in range(5)] for j in range(1,studentNum+1)]
    choice = [random.sample(schoolList,choiceNum) for _ in range(studentNum)]
    
    data={
        'schoolList':schoolList,
        'acceptQuota':acceptQuota,
        'schoolweighted':schoolweighted,
        'studentList':studentList,
        'score':score,
        'choice':choice
    }

    return data


def printData(data):
    schoolList,acceptQuota,schoolweighted=data['schoolList'],data['acceptQuota'],data['schoolweighted']
    studentList,score,choice=data['studentList'],data['score'],data['choice']
    print('school'+'\t'+'Quota'+'\t'+'weighted')
    for i in range(len(schoolList)):
        print(schoolList[i],end = '\t')
        print(acceptQuota[i],end = '\t')
        print(schoolweighted[i])
    print('student'+'\t'+'score'+'\t'+'choice')
    for i in range(len(studentList)):
        print(studentList[i],end = '\t')
        print(score[i],end = '\t')
        print(choice[i])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--schoolNum', default=5)
    parser.add_argument('--studentNum', default=20)
    parser.add_argument('--choiceNum', default=5)

    args = parser.parse_args()

    data = genData(int(args.schoolNum),int(args.studentNum),int(args.choiceNum))

    ret=json.dumps(data)
    with open('input_2.json','w') as f:
        f.write(ret)