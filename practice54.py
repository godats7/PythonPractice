# 에러를 발생시켜보자

try:
    print("==한 자리 숫자 전용 나누기 계산기==")
    num1 = int(input("첫 번째 숫자를 입력하세요 : "))
    num2 = int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >=10 or num2 >= 10:
        raise ValueError #raise는 에러를 의도적으로 발생시킨다.
    print("{0} / {1} = {2}".format(num1,num2,int(num1/num2)))
except ValueError as err:
    print("잘못된 값을 입력하였습니다. 한 자리 숫자만 입력하세요")
    print(err)