# 지역변수와 전역변수

gun = 10 #전역변수

# def checkpoiont(soldiers):
#     # gun= 20 #지역변수
#     global gun #전역변수를 가져온다 global
#     gun = gun-soldiers
#     print("함수내에서 남은 총{0}".format(gun))

def checkpoiont_return(gun,soldiers):
    gun = gun-soldiers
    print("함수내에서 남은 총{0}".format(gun))
    return gun

print("전체 총{0}".format(gun))
# checkpoiont(2) #2명이 사용
gun  =checkpoiont_return(gun,2)
print("남은 총{0}".format(gun))