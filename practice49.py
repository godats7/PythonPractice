# 연산자 오버로딩

class Unit: #일반 유닛  부모클래스
    def __init__(self,name,hp,speed): #__init__은 생성자
        self.name = name 
        self.hp = hp 
        self.speed =speed     
    def move(self,  location):
        print("지상유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name,location,self.speed))

class AttackUnit(Unit): # Unit을 상속하는 AttackUnit  자식클래스
    def __init__(self,name,hp,speed,damage): 
        Unit.__init__(self, name,hp,speed) #Unit에서 이름과 체력을 가져놈        
        self.damage = damage
    def attack(self, location)    :
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력은 {2}]".\
            format(self.name,location,self.damage))

    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기, 다른 지상유닛을 수송, 공격x
class Flyable : 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

# 공중 공격 유닛 클래 스
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp,0,damage) #지상스피드는 0
        Flyable.__init__(self,flying_speed)
    def move(self, location):
        print("공중유닛 이동")
        self.fly(self.name, location)
        
# 벌처 : 지상유닛, 기동력이 좋음
vulture = AttackUnit("벌쳐",80,10,20)

# 배틀크루져 : 공중유닛, 체력도 공격력도 좋음
battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,"9시")
battlecruiser.move("9시")