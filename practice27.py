# continue, break

absent = [2,5] #결석
no_book=[7] #책없음
for student in range(1,11): # 1~10까지
    if student in absent :
        continue
    elif student in no_book:
        print("{0}는 교무실로 따라와".format(student))
        continue
    print("{0},학생 책을 읽어봐".format(student))