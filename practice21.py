# 세트(set)
# 중복이 안됨 순서가 없음
my_set = {1,2,3,3,3}
print(my_set)

my_set2 = (1,2,3,3,3)
print(my_set2)

java={"유재석","김태호","양세형"}
python=set(["유재석","박명수"])

# 교집합( java와 python 을 모두 하는 사람)
print(java & python)
print(java.intersection(python))

#합집합( java도 python도 할 수 있는 사람)
print(java | python)
print(java.union(python))

#차집합(java는 하지만 python은 모르는 사람)
print(java-python)
print(java.difference(python))

#python을 할 줄 아는 사람이 늘어남
python.add("김태호")
print(java)
print(python)

# java를 까먹음
java.remove("김태호")
print(java)
print(python)