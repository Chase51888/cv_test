try:
    with open('test.txt','r+',encoding='UTF-8') as f:#w写 r读 写会清空源文件 a为附加内容 u,w会创建 r+覆盖写 a+附加读写
        f.write('test1\n')
        f.write('test2\n')
        f.write('test3\n')
except ValueError:
    print(1)
else:
    print(2)
finally:
    print(3)

    #try 可能会出现异常的代码块 except加异常名 当该异常发生时执行的代码块 else 都没问题执行的块 finally 无论怎样都执行的代码块
    #unitest 测试库 自带的assertEqual(A,B)方法用于比对A和B是不是相等 要用类写
    import unittest as un
    from 原文件 import 测试的函数
    class Testx(un.TestCase):
        def test_xxx(self): #测试用的函数必须以test_命名 setUp(self)方法可以创建初始的样例包括参数等用于测试，方便后续不用重复赋值
            xxx