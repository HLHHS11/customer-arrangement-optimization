import time


def generate_combination_list(n,r,i=0):
    if r==1:
        combination = []
        for j in range(i+1,n-r+2):
            combination.append([j])
        return combination
    else:
        if r>n/2:
            r = n - r
        combination = []
        for j in range(i+1,n-r+2):
            temp_combination = generate_combination_list(n,r-1,j)
            for k in range(len(temp_combination)):
                temp_combination[k].insert(0,j)
            combination += temp_combination
        return combination
        

start = time.time()
print(generate_combination_list(40,37))
print(time.time()-start)