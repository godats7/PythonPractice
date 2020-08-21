# for

# for 변수 in 컨테이너
    # 실행할 명령



elements=("땅","불","바람","물","마음")

for element in elements:
    print(element, end=" ")

for me in "이욱종":
    print(me)

for number in range(0,5):
    print(number)

# 구구단
for j in range(2,10):
    for i in range(1,10):
        print("{0}x{1}={2}는 {0}단".format(j,i,i*j) )
        if i==9:
            print("\n")
