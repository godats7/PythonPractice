#사전

cabinet={3:"유재석", 100:"김태호"} #key는 3 index값은 유재석
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(5))
print(cabinet.get(5,"사용가능"))
# print(cabinet[5])

print(3 in cabinet)
print(5 in cabinet)

# 새 손님 등장
cabinet[10]="조세호"
print(cabinet)
cabinet[10]="김종국"
print(cabinet)

# 손님이 떠났다
del cabinet[10]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())

# key와 value 쌍으로 출력
print(cabinet.items())

# 문을 닫습니다.
cabinet.clear()
print(cabinet)