# 한줄 for

# 출석번호가 1,2,3,4, 앞에 100붙이기로함 -> 101,102,..

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students]
print(students)

students = ["iron man","thor","groot"]
students = [len(i) for i in students]
print(students)

students = ["iron man","thor","groot"]
students = [i.upper() for i in students]
print(students)