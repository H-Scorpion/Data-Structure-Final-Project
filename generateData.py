import random
import json

schoolNum=5
studentNum=20
choiceNum=5

schoolList = [str(i) for i in range(1,schoolNum+1)]
acceptQuota = [random.randint(1,studentNum*.3) for _ in range(schoolNum)]
#5科加權比重
schoolweighted = [[str(random.randint(0,3)) for i in range(5)] for _ in range(schoolNum)]
# acceptQuota=[1 for _ in range(schoolNum)]

studentList = [str(i) for i in range(1,studentNum+1)]
score = random.sample(range(100), studentNum) #分數不重複
choice = [random.sample(schoolList,choiceNum) for _ in range(studentNum)]

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

data={
    'schoolList':schoolList,
    'acceptQuota':acceptQuota,
    'schoolweighted':schoolweighted,
    'studentList':studentList,
    'score':score,
    'choice':choice
}
ret=json.dumps(data)
with open('input_2.json','w') as f:
    f.write(ret)