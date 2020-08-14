# 표준체중 구하기

# 성별 공식
# 남자 : 키*키*22
# 여자 : 키*키*21

# 조건1 : 표준체중은 졀도의 함수 내에서 계산
#     *함수명 :std_weight
#     *전달값 :키(height), 성별(gender)
# 조건2 : 표준 체중은 소수점 둘째자리까지 표시

# 출력예제
# 키 175cm 남자의 표준 체중은 67.38kg이다.

def std_weight(height, gender):
    if gender == "남자":
        return height*height*22
    elif gender =="여자":
        return height*height*21

height = 175
gender = "남자"   
std_weight = round(std_weight(height /100,gender),2)
print("이사람의 키는 {0}이고 성별은 {1}이고 표준체중은 {2}이다".format(height, gender, std_weight))