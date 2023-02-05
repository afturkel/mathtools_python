import numpy as np
from functools import reduce


def operationinput(numinp):
    result = []
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    x = ""
    for i in numinp:
        if i in nums:
            x += i
        else:
            result.append(list(x))
            x = ""
    result.append(list(x))
    new_list = [list(map(int, lst)) for lst in result]
    single_list = reduce(lambda x,y: x+y, new_list)
    print(single_list)


    #res = [eval(i) for i in result]
    #print(res)
def addition():
    operationinput(input())
    print(sum(single_list))

def division():
    lst = "".join([i if i in [str(e) for e in range(11)]else " " for i in input()]).split(" ")
    res = [eval(i) for i in lst]
    print(sum(res))