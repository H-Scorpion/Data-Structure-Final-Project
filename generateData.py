import random
import json

schoolNum=5
studentNum=20
choiceNum=5

schoolList=[str(i) for i in range(1,schoolNum+1)]
acceptQuota=[random.randint(1,studentNum*.3) for _ in range(schoolNum)]
# acceptQuota=[1 for _ in range(schoolNum)]

studentList=[str(i) for i in range(1,studentNum+1)]
score=random.sample(range(100), studentNum) #分數不重複
choice=[random.sample(schoolList,choiceNum) for _ in range(studentNum)]

print(schoolList)
print(acceptQuota)
print(studentList)
print(score)
print(choice)

data={
    'schoolList':schoolList,
    'acceptQuota':acceptQuota,
    'studentList':studentList,
    'score':score,
    'choice':choice
}
ret=json.dumps(data)
with open('input_2.json','w') as f:
    f.write(ret)