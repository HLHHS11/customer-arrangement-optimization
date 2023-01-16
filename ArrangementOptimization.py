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

# 組み合わせの配列を格納した配列（2次元配列）を生成
n = 20   #6→28
r = 10   #3→10
combination_list = generate_combination_list(n,r)
arrangement_list = []
iterator_for_combination_list = 0   #!!最終的には、下のループをitems()メソッドを使って書き直したい。一旦混乱を防ぐためこのまま
ratio_array = np.empty(len(combination_list))
for each_combination in combination_list:   #each_combinationの例[1,3,5,6,7,10]
    # 各組み合わせに対応する着座表を作成
    sat_seat_position = np.empty([r,2])
    counter = 0
    for iterator in each_combination:
        sat_seat_position[counter] = np.array(seat_position[iterator-1])
        counter += 1
    # 不快度の計算の下準備
    # 各行・各列に着席している人数を配列に
    SIZE_ROW = 6
    SIZE_COLUMN = 8 #8→11
    total_people_row = np.zeros(SIZE_ROW)     # 各行にいる人の数の配列
    total_people_column = np.zeros(SIZE_COLUMN)   # 各列にいる人の数の配列
    for position in sat_seat_position:  #positionは、サイズ2のndarray(のはず)
        total_people_row[int(position[0])] += 1
        total_people_column[int(position[1])] += 1
    #視界の広さの合計および視界に入る人の数の合計を計算
    sum_eyesight = 0   # 視界の広さの合計
    sum_counted_people = 0   # 視界に入る人の数の合計
    #for i in range(2):  #3*i行目に着目 
    #    eyesight = SIZE_COLUMN * (SIZE_ROW-1-3*i)
    #    sum_eyesight += eyesight * total_people_row[3*i]    #人数分のeyesightを足す
    #    for j in range(3*i+1, SIZE_ROW):    #3*i行目より下側の人数
    #        sum_counted_people += total_people_row[j] * total_people_row[3*i]   #人数分のcounted_peopleを足す
    #for i in range(2):  #3*i+2行目に着目。理論上上のループと合わせることができる
    #    eyesight = SIZE_COLUMN * (3*i+2)
    #    sum_eyesight += eyesight * total_people_row[3*i+2] 
    #    for j in range(0, 3*i+2):   #3*i+2行目より上側の人数
    #        sum_counted_people += total_people_row[j] * total_people_row[3*i+2]
    for i in range(2):  #高速化のため、3*i行目と3*i+2行目をまとめて計算
        sum_eyesight += (SIZE_COLUMN*(SIZE_ROW-1-3*i))*total_people_row[3*i] + (SIZE_COLUMN*(3*i+2))*total_people_row[3*i+2]
        for j in range(3*i+1, SIZE_ROW):    #3*i行目より下側の人数
            sum_counted_people += total_people_row[j] * total_people_row[3*i]   #人数分のcounted_peopleを足す
        for j in range(0, 3*i+2):   #3*i+2行目より上側の人数
            sum_counted_people += total_people_row[j] * total_people_row[3*i+2]
    #for i in range(2):  #2→3    3*i列目に着目
    #    eyesight = SIZE_ROW * (SIZE_COLUMN-1-3*i)
    #    sum_eyesight += eyesight * total_people_column[3*i]
    #    for j in range(3*i+1, SIZE_COLUMN):  #2→3    3*i列目より右側の人数
    #        sum_counted_people += total_people_column[j] * total_people_column[3*i]
    #for i in range(2):  #2→3    3*i+2列目に着目
    #    eyesight = SIZE_ROW * (3*i+2)
    #    sum_eyesight += eyesight * total_people_column[3*i+2]
    #    for j in range(0, 3*i+2):
    #        sum_counted_people += total_people_column[j] * total_people_column[3*i+2]
    for i in range(2):  #2→3    3*i列目と3*i+2行目をまとめて計算
        sum_eyesight += (SIZE_ROW*(SIZE_COLUMN-1-3*i))*total_people_column[3*i] + (SIZE_ROW*(3*i+2))*total_people_column[3*i+2]
        for j in range(3*i+1, SIZE_COLUMN):  #2→3    3*i列目より右側の人数
            sum_counted_people += total_people_column[j] * total_people_column[3*i]
        for j in range(0, 3*i+2):
            sum_counted_people += total_people_column[j] * total_people_column[3*i+2]
    ratio_array[iterator_for_combination_list] = sum_counted_people / sum_eyesight    
    iterator_for_combination_list += 1

optimal_index = ratio_array.argmin()
max_index = ratio_array.argmax()
#最適解の組み合わせ
optimal_seat_position = np.empty([r,2]) #!!あやしい
counter = 0
for iterator in combination_list[optimal_index]:   #iteratorの例:3
    optimal_seat_position[counter] = np.array(seat_position[iterator-1])
    #いらない？？copy_arrangement[int(sat_seat_position[0]),int(sat_seat_position[1])] = 1  #おそらくここでのsat_seat_positionの意味は現在の意味と違って一次元配列だ。
    counter += 1
copy_arrangement = ARRANGEMENT.copy()
for array in optimal_seat_position:
    copy_arrangement[int(array[0]),int(array[1])] = 1

print(optimal_index)
print(ratio_array[optimal_index])
#print(ratio_array)
print(len(ratio_array))
print(copy_arrangement)