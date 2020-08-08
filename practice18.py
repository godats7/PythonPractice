# 리스트

# 지하철 칸별로 10명, 20명, 30명
# subway1=10
# subway2=20
# subway3=30

subway=[10,20,30]
print(subway)

subway=["유재석","박명수","조세호"]
print(subway)

#조세호사 몇 번째 칸에 타고 있는가

print(subway.index("조세호"))

# 다음 역에서 하하가 탑승
subway.append("하하") # append는 항상 맨 뒤에 붙음
print(subway)

# 정형돈을 유재석 다음에 태우자
subway.insert(1,"정형돈")
print(subway)

# 뒤에서 한명씩 꺼내보자
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명있는지 확인
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 자양한 자료형 함꼐 사용
mix_list=["조세호",20,True]
num_list = [5,4,3,2,1]
print(mix_list)
num_list.extend(mix_list)
print(num_list)