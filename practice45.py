#  클래스

class Unit:
    def __init__(self,name,hp,damage): #__init__은 생성자
        self.name = name #self.변수명은 멤버변수
        self.hp = hp
        self.damage = damage
        print("{0}유닛이 생성되었습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp,self.damage))

marine1 = Unit("마린","40","5")
marine2 = Unit("마린","40","5")
tank = Unit("시즈탱크",150,35)
print(type(marine1))
print(type(marine2))
print(type(tank))

# 레이스 : 공중유닛, 비행기, 클로킹
wraith1 = Unit("레이스",80,5)
print("유닛이름 : {0}, 공격력 : {1}".format(wraith1.name,wraith1.damage))

# 레이스를 마인트컨트롤해보자
wraith2 = Unit("빼앗은 레이스",80,5)
wraith2.clocking = True
if wraith2.clocking ==True:
    print("{0}는 지금 클로킹 상태입니다.".format(wraith2.name))