# 파일 입출력

# score_file = open("score.txt","w",encoding="utf8") #w는 쓰기
# print("수학 : 0점", file=score_file)
# print("영어 : 50점", file=score_file)
# score_file.close()

# score_file = open("score.txt","a",encoding="utf8") #a는 append
# score_file.write("과학 : 80점")
# score_file.write("\n코딩 : 100점")
# score_file.close()

# 파일 출력
score_file = open("score.txt","r",encoding="utf8") # r은 읽어들이기
print(score_file.read())
score_file.close()

score_file = open("score.txt","r",encoding="utf8")
print(score_file.readline()) # 한 줄 읽고 커서는 다음줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())
score_file.close()