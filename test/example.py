import numpy

#数组 区别python非固定类型 C为固定类型
arrayx=[]#列表用方括号
tuple_test=()#元组tuple 不能操作 不灵活 但是可以作为键 比如重名不同年龄的人
dic_test={'小明':'111',('小王',23):'222','小王':333}#字典：可变用花括号 键：值 删除字典用del 
print (dic_test)
named=dic_test['小王']
print(named)
named=dic_test[('小王',23)]
print(named)
del dic_test['小明']
print (dic_test)

for search_a,search_b in dic_test.items():
    if search_b==333:
        print (search_a)