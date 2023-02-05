import numpy as np

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
    #new_list = [list(map(int, lst)) for lst in result]
    print(result)

    #res = [eval(i) for i in result]
    #print(res)
def addition():
    lst = "".join([i if i in [str(e) for e in range(11)]else " " for i in input()]).split(" ")
    print(lst)
    res = [eval(i) for i in lst]
    print(sum(res))

def division():
    lst = "".join([i if i in [str(e) for e in range(11)]else " " for i in input()]).split(" ")
    res = [eval(i) for i in lst]
    print(sum(res))

operationinput(input())

"""
o sublistlerdeki rakamlari birlestirip birbiriyle operasyon et
bunlari fonksiyonlara ayirip fazla kod kullanmaktan kaçin
"""