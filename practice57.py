# 동네에 항상 대기손님이 있는 치킨집이 있다.
# 대기손님의 치킨요리 시간을 줄이고자 자동주문을 한다.
# 적절한 예외처리 구문을 만들기

# 조건 1 : 1보다 작거나 숫자가 아닌 입력값이 들어올 때는 valueerror 로 처리
# 조건 2 : 대기 손님이 주문 할 수 있는 치킨 량은 10마리로 한정
#         치킨 소진시 사용자 정의 에러 soldouterror
#         출력 메시지 :  재고가 소진되어 더 이상 주문을 받지 않습니다.


chicken = 10
waiting = 1

class SoldOutError(Exception):
    pass


while (True):
    try:
        print("[남은 치킨 : {0}]".format(chicken))
        order = int(input("몇 마리를 주문하시겠습니까?"))
        if order > chicken:
            print("재료가 소진되었습니다.")
        elif order <= 0:
            raise ValueError
        else:
            print("[대기번호 {0}] {1}마리 주문이 완료되었습니다.".format(waiting,order))
            waiting +=1
            chicken -= order
        
        if chicken ==0:
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하였습니다.")
    except SoldOutError as identifier:
        print("재고가 소진되어 더 이상 주문을 받지 않습니다.")
        break
    


