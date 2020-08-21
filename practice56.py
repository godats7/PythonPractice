# finally 예외에 상관없이 무조건 실행

class BigNumberError(Exception):
    def __init__(self,msg):
        self.msg = msg
    def __str__(self):
        return self.msg

try:
    print("==한 자리 숫자 전용 나누기 계산기==")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >=10 or num2 >= 10:
        raise BigNumberError("입력값 : {0}, {1}".format(num1, num2)) #raise는 에러를 의도적으로 발생시킨다.
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError as err:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
    print(err)
except BigNumberError as err:
    print("에러가 발생 한자리만 입력하세요")
    print(err)
    
finally:
    print("계산기를 이용해주셔서 감사합니다.")