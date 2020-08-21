# operator(할당 연산자 =,+=,-=,/=,*=)

# a = b # b의 값을 a에 할당한다(넣는다)
# a += b # a에 b의 값을 더한다

count = 1
print(count)

count += 1
print(count)

# 산술연산자(+,-,/,*)

# 산술연산자( **,//,%)

a = 3**2 
print(a)
a = 3//2
print(a)
a = 3%2
print(a)

numbers = [1,2,3,4,5,6,7,8,9,10]

odd_numbers = [number for number in numbers if number % 2==1]
print(odd_numbers)

even_numbers = [number for number in numbers if number % 2==0]
print(even_numbers)