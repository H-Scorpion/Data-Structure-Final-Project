import random
import json
import argparse


def genData(schoolNum,studentNum,choiceNum,weighted=True):
    schoolList = [str(i) for i in range(1,schoolNum+1)]
    try:
        acceptQuota = [random.randint(1,studentNum*.3) for _ in range(schoolNum)]
    except:
        #When the studentNum*.3 is too small
        acceptQuota = [1 for _ in range(schoolNum)]
    #5科加權比重
    if weighted:
        schoolweighted = [[random.randint(0,3) for i in range(5)] for _ in range(schoolNum)]
    else:
        schoolweighted = [[1 for i in range(5)] for _ in range(schoolNum)]
    #超額比序項目('01234'代表'國英數自社')
    overquota = [random.sample([0,1,2,3,4],5) for _ in range(schoolNum)]

    studentList = [str(i) for i in range(1,studentNum+1)]
    score = [[random.randint(0,100) for i in range(5)] for j in range(1,studentNum+1)]
    choice = [random.sample(schoolList,choiceNum) for _ in range(studentNum)]
    
    data={
        'schoolList':schoolList,
        'acceptQuota':acceptQuota,
        'schoolweighted':schoolweighted,
        'overquota':overquota,
        'studentList':studentList,
        'score':score,
        'choice':choice
    }

    return data


def printData(data):
    schoolList,acceptQuota,schoolweighted=data['schoolList'],data['acceptQuota'],data['schoolweighted']
    overquota = data['overquota']
    studentList,score,choice=data['studentList'],data['score'],data['choice']
    print('school'+'\t'+'Quota'+'\t'+'weighted'+'\t'+'overquota')
    for i in range(len(schoolList)):
        print(schoolList[i],end = '\t')
        print(acceptQuota[i],end = '\t')
        print(schoolweighted[i],end = '\t')
        print(overquota[i])
    print('student'+'\t'+'score'+'\t'+'choice')
    for i in range(len(studentList)):
        print(studentList[i],end = '\t')
        print(score[i],end = '\t')
        print(choice[i])



if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('--schoolNum', default=5)
    parser.add_argument('--studentNum', default=10)
    parser.add_argument('--choiceNum', default=5)
    parser.add_argument('--output', default='input_1.json')
    parser.add_argument('--weighted', default=True)

    args = parser.parse_args()

    data = genData(int(args.schoolNum),int(args.studentNum),int(args.choiceNum),bool(args.weighted))
    printData(data)
    
    ret=json.dumps(data)
    with open(args.output,'w') as f:
        f.write(ret)