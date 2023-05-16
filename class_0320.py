#[if~else문]
# 참일때와 거짓일때 나오는 실행문
# 참일때만 종속문자, 거짓이면 무조건 else

# num=int(input("수 입렵: "))
# if num==1:
#     print("1입력")
# else:
#     print("1이 아닌 값 입력")
# ##=> 1일 경우 "1입력" 1이 아닐 경우 "1이 아닌 값 입력"이 나옴
# if문이 거짓이라 else값이 나온다.
# => 참일 때와 거짓인 값을 다 확인 해봐야한다.

# arr=[1,2,3,4,5] #=> 리스트
# na=int(input("찾을 숫자 입력 :"))
# if na in arr:
#     print("arr :",arr,"찾는 숫자가 존재 합니다 :", na)
# else:
#     print("arr:",arr,"안에는 찾고자 하는 숫자가 없습니다.:",na)
# print('결과:',na in arr)

# a in b 에서 in은 멤버 연산자라 불리웁니다.
# 뜻은 b안에 a가 존재하면 참, 존재하지 않으면 거짓입니다.
# 즉 a in b의 문법은 True나 False를 반환합니다.
# 상대되는 표현으로는
# a not in b가 있습니다.
# 뜻은 b안에 a가 존재하지 않으면 참, 존재하면 거짓이 됩니다.

# st="Hello Python Fun"#시퀀스형 자료형
# na=input("찾고자 하는 문자열 입력 :")
# if na in st:
#     print("st:",st,"찾는 문자열 :",na,"존재한다")
# else:
#     print("st 안에는 ",na, "존재 하지 않습니다.")
#=> 대 소문자 구분해서 출력이 된다.

# old_id=input("저장한 ID 입력")
# print("인증 프로그램입니다.")
# print("ID와 PW를 입력하세요")
# new_id=input("ID입력 : ")
# if old_id==new_id:
#     print("인증 통과 했습니다.")
# else:
#     print("인증 실패")

# [중첩된IF문]
# f 조건식 1 :  => 참이면 아래것, 거짓이면 바로 맨 아래 else로
#     if 조건식 2 :   => 참이면 아래것
#         종속문장 1  => 참이면 아래것
#     else : 
#         종속문장 2 
# else : 
#     종속문장 3 
# 다음 문장; 

# num=int(input("수 입력:")) 
# if num % 3 ==0:
#     if num % 2 ==0:
#         print("num은 3의 배수면서 짝수입니다.")
# print("다음 문장 실행")

# num=int(input("수 입력:"))
# if num%3==0 and num%2==0:
#      print("num은 3의 배수면서 짝수입니다.")
# print("다음 문장 실행")

#강사님 풀이
# num=int(input("수 입력:"))
# if num%3==0 and num%2==0:
#      print("num은 3의 배수면서 짝수입니다.")
# print("다음 문장 실행")

# num = int(input("수 입력:"))
# if num >= 0:
#     if num % 2 == 0:
#         print("num은 양의 짝수 입니다.")
#     else:
#         print("num은 양의 홀수 입니다.")
# else:
#     print("num은 음수입니다.")
# print("다음 문자 실행")
#=> 요것은 순서를 바꿀수 없고, if문 하나로 변경 할 수도 없다.
#else문으로 바로 확인 할 수 있다!

#  인증 프로그램을 만드시오. 
#  1.아이디가 틀리면 등록되지 않은 아이디 입니다 출력 
#  2.비밀번호가 틀리면 비밀번호가 틀렸습니다 출력 
#  3.아이디와 비밀번호가 일치한다면 인증 통과 출력
# 중첩으로 만들고, 하나는 네이버처럼 (아이디 패스워드 한번에 입력)
# 구글은 (아이디 인증 후 패스워드 입력)

# old_id=input("저장된 ID 입력")
# old_pw=input("저장된 PW 입력")
# print("ID와 PW를 입력하세요")
# new_id=input("ID입력 : ")
# new_pw=input("PW입력 : ")
# if old_id!=new_id:
#     print("등록되지 않은 아이디 입니다.")
#     eles:print("인증 실패")
# if old_pw!=new_pw:
#      print("비밀번호가 틀렸습니다.")
#      eles:print("인증 실패")
# else:
#     print("인증 통과")

# old_id=input("저장된 ID 입력")
# old_pw=input("저장된 PW 입력")
# print("ID와 PW를 입력하세요")
# new_id=input("ID입력 : ")
# new_pw=input("PW입력 : ")
# if old_id==new_id:
#     print(new_pw=input("PW입력 : "))
#     if old_pw==new_pw:
#         eles:print("인증 통과")
##===> 내가 한거 다 버그 !! 확인하기!

#=>강사님 풀이
#네이버 방식
# save_id=input("저장할 id 입력 : ")
# save_pw=input("저장할 pw 입력 : ")
# print("=============== 인증 프로그램 ===============")
# new_id = input("id 입력 : ")
# new_pw = input("pw 입력 : ")
# if save_id == new_id :
#      if save_pw == new_pw :
#        print("인증 통과!!!")
#      else :
#       print("비밀번호가 틀렸습니다")
# else :
#     print("등록되지 않은 id 입니다")

# 구글방식
# save_id=input("저장할 id 입력 : ")
# save_pw=input("저장할 pw 입력 : ")
# print("=============== 인증 프로그램 ===============")
# new_id = input("id 입력 : ")
# if save_id == new_id :
# new_pw = input("pw 입력 : ")
# if save_pw == new_pw :
# print("인증 통과!!!")
# else :
# print("비밀번호가 틀렸습니다")
# else :
# print("등록되지 않은 id 입니다")

