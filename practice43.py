# 매주 1회 작성해야 하는 보고서
# 보고서의 형식은 다음과 같다

# - x 주차 주간보고 -
# 부서 : 
# 이름 :
# 업무 요약 : 

# 1주차부터 50주차까지의 보고서 파일을 만드는 프로그램을 작성하시오.

# 조건 :파일명은 '1주차.txt'...와 같이 한다

for i in range(1,51):
    with open("{0}주차.txt".format(i),"w",encoding="utf8") as report_file:
         report_file.write("{0}주차 주간보고".format(i))
         report_file.write("\n부서 :")
         report_file.write("\n이름 :")
         report_file.write("\n업무 요약 :") # write는 기본적으로 덮어쓰기이다.
   


