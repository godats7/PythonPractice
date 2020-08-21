# comprehension

numbers = [1,2,3,4,5,6,7,8,9,10]
odd_number=[]

# for number in numbers:
#     if number % 2 == 1:
#         odd_number.append(number)
# print(odd_number)

odd_number=[number for number in numbers if number % 2 == 1]
print(odd_number)
