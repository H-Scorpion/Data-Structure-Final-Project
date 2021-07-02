import matplotlib.pyplot as plt

def initialize():
    with open('runtimeList3.txt','r') as f:
        runtimeData = f.readlines()
    studentNum=[]
    runtime=[]
    for data in runtimeData:
        data = data.split(' ')
        studentNum.append(int(data[0]))
        runtime.append(float(data[1]))
    return studentNum,runtime
studentNum,runtime=initialize()
plt.plot(studentNum,runtime)
plt.xlabel("studentNum")
plt.ylabel("runtime")
plt.title("schoolNum=200,choice=5")
plt.show()