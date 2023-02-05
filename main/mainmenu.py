import numpy as np

def addition():
    lst = "".join([i if i in [str(e) for e in range(11)]else " " for i in input()]).split(" ")
    res = [eval(i) for i in lst]
    print(sum(res))

addition()