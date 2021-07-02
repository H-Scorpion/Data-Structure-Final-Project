import matplotlib.pyplot as plt

def initialize(file):
    with open(file,'r') as f:
        runtimeData = f.readlines()
    studentNum=[]
    runtime=[]
    for data in runtimeData:
        data = data.split(' ')
        studentNum.append(int(data[0]))
        runtime.append(float(data[1]))
    return studentNum,runtime
studentNum_1,runtime_1=initialize('runtimeHeap1.txt')
studentNum_2,runtime_2=initialize('runtimeList3.txt')
data1, = plt.plot(studentNum_1,runtime_1,label='using Heap')
data2, = plt.plot(studentNum_2,runtime_2,label='using List')
plt.xlabel("studentNum")
plt.ylabel("runtime")
plt.title("schoolNum=200,choice=5")
plt.legend(handles=[data1,data2])
plt.show()