# format

print("my name is {0},{1}".format("이욱종","허광지"))
print("my name is {1},{0}".format("이욱종","허광지"))
print("my name is {},{}".format("이욱종","허광지"))

#indexing
my_name = "이욱종의 파이썬"
print(my_name[0])
print(my_name[0:])
print(my_name[0:3])
print(my_name[1:4])
print(my_name[-1])
print(my_name[:-1])
print(my_name[-2:])
print(my_name[:-2])

my_str = "김왼손의 왼손코딩"
print(my_str[-5:-1])
print(my_str[5:])
print(my_str[-5:])

# split
fruit_str = "딸기 배 사과 토마토 수박"
fruits = fruit_str.split()
print(fruits)
