# 클래스

# 마린 : 공격 유닛, 군인, 총을 쏜다
name = "marine"
hp = 40
damage = 5

print("{0}유닛이 생성되었습니다.".format(name))
print("체력은 {0}이고 공격력은 {1}입니다.\n".format(hp,damage))

#탱크 : 공격 유닛, 탱크, 포를 쏘며 일반모드/시즈모드가 있다.
tank_name = "siege tank"
tank_hp = 150
tank_damage =35

print("{0}유닛이 생성되었습니다.".format(tank_name))
print("체력은 {0}이고 공격력은 {1}입니다.\n".format(tank_hp,tank_damage))

def attack(naem, location,damage):
    print("{0} : {1}방향으로 적군을 공격합니다.[공격력 {2}]".format(name,location,damage))

attack(name,"1시",damage)
attack(tank_name,"1시",tank_damage)