def calculate_num_print(num,calculate_num):#传入低阶函数的时候，不要带括号
    result=calculate_num(num)
    print(f'''
        数字参数|{num}|
        计算结果|{result}|
        ''')
def calculate_squre(num):
    return num * num
def calculate_cube(num):
    return num*num*num

num=int(input('输入:'))
calculate_num_print(num,calculate_squre)
calculate_num_print(num,calculate_cube)
#对于只可能用一次的函数使用lambda匿名函数，只能有一句后续语句
calculate_num_print(num,lambda x:num+7)
