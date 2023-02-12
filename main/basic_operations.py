from before_operation_process import *

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