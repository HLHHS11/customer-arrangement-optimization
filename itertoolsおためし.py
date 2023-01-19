# itertoolsがどんなもんか調べるためのファイル
# itertools.combinations()では文字列で組み合わせを作るので
# 引数に"0123456789101112"...とやっても上手く動かない
# そこで一旦abc...で組み合わせを生成してもらってから、
# それをイテレータの数値に変換する
# 230119現在、VSCodeでは29行目に赤線が出てるけど問題なく動く


import itertools
import time

START = time.time()
list_return = list(itertools.combinations("abcdefghijklmnopqrstuvwxyzAB",14))
#print(list_return)
convert_dic = {
    "a": 0, "b": 1, "c": 2, "d": 3, "e": 4,
    "f": 5, "g": 6, "h": 7, "i": 8, "j": 9,
    "k": 10, "l": 11, "m": 12, "n": 13, "o": 14,
    "p": 15, "q": 16, "r": 17, "s": 18, "t": 19,
    "u": 20, "v": 21, "w": 22, "x": 23, "y": 24,
    "z": 25, "A": 26, "B": 27
}
combination_list = []
for each_combination in list_return:
    each_combination = list(each_combination)
    counter = 0
    for item in each_combination:
        #print(f"each combination:{each_combination}")
        each_combination[counter] = convert_dic[item]
        counter += 1
    combination_list.append(each_combination)
#print(list_return)
print(combination_list)
print(time.time()-START)