#itertoolsがどんなもんか調べるためのファイル
import itertools
import time

START = time.time()
list_return = list(itertools.combinations("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMN",20))
#print(list_return)
print(time.time()-START)