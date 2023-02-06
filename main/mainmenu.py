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
    concat_res = [''.join(sub_list) for sub_list in result]
    int_res = [int(i) if i.isdigit() else i for i in concat_res]
    
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

