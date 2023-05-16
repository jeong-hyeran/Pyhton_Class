# PYTHON_PROGRAMMING 조건문 IF
# If 문 
# ❖ if문 
# ▪ if 조건식 : 에서 조건식이 참이면 실행할 문장이 처리되고, 
# 거짓이면 아무것도 실행하 지 않고 프로그램을 종료 

# if 조건식 : 
# 종속문장 
# 다음 문장 
# if 조건식 : 
# 종속문장 
# 종속문장 
# 다음 문장; 
# 조건식 
# 참
# 종속문장 다음 문장 
# 거짓 

# 예제 
# num1 = 10 
# num2 = 5 
# if num1 > num2: 
# print("num1 이 num2보다 크다")
# 예제 
# num1 = int(input("수 입력 : ")) 
# if num1 % 2 == 0: 
# print("num1 : ",num1,"짝수다") print("나는 다음 문장")
# 예제 
# num1 = int(input("수 입력 : ")) 
# if num1 % 2 == 0: 
# print("num1 : ",num1,"짝수다") 
# print("num1 : ",num1,"2의 배수이다") print("나는 다음 문장")
# 예제 
# print("1.easy game") 
# print("2.hard game") 
# print("3.exit") 
# num1 = int(input("선택 : ")) if num1 == 1: 
# print("easy game start") if num1 == 2: 
# print("hard game start") if num1 == 3: 
# print("game exit")
# 문제 
# ❖날짜를 입력받아 요일을 구하시오. 
# (단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일) (어떤 값을 입력을 받던 요일이 정확히 출력 되게 만드시오
# Quiz 
# ❖ 입력한 데이터가 3의 배수인 경우 출력하시오. 
# ❖ 절대값을 구하는 프로그램을 작성하시오. 
# ❖ 수를 입력 받아 짝,홀수를 구분하여 출력하시오. ❖ 두수를 입력 받아 큰 수를 출력하시오. 
# ❖ 세수를 입력 받아 큰 수를 출력하시오. 
# ❖ 두수를 입력 받아 큰 수가 짝수이면 출력하시오. ❖ 두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.

# If else문 
# ❖ if~else 문 
# ▪ 참일 때 실행하는 문장과 거짓일 때 실행하는 문장이 다를 때 사용 
# if 조건식 : 
# 종속문장 
# 거짓 

# else : 
# 종속문장 
# 다음 문장 
# 조건식 
# 참 
# else이후 

# if 조건식 : 
# 종속문장 
# 종속문장 
# else : 
# 종속문장 
# 종속문장 
# 다음 문장; 
# 종속문장 다음 문장 
# 종속문장

# 예제 
# num = int(input("수 입력 : ")) if num == 1: 
# print("1입력") 
# else: 
# print("1 이 아닌 값 입력")
# 예제 
# arr = [1,2,3,4,5] 
# na = int(input("찾을 숫자 입력 : ")) 
# if na in arr: 
# print("arr : ",arr,"찾는 숫자가 존재 합니다 : ",na) else: 
# print("arr : ",arr,"안에는 찾고자 하는 숫자가 없습니다 : ",na) print('결과 : ',na in arr)
# 예제 
# st = "Hello Python Fun" 
# na = input("찾고자 하는 문자열 입력 : ") if na in st: 
# print("st : ",st,"찾는 문자열 : ",na,"존재 한다") else: 
# print("st 안에는 ",na,"존재 하지 않습니다")
# 예제 
# old_id = input("저장할 ID 입력 : ") print("인증 프로그램 입니다") print("ID와 PW를 입력하세요") new_id = input("ID 입력 : ") if old_id == new_id : 
# print("인증 통과 했습니다") else: 
# print("인증 실패")

# 중첩된 if 문 
# if 조건식 1 : 
# if 조건식 2 : 
# 종속문장 1 
# else : 
# 종속문장 2 
# 조건식 1 
# 거짓 거짓 
# 참 
# 조건식 2 참

