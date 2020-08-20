# 스타크래프트 프로젝트

from random import *

class Unit:
    def __init__(self,name,hp,speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성되었습니다.".format(name))

    def move(self,  location):
        print("지상유닛 이동")
        print("{0} : {1} 방향으로 이동합니다. [속도 {2}]".format(self.name,location,self.speed))

    def damaged(self, damage):
        print("{0} : {1}데미지를 입었습니다.".format(self.name,damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1}입니다.".format(self.name,self.hp))
        if self.hp <=0:
            print("{0} : 파괴되었습니다.".format(self.name))

class AttackUnit(Unit): 
    def __init__(self,name,hp,speed,damage): 
        Unit.__init__(self, name,hp,speed) 
        self.damage = damage
    def attack(self, location)    :
        print("{0} : {1}방향으로 적군을 공격합니다. [공격력은 {2}]".\
            format(self.name,location,self.damage))

class Flyable(Unit) : 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed
    
    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]"\
            .format(name,location,self.flying_speed))
  
#  마린 클래스

class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self,"마린",40,1,5)
# 마린의 스팀팩 :  일정시간동안 공격속도및 이동속도 증가 체력 10감소
    def stimpack(self):
        if self.hp> 10:
            self.hp -= 10
            print("{0} : 스팀팩을 사용합니다. (HP10 감소)".format(self.name))
        else :
            print("{0} : 체력이 부족하여 사용할 수 없습니다.".format(self.name))

# 탱크 클래스

class Tank(AttackUnit):
# 탱크의 시즈모드
    seige_developed = False
    def __init__(self):
        AttackUnit.__init__(self,"시즈탱크",150,1,35)
        self.seige_mode=False
    def set_seige_mode(self):
        if Tank.seige_developed == False:
            return
        #현재 시즈모드 아닐때 -> 시즈모드
        if self.seige_mode == False:
            print("{0} :  시즈모드로 전환합니다.".format(self.name))
            self.damage *=2
            self.seige_mode = True
        #현재 시즈모드일때 -> 시즈모드 해제
        else:
            print("{0} :  시즈모드를 해제합니다.".format(self.name))
            self.damage /=2
            self.seige_mode = False

# 공중공격유닛
class FlyableAttackUnit(AttackUnit,Flyable):
    def __init__(self,name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp,0,damage) #지상스피드는 0
        Flyable.__init__(self,flying_speed)
    def move(self, location):
        print("공중유닛 이동")
        self.fly(self.name, location)

# 레이스
class Wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self,"레이스",80,20,5)
        self.cloaked = False #클로킹 해제
    
    def cloaking(self):
        if self.cloaked == True:
            print("{0} : 클로킹을 해제합니다.".format(self.name))
            self.cloaked = False
        else:
            print("{0} : 클로킹을 설정합니다.".format(self.name))
            self.cloaked = True

def game_start():
    print("새로운 게임을 시작합니다.")

def game_over():
    print("Player : GG")
    print("[Player] 님이 게임에서 퇴장하셨습니다.")


# 실제 게임 진행
game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = Wraith()

# 유닛 일괄관리
attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동
for unit in attack_units:
    unit.move("1시")

# 탱크 시즈모드 개발
Tank.seige_developed =True
print("[알림] 시즈모드가 개발되었습니다.")

# 공격모드 준비
for unit in attack_units:
    if isinstance(unit,Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seige_mode
    elif isinstance(unit,Wraith):
        unit.cloaking()

# 공격
for unit in attack_units:
    unit.attack("1시")

# 데미지 받음
for unit in attack_units:
    unit.damaged(randint(5,21))

# 게임종료
game_over()





        






    
    