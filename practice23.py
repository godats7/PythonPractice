from random import *
num = range(1,21)
num = list(num)

# print(num)
# print(list)
shuffle(num)
winner = sample(num, 4)
print(winner)
print("--당첨자--")
print("치킨 당첨자 : {0}".format(winner[0]))
print("커피 당첨자 : {0}".format(winner[1:]))