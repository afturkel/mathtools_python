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