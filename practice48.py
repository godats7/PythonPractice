# 다중상속

class Unit: #일반 유닛  부모클래스
    def __init__(self,name,hp): #__init__은 생성자
        self.name = name 
        self.hp = hp      

class AttackUnit(Unit): # Unit을 상속하는 AttackUnit  자식클래스
    def __init__(self,name,hp,damage): 
        Unit.__init__(self, name,hp) #Unit에서 이름과 체력을 가져놈        
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
    
    def fly(self,name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))

# 공중 공격 유닛 클래서
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp,damage)
        Flyable.__init__(self,flying_speed)

# 발키리 : 공중공격유닛, 한번에 14발의 미사일 발사
valkyrie = FlyableAttackUnit("발키리",200,6,5) #발키리를 만든다
valkyrie.fly(valkyrie.name,"3시") #발키리를 이동시킨다.