#elif문
# if elif else 다중if문
# 다 거짓인 경우 마지막 eles문이 필요한데
# 위에서 참일 경우 그냥 빠져나가기 때문에 안 적어도 된다!

# num = int(input("수 입력 : ")) 
# if num > 100: 
#     print("100보다 큰 수 입력") 
# elif num > 50: 
#     print("50보다 큰 수 입력") 
# elif num > 0: 
#     print("0보다 큰 수 입력") 
# else: 
#     print("그 외의 값 입력")

#다중if문은 단위의 중복 여부를 신경 써야 한다.

# 이름, 학번, 3과목의 성적을 입력 받아 합계와 평균을 구하고, 
# 평균이 90이상이면 ‘A’, 80 이상‘B’, 70이상 ’C’, 
# 60이상 ‘D’, 60미만이면 ‘F’ 를 출력하시오 

# name=input("이름 : ")
# num=input("학번 : ")
# score_1=input("첫번째 과목 :")
# score_2=input("두번째 과목 :")
# score_3=input("세번째 과목 :")
# sum_=(score_1+score_2+score_3)
# ave=int(sum_/3)

# if ave >= 90:
#     print("A")
# elif ave >= 80:
#     print("B")
# elif ave >= 70:
#     print("C")
# elif ave >= 60:
#     print("D")   
# else:print("F")

##=> 강사님 풀이
# name=input("이름 입력 : ")
# hak =input("학번 입력 : ")
# kor=int(input("국어 점수 : "))
# eng=int(input("영어 점수 : "))
# mat=int(input("수학 점수 : "))
# sum_=kor+eng+mat
# avg=sum_/3
# if avg>=90 : level ='A'
# elif avg>=80 : level ='B'
# elif avg>=70 : level ='C'
# elif avg>=60 : level ='D'
# else :level='F'
# print("======================== 성적표 ========================")
# print("이름\t학번\t국어\t영어\t수학\t총점\t평균\t학점")
# print("%s\t%s\t%d\t%d\t%d\t%d\t%.2f\t%c"%(name,hak,kor,eng,mat,sum_,avg,level))



# 커피의 개당 가격은 2000원이다. 
# 10개 초과하면 초과하는 양에 대해서만 개당 1500원씩 받는다. 
# 커피의 개수를 입력 받아 금액을 출력하시오. 

# coffee_1=2000
# coffee_11=1500 #11잔 이상부터 가격
# oder=int(input("커피 개수 : "))
# sum_10=int((coffee_1)*10)  #10잔 가격
# sum_11=int((oder-10)*coffee_11) # 11잔 부터 총 금액
# # if oder <= 10:
# #     print("%s원 입니다."%oder*coffee_1)
# # if oder > 10:
# #     print("%s원 입니다."%(10*coffee_1)+((oder-10)*coffee_11))

# if oder > 10:
#     print(sum_10+sum_11)
# elif oder <= 10:
#     print(coffee_1*oder)

##=> 강사님 풀이

# coffee=int(input("주문할 커피수량 입력 : "))
# if coffee > 10 : #초과분이 발생된경우
#     money= 2000*10+(coffee-10)*1500
# else :# 10잔 이하인경우
#     money= 2000 * coffee
# print("주문한 커피 금액 : %d원"%money)



# 정수를 입력받아 아래와 같이 출력하시오. 
# 3의배수이면서,4의배수 입니다 
# 3의배수 입니다 
# 4의배수 입니다 
# 3의배수도,4의배수도 아닙니다 
# 0은3의 배수도 4의 배수도 아닙니다. 

# num=int(input("정수 입력 :"))
# if num % 3 ==1 and num % 4 ==1:
#     print("%d은 3의배수이면서,4의배수 입니다."% num)
# if num % 3 ==1 :
#     print("%d은 3의배수 입니다."% num)
# if num % 4 ==1:
#     print("%d은 4의배수 입니다."% num)
# if num % 3 !=1 and num % 4 !=1:
#     print("%d은 3의배수도,4의배수도 아닙니다."% num)
# else : num = 0
# # ??    print("%d은 3의배수도,4의배수도 아닙니다."% num)
# ==>> 내꺼에서 순서와 배수... % 뒤에 0

##=> 강사님 풀이
# num1 = int(input("정수입력 : "))
# if num1 == 0:
#     print("0은3의배수도4의배수도 아닙니다.")
# elif num1 %3 == 0 and num1 %4 == 0 :
#     print("3의배수이면서,4의배수 입니다")
# elif num1%3 == 0 :
#     print("3의배수입니다")
# elif num1%4 == 0 :
#     print("4의배수입니다")
# else :
#     print("3의배수도,4의배수도 아닙니다")

# 비행기를 타는데 30분 거리까지의 기본 요금은 30000원이며, 
# 10분 단위로 추가요금 5000원씩 부가된다. 
# 비행기 탈 시간을 입력하여 요금 계산기를 만드시오.

# charg_30min=30000
# extra_10=5000
# time=int(input("비행 시간을 입력하시오. [분 단위]"))
# time_exr1=31
# time_exr2=40
# extra_time=time-30
# extra_monye=(extra_time)*5000
# if time_exr1 < time < time_exr2:print(30000+5000)
# # elif time_exr1+10 < time < time_exr2+10:
# #     print("비행기 요금은 30000원 입니다.")
# else: print("비행기 요금은 30000원 입니다.")

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

#  time=40
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