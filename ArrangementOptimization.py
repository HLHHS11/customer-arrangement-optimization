import numpy as np
import time


def generate_arrangement_array():
    '''カフェ店内の座席・卓の"大きな配置図"を生成'''
    arrangement = np.zeros((6,11))
    for i in range(2):
        for j in range(3): 
            arrangement[3*i,3*j] = 2
            arrangement[3*i,2+3*j] = 2
            arrangement[1+3*i,1+3*j] = 3
            arrangement[2+3*i,2+3*j] = 2
            arrangement[2+3*i,3*j] = 2
        arrangement[3*i,9] = 2 
        arrangement[3*i+1,9] = 2  
        arrangement[2+3*i,9] = 2 
        arrangement[1+3*i,10] = 3 
    return arrangement


def generate_seat_position_array():
    '''全体の（大きな）配置図における座席の場所を取り出した"小さな配置図"を生成'''
    seat_position = np.empty((28,2))   
    counter = 0
    for i in range(2):
        for j in range(3): 
            seat_position[counter] = [3*i,1+3*j]
            counter += 1
            seat_position[counter] = [1+3*i,3*j]
            counter += 1
            seat_position[counter] = [1+3*i,2+3*j]
            counter += 1
            seat_position[counter] = [2+3*i,1+3*j]
            counter += 1
        seat_position[counter] = [3*i,10]
        counter += 1
        seat_position[counter] = [2+3*i,10] 
        counter += 1
    return seat_position


def generate_combination_list(n,r,i=0):
    if r>n/2:
        r = n-r
    if r==0:
        return []
    elif r==1:
        combination = []
        for j in range(i+1,n-r+2):
            combination.append([j])
        return combination
    else:
        combination = []
        for j in range(i+1,n-r+2):
            temp_combination = generate_combination_list(n,r-1,j)
            for k in range(len(temp_combination)):
                #temp_combination[k].insert(0,j)
                temp_combination[k].append(j)
            combination += temp_combination
        return combination


# ----プログラム開始----
START_TIME = time.time()    # 開始時刻を記録
seat_position = generate_seat_position_array()  # 座席の場所を示す「小さな配置図」

# ----組み合わせの配列を格納した配列（2次元配列）を生成----
n = 28
r = 14   
combination_list = generate_combination_list(n,r)

# ----不快度の一覧の配列と、補助の変数を用意----
ratio_array = np.empty(len(combination_list))   # 不快度の一覧の配列
index_of_ratio_array = 0    # 上のratio_arrayのインデックス（最後に代入するときに必要）

# ----各コンビネーションに対してループを回し、不快度を求める----
for each_combination in combination_list:
    # --コンビネーションに対応する着座表を作成--
    sat_seat_position = np.empty([r,2]) # 「小さな配置図」の中から「人が座る席」だけ選ぶ
    counter = 0
    for value in each_combination:
        sat_seat_position[counter] = np.array(seat_position[value-1])
        counter += 1
    # --不快度の計算の下準備--
    # --各行・各列に着席している人数を配列に--
    SIZE_ROW = 6
    SIZE_COLUMN = 11
    total_people_row = np.zeros(SIZE_ROW)     # 各行にいる人の数の配列
    total_people_column = np.zeros(SIZE_COLUMN)   # 各列にいる人の数の配列
    for position in sat_seat_position: 
        total_people_row[int(position[0])] += 1
        total_people_column[int(position[1])] += 1
    # --視界の広さ および 視界に入る人の数の合計を計算--
    sum_eyesight = 0   # 視界の広さの合計
    sum_counted_people = 0   # 視界に入る人の数の合計
    for i in range(2):  # 3*i"行"目に着目。3*i行目の人は下側を向いている
        eyesight = SIZE_COLUMN * (SIZE_ROW-1-3*i)
        sum_eyesight += eyesight * total_people_row[3*i]    # 人数分のeyesightを足す
        for j in range(3*i+1, SIZE_ROW):    # 3*i"行"目より下側の人数
            sum_counted_people += total_people_row[j] * total_people_row[3*i]   # 人数分のcounted_peopleを足す
    for i in range(2):  # 3*i+2"行"目に着目
        eyesight = SIZE_COLUMN * (3*i+2)
        sum_eyesight += eyesight * total_people_row[3*i+2] 
        for j in range(0, 3*i+2): 
            sum_counted_people += total_people_row[j] * total_people_row[3*i+2]
    for i in range(2):  # 3*i"列"目に着目。3*i列目の人は右側を向いている
        eyesight = SIZE_ROW * (SIZE_COLUMN-1-3*i)
        sum_eyesight += eyesight * total_people_column[3*i]
        for j in range(3*i+1, SIZE_COLUMN):
            sum_counted_people += total_people_column[j] * total_people_column[3*i]
    for i in range(2):  # 3*i+2"列"目に着目
        eyesight = SIZE_ROW * (3*i+2)
        sum_eyesight += eyesight * total_people_column[3*i+2]
        for j in range(0, 3*i+2):
            sum_counted_people += total_people_column[j] * total_people_column[3*i+2]
    # --ループの外で用意した不快度の配列に、補助変数を用いて代入--
    ratio_array[index_of_ratio_array] = sum_counted_people / sum_eyesight    
    index_of_ratio_array += 1

# ----最適解に対応する座席表を作成する----
# ----不快度が最小（・最大）となったときのratio_arrayのインデックスを取得----
min_index = ratio_array.argmin()
max_index = ratio_array.argmax()

# ----不快度が最小のときの「大きな座席図」を作成----
min_seat_position = np.empty([r,2])
counter = 0
for value in combination_list[min_index]:   # 「人が座る席」の表を作成するためのループ
    min_seat_position[counter] = np.array(seat_position[value-1])
    counter += 1
ARRANGEMENT = generate_arrangement_array()  #　大きな座席表を作成
min_arrangement = ARRANGEMENT.copy()    # 「大きな配置図」の初期化
for array in min_seat_position:
    min_arrangement[int(array[0]),int(array[1])] = 1

# ----不快度が最大のときの「大きな座席図」を作成（上と同様）----
max_seat_position = np.empty([r,2])
counter = 0
for value in combination_list[max_index]: 
    max_seat_position[counter] = np.array(seat_position[value])
    counter += 1
ARRANGEMENT = generate_arrangement_array() 
max_arrangement = ARRANGEMENT.copy()   
for array in max_seat_position:
    max_arrangement[int(array[0]),int(array[1])] = 1

# ----結果の出力----
print(f'検討した配置図 : {len(combination_list)}通り')
print(f'不快度の最小値 : {ratio_array[min_index]}')
print(f'不快度最小の座席図\n{min_arrangement}')
print(f'不快度の最大値 : {ratio_array[max_index]}')
print(f'不快度最大の座席図\n{max_arrangement}')
print(f"処理時間 : {time.time()-START_TIME} s")