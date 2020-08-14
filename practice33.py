# 가변인자

# def profile(name, age, lang1,lang2,lang3, lang4, lang5):
#     print("이름 : {0}\t 나이{1}\t ".format(name, age), end=" " )
#     print(lang1,lang2,lang3,lang4,lang5)

def profile(name, age, *language):
    print("이름 : {0}\t 나이{1}\t ".format(name, age), end=" " )
    for lang in language:
        print(lang, end=" ")
    print()    

profile("유재석",20,"파이썬","자바","씨","기타","등등","추가로")
profile("김태호",25,"코틀린","스위프트")