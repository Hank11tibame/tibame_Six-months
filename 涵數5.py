#None在Python中獨立成為一個資料型態None Type
def greeting(name):
    """Python函數需傳遞名字name"""
    print("Hi, ", name,"Good Moring !")
    return
ret_value = greeting('Hank')
print("greeting()傳回值 = ",ret_value)
print(ret_value, " 的 type = ",type(ret_value))