# else : 
# 종속문장 3 
# 다음 문장; 
# 문장3 문장2 문장1 다음문장 

# 예제 
# num = int(input("수 입력 : ")) 
# if num % 3 == 0: 
# if num % 2 == 0: 
# print("num은 3의 배수면서 짝수 입니다") 
# print("다음문장 실행") 
# ❖ If문 하나로 변경하시오.
# 예제 
# num = int(input("수 입력 : ")) if num > 0: 
# if num % 2 == 0: 
# print("num은 양의 짝수 입니다") else: 
# print("num은 양의 홀수 입니다") else: 
# print("num은 음수 입니다") 
# print("다음문장 실행")
# Quiz 
# ❖ 사용자로 부터 Gbyte의 값을 입력받아 byte,Kbyte,Mbyte로 각각 출력 되 게 만드시오.(1.byte 2.Kbyte 3.Mbyte 선택) 
# ❖ 인증 프로그램을 만드시오. 
# • 1.아이디가 틀리면 등록되지 않은 아이디 입니다 출력 
# • 2.비밀번호가 틀리면 비밀번호가 틀렸습니다 출력 
# • 3.아이디와 비밀번호가 일치한다면 인증 통과 출력

# elif 문 
# 조건식 1 
# 각 조건에 맞는 부분을 찾아서 실행 
# 거짓 
# if 조건식 1 : 문장1 
# elif 조건식 2 : 문장 2 
# 참거짓 
# 조건식 2 참 

# elif 조건식 3 : 문장 3 
# …… 
# elif 조건식 n : 문장 n 
# else : 
# 문장 n+1
# 문장3 문장2 문장1 다음문장 

# 예제 
# num = int(input("수 입력 : ")) if num > 100: 
# print("100보다 큰 수 입력") elif num > 50: 
# print("50보다 큰 수 입력") elif num > 0: 
# print("0보다 큰 수 입력") else: 
# print("그 외의 값 입력")
# Quiz 
# ❖ 이름, 학번, 3과목의 성적을 입력 받아 합계와 평균을 구하고, 평균이 90이상이면 ‘A’, 80 이상‘B’, 70이상 ’C’, 60이상 ‘D’, 60미만이면 ‘F’ 를 출력하시오 
# ❖ 커피의 개당 가격은 2000원이다. 10개 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다. 커피의 개수를 입력 받아 금액을 출력하시오. 
# ❖ 정수를 입력받아 아래와 같이 출력하시오. 
# 3의배수이면서,4의배수 입니다 
# 3의배수 입니다 
# 4의배수 입니다 
# 3의배수도,4의배수도 아닙니다 
# 0은3의 배수도 4의 배수도 아닙니다. 

# 비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 
# 10분 단위로 추가요 금 5000원씩 부가된다. 
# 비행기 탈 시간을 입력하여 요금 계산기를 만드시오.
# time=40
# # if 30 < time: print("추가시간 발생")
# # # elif num%10==0:
# # #     print("10의 배수")
# # if time%10!=0:
# #      extra_time=time//10
# #      print(extra_time)
# # extra_time=time//10
# # if (30 < time) and (time%10!=0):
    
# #     print("추가비행 시간은 %d분"%extra_time) 
# # else:print("비행요금은 30000원 입니다.")

# # extra_time=(time)
# # extra_time 은 time > 30 일 경우에 발생
# # extra_time 은 time-30 이다
# if (time > 30):
#     extra_time =(time-30)
#     strat_time= extra_time%10==1
#     end_time= extra_time%10==0
#     print("추가시간 %d분 발생"%extra_time,
#           "시작시간 %d분"% strat_time,
#           "종료시간 %d분"% end_time)


#     # if 0 < extra_time < 10:
#     #     print("추가 금액 %d원"%5000)



#     # strat_time= extra_time%10==1
#     # end_time= extra_time%10==0
#     # if strat_time< extra_time < end_time:
#     #     money=extra_time*15000
#     #     print("추가요금은 %d원 이다."% money)