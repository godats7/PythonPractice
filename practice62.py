# 내장함수
# input  : 사용자의 입력을 받는 함수

language = input("무슨 언어를 좋아하세요? : ")
print("{0}는 매우 좋은 언어입니다.".format(language))

# dir : 어떤 객체를 넘겨줬을 때 그 객체가 어떤 변수와 함수를 가지고 있는지 표시
print(dir())
import random
print(dir())
import pickle
print(dir())

print("이것은 랜덤에서 사용가능한 것들 : "+str(dir(random)))
print("\n"*5)

name ="이욱종"
print(dir(name)) #name이란 변수에서 사용가능한 내용들을 전부 보여준다.
