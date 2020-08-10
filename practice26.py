#while(반복)

customer = "토르"
index  =5
while index >=1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다".format(customer,index))
    index = index -1
    if index ==0:
        print("커피는 폐기처분")

customer = "아이언맨"
index =1
while True:
    print("{0}님, 커피가 준비되었습니다. 호출{1}회".format(customer,index))
    index +=1
    if index == 10:
        print("좀 가져가세요")
        break

customer = "토르"
person = "unknown"

while person != customer:
    print("{0}님, 커피가 준비되었습니다. ".format(customer))
    person =input("이름이 어떻게 되세요? ")
    if person =="토르":
        print("기다렸습니다 "+person+"님")
        break