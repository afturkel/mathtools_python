import numpy as np

def b_operation_process(numinp):
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
    b_operation_process.var = [int(i) if i.isdigit() else i for i in concat_res]
    
def addition(numinp):
    b_operation_process(numinp)
    print(sum(b_operation_process.var))

def subtraction(numinp):
    b_operation_process(numinp)
    valor = b_operation_process.var[0]
    del b_operation_process.var[0]
    subres = valor-sum(b_operation_process.var)
    print(subres)
    
def multiplication(numinp):
    res = 1
    b_operation_process(numinp)
    for x in b_operation_process.var:
        res = res * x
    print(res)