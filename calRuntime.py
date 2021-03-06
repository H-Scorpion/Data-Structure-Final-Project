import time
from generateData import genData
from main import *

fileName='runtimeHeap.txt'
if __name__=='__main__':
    with open('./outputData/runtimeData/'+fileName,'w') as f:
        f.truncate()

    for studentNum in range(10,100000,1000):
        data=genData(200,studentNum,5)
        match=initialize(data)
        print(studentNum)
        t1=time.time()
        match.start_match()
        t2=time.time()
        with open('./outputData/runtimeData/'+fileName,'a') as f:
            f.writelines(str(studentNum)+' '+str(t2-t1)+'\n')
    print("complete")