# 표준 입출력

import sys

print("python","java", sep=",") #sep값으로 value를 어떻게 구분하는지 지정
print("python","java","javascript", sep=" vs ")
print("python","java", sep=",",end="?\n") #마지막줄에 무엇을 넣을지 end

print("python","java","javascript", file=sys.stdout)
print("python","java","javascript", file=sys.stderr)

scores = {"수학":0,"영어":50,"코딩":100}#딕셔너리
for subject,score in scores.items():
    print(subject,score)
    
scores = {"수학":0,"영어":50,"코딩":100}#딕셔너리
for subject,score in scores.items():    
    print(subject.ljust(8),score)
    
scores = {"수학":0,"영어":50,"코딩":100}#딕셔너리
for subject,score in scores.items():   
    print(subject.ljust(8),str(score).rjust(4), sep=" : ")    

#은행 대기순번표
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(3))
for num in range(1,21):
    print("대기번호 : "+str(num).zfill(4))

# 표준입력

answer = input("아무 값이나 입력하세요 :") #input 으로 받은 값은 무조건 str
print(type(answer))
print("입력하신 값은 "+answer+"입니다.")
