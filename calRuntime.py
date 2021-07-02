import time
from generateData import genData
from main import *

fileName='runtimeList3.txt'
if __name__=='__main__':
    with open(fileName,'w') as f:
        f.truncate()

    for studentNum in range(1000,100000,1000):
        data=genData(200,studentNum,5)
        match=initialize(data)
        print(studentNum)
        t1=time.time()
        match.start_match()
        t2=time.time()
        with open(fileName,'a') as f:
            f.writelines(str(studentNum)+' '+str(t2-t1)+'\n')
    print("complete")