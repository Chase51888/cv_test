#继承练习，还用到了多态
#人员管理系统 全职和兼职
#全职兼职都有工号姓名
#都有打印id功能
#全职有月薪，兼职有日薪，每月工作天数
#全职兼职都有计算月薪方法，计算方式不同
class Employee:
    def __init__(self,name_set,id_set,salary_set) -> None:
        self.name=name_set
        self.id=id_set
        self.salary=salary_set
    def print_id(self):
        print(self.id)
    def cac_salary():
        None

class FullTime(Employee):
    def __init__(self, name_set, id_set,salary_set) -> None:
        super().__init__(name_set, id_set,salary_set)
    def set_salary(self,salary_set):
        self.salary=salary_set
    def cac_salary(self):
        return self.salary *1
        

class PartTime(Employee):
    def __init__(self, name_set, id_set,salary_set,work_day_set) -> None:
        super().__init__(name_set, id_set,salary_set)
        self.work_day=work_day_set
    def set_salary(self,salary_set):
        self.salary=salary_set
    def cac_salary(self):
        self.salary = self.work_day * self.salary
        return self.salary

#全职员工
ef = FullTime('牛马','001',None)
ef.set_salary(5100)
print(f'{ef.name}的ID为{ef.id}，本月工资为{ef.cac_salary()}')
#兼职员工
ep = PartTime('人上人','002',80,20)
print(f'{ep.name}的ID为{ep.id}，本月工资为{ep.cac_salary()}')