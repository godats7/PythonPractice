# 사이트 별로 비밀번호 만들기
# 예) http:\\naver.com
# 규칙1 : http:\\부분은 제외 -> naver.com
# 규칙2 : 처음 만나는 점 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자갯수 + 글자 내 e 갯수 + !로 구성
#           (nav)                     (5)         (1)         (!)
# 생성된 비밀 번호 : nav51!

page = "http:\\naver.com"
rule1 = page[6:]
print(rule1)
rule2 = page[6:11]
print(rule2)
rule3 =rule2[:3]+str(len(rule2))+str(rule2.count("e")) + str("!")
print(rule3)


url = "http:\\naver.com"
my_str = url.replace("http:\\","")
my_str =my_str[:my_str.index(".")]
password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0}의 비밀번호는 {1}입니다".format(url,password))