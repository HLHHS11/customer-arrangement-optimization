import random   #たぶんもうrandomの出番はないけど、一応
import numpy as np


def generate_arrangement_array():
    """カフェ店内の座席の配置表を生成
    注意！：表記は数学の行列の表記と同じように見えるが、
    実際にはlist[][]のように外側から順にインデックスを指定する表記である"""
    arrangement = np.zeros((12,18))
    for i in range(4):
        for j in range(6):
            arrangement[3*i,3*j] = 2
            arrangement[3*i,2+3*j] = 2
            arrangement[1+3*i,1+3*j] = 3
            arrangement[2+3*i,2+3*j] = 2
            arrangement[2+3*i,3*j] = 2
    return arrangement


def generate_seat_position_array():
    seat_position = np.empty((96,2))
    counter = 0
    for i in range(4):
        for j in range(6):
            seat_position[counter] = [3*i,1+3*j]
            counter += 1
            seat_position[counter] = [1+3*i,3*j]
            counter += 1
            seat_position[counter] = [1+3*i,2+3*j]
            counter += 1
            seat_position[counter] = [2+3*i,1+3*j]
            counter += 1
    return seat_position


arrangement = generate_arrangement_array()
seat_position = generate_seat_position_array()
print("変換前の配置図")
print(arrangement)
print(seat_position)
#print(arrangement==0) 

#配置図を作成し、それに対する不快度・空間の広さを求める
#for 





"""
#配列arrangementをもとにして座席図を作る方法
#次のコミットで消す
seat_position = []
for k in range(12):
    for l in range(18):
        if arrangement[k,l] == 0:
            seat_position.append([k,l])

#ランダムに0→1置換処理
MAX_NUMBER_OF_1 = 30    #
random.shuffle(seat_position)
for m in range(MAX_NUMBER_OF_1):
    (row, column) = seat_position[m]
    arrangement[row, column] = 1

#print("変換後の配置図")    
#print(arrangement)
"""