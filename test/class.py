class CuteCat:
    def __init__(self,nameSet,ageSet,colorSet) -> None:#构造函数
        self.name=nameSet
        self.age=ageSet
        self.color=colorSet
        self.rate=0
    def speak(self):
        print('Miao'*self.age)
    def set_rate(self,rateSet):
        self.rate=rateSet
cat1=CuteCat('HUA',1,'White')
print(f'Cat named {cat1.name},its age is {cat1.age},and color is {cat1.color}')
cat2=CuteCat('Niu',2,'Black')
print(f'Cat named {cat2.name},its age is {cat2.age},and color is {cat2.color}')

cat1.speak()
cat2.speak()

cat1.set_rate(2)
cat2.set_rate(1)
print(f'{cat1.name}的评级为{str(cat1.rate)},{cat2.name}的评级为{str(cat2.rate)}')