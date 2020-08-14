def profile(name, age, main_lang):
    print("이름 : {0}\t 나이 : {1}\t 주 사용안어 : {2}"\
        .format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 기본값 설정

def profile2(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t 나이 : {1}\t 주 사용안어 : {2}"\
        .format(name, age, main_lang))

profile2("유재석")
profile2("김태호")
