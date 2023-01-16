import random   #たぶんもうrandomの出番はないけど、一応
import numpy as np
import copy


def generate_arrangement_array():
    """カフェ店内の座席の配置表を生成
    注意！：表記は数学の行列の表記と同じように見えるが、
    実際にはlist[][]のように外側から順にインデックスを指定する表記である"""
    arrangement = np.zeros((6,8))  #8→11
    for i in range(2):
        for j in range(2):  #3
            arrangement[3*i,3*j] = 2
            arrangement[3*i,2+3*j] = 2
            arrangement[1+3*i,1+3*j] = 3
            arrangement[2+3*i,2+3*j] = 2
            arrangement[2+3*i,3*j] = 2
        arrangement[3*i,6] = 2  #9
        arrangement[3*i+1,6] = 2    #9
        arrangement[2+3*i,6] = 2    #9
        arrangement[1+3*i,7] = 3   #10
    return arrangement


def generate_seat_position_array():
    seat_position = np.empty((20,2))    #20→28
    counter = 0
    for i in range(2):
        for j in range(2):  #2→3
            seat_position[counter] = [3*i,1+3*j]
            counter += 1
            seat_position[counter] = [1+3*i,3*j]
            counter += 1
            seat_position[counter] = [1+3*i,2+3*j]
            counter += 1
            seat_position[counter] = [2+3*i,1+3*j]
            counter += 1
        seat_position[counter] = [3*i,7] #7→10
        counter += 1
        seat_position[counter] = [2+3*i,7] #7→10
        counter += 1
    return seat_position


def generate_combination_list(n,r,i=0):
    if r>n/2:
        r = n-r
    if r==1:
        combination = []
        for j in range(i+1,n-r+2):
            combination.append([j])
        return combination
    else:
        combination = []
        for j in range(i+1,n-r+2):
            temp_combination = generate_combination_list(n,r-1,j)
            for k in range(len(temp_combination)):
                temp_combination[k].insert(0,j)
            combination += temp_combination
        return combination


ARRANGEMENT = generate_arrangement_array()
seat_position = generate_seat_position_array()
print("変換前の配置図")
print(ARRANGEMENT)
print(seat_position)
#print(arrangement==0) 

# 配置図を作成し、それに対する不快度・空間の広さを求める
# 配置図作るだけ作ったけど、たぶんndarrayのでかいやつを使う必要はない

n = 6   #6→28
r = 3   #3→10
combination_list = generate_combination_list(n,r)
arrangement_list = []
for each_combination in combination_list:   #each_combinationの例[1,3,5,6,7,10]
    # このブロックは、各組み合わせの計算をする場所
    copy_arrangement = ARRANGEMENT.copy()
    sat_seat_position = np.empty([r,2]) #!!あやしい
    counter = 0
    for iterator in each_combination:   #iteratorの例:3
        sat_seat_position[counter] = np.array(seat_position[iterator-1])
        #copy_arrangement[int(sat_seat_position[0]),int(sat_seat_position[1])] = 1  #おそらくここでのsat_seat_positionの意味は現在の意味と違って一次元配列だ。
        counter += 1
    arrangement_list.append(copy_arrangement)
    print(f"sat_seat_position : {sat_seat_position}")
    



