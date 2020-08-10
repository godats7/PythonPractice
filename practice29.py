from random import *

cnt = 0
for i in range(1,51):
    time = randrange(5,51)
    if 5<= time <=15:
        print("[0] {0}번째 손님 (소요시간 : {1})".format(i, time))
        cnt += 1
    elif cnt == 2:
        print("{0}번 손님을 마지막으로 버스 출발하겠습니다.".format(i))
        break
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1})".format(i, time))
    
        

print("총 탑승승객 : {0}분".format(cnt))
