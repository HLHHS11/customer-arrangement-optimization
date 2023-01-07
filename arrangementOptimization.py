
import numpy as np
import random   #新しく追加した行

chair = np.zeros((12,18))

for j in range(6):
    for i in range(4):
        chair[1+3*i,1+3*j] = 3
        chair[3*i,3*j] = 2
        chair[3*i,2+3*j] = 2
        chair[2+3*i,2+3*j] = 2
        chair[2+3*i,3*j] = 2

MAX_NUMBER_OF_1 = 30    #ここから下を追加
#countNumberOf1 = 0     #この行は消しちゃってOK
positionOfZeroList = []
for k in range(12):
    for l in range(18):
        if chair[k,l] == 0:
            positionOfZeroList.append([k,l])

random.shuffle(positionOfZeroList)
for m in range(MAX_NUMBER_OF_1):
    (row, column) = positionOfZeroList[m]
    chair[row, column] = 1
    
print(chair)