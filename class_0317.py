# 양수는 bit부정 하면 숫자는 1이 늘어난다.
# 음수는 bit부정 하면 숫자는 1이 줄어든다.
# 2진수는 음수 표현이 없다.그래서 부호비트라는 것을 사용한다.
# 보수...? =-======힝.. ㅜㅜ
# 보수 
# 10진수의 보수
# 7의 보수는 3, 6의 보수는 4
# 10진수의 N-1보수(9의 기준)
# 7의 보수는 2, 6의 보수는 3

# 2진수 N-1보수는 반전시키면 된다.
# 인터넷에서 8비트로 만들 수 있는 가장 큰수는 얼마일까..127
# 제일 작은 수 -128...
# 뭔 소리야야양 흐이이잉 ㅠ

##2진수 10진수 변환을 .. 공부해야한다.

# num1=3
# num2=5
# result=num1|num2 # 2진수 변환 후 논리연산 진행 or
# print(result)
#=> 출력값 7

# num1=3
# num2=5
# result=num1&num2 # 2진수 변환 후 논리연산 진행 and
# print(result)
# #=> 출력값 1

# num1=3
# num2=5
# result=num1^num2 # 2진수 변환 후 논리연산 진행 xor(배타적 논리합)
# print(result)
#=> 출력값 6

# print(5 << 2) #5를 2진수 변환 후 2비트 왼쪽으로 이동 (숫자가 커짐)
# #=> 출력값 20
# print(20 >> 2) #20를 2진수 변환 후 2비트 오른쪽으로 이동 (숫자가 작아짐)
# #=> 출력값 5
#                 #단, 비트전체가 2의 0승 자리보다 더 안쪽으로 이동되면 결과는 0

# [if문]

# 제어문
# 기본적인 흐름은 좌에서 우로, 위에서 아래의 흐름(책읽는 진행 방향)을 갖는다. 
# 하지만 이 흐름을 제어한다 해서 제어문이라 표현
# 제어문은 크게 조건문과 반복문으로 나뉜다.

# 조건문(분기문)
# 조건제어문은 조건식의 결과(True, False)에 따라서
# 흐름이 나뉘는 문법을 조건제어문이라고 함
# if라는 키워드를 사용함 조건문은 다양한 유형이 있음

# num1=10
# num2=5

# if num1>num2: #참이여서 출력 됨
#     print("num1이 num2보다 크다")
#     #=>출력값
#     # num1이 num2보다 크다

# num1 = int(input("수 입력 : "))

# if num1%2==0:
#     print("num1 :",num1,"짝수다")
# print("나는 다음 문장")

#=> 출력값
# -> 입력 값 10일 경우
# 수 입력 : 10
# num1 : 10 짝수다
# 나는 다음 문장

#=> 출력값
# -> 입력 값 5일 경우
# 수 입력 : 5
# 나는 다음 문장

# num1=int(input("수 입력 : "))
# if num1 % 2 == 0:
#     print("num1:",num1,"짝수다")
#     print("num1:",num1,"2의 배수이다")
# print("나는 다음 문장")

#=> 출력값
# 수 입력 : 10
# num1: 10 짝수다
# num1: 10 2의 배수이다
# 나는 다음 문장

# 수 입력 : 5
# 나는 다음 문장

# print("1.easy game")
# print("2.hard game")
# print("3.exit")
# num1=int(input("선택: "))
# if num1 == 1:
#     print("easy game start")
# if num1 == 2:
#     print("hard game start")
# if num1 == 4:
#     print("game exit")

# 단순 if문은 조건이 맞으면 모든것이 실행된다.

# 날짜를 입력받아 요일을 구하시오. 
# (단, 1일은 무조건 월요일이다. 7일은 일요일, 8일은 다시 월요일) 
# (어떤 값을 입력을 받던 요일이 정확히 출력 되게 만드시오

# num1=int(input("일자를 입력하세요."))
# if num1 % 7 == 0: print("월요일")
# if num1 % 7 == 0:  print("화요일")
# if num1 % 7 == 0:  print("수요일")
# if num1 % 7 == 0:  print("목요일")
# if num1 % 7 == 0:  print("금요일")
# if num1 % 7 == 0:  print("토요일")
# if num1 % 0 == 0:  print("일요일")

# if num1 // 1 == 1:
#     print("월요일")
# if num1 // 2 == 1:
#     print("화요일")
# if num1 // 3 == 1:
#     print("수요일")
# if num1 // 4 == 1:
#     print("목요일")
# if num1 // 5 == 1:
#     print("금요일")
# if num1 // 6 == 1:
#     print("토요일")
# if num1 // 7 == 1:
#     print("일요일")

###강사님 풀이
# day=int(input("날짜 입력 : "))
# if day%7 ==1 : print("월요일!!!")
# if day%7 ==2 : print("화요일!!!")
# if day%7 ==3 : print("수요일!!!")
# if day%7 ==4 : print("목요일!!!")
# if day%7 ==5 : print("금요일!!!")
# if day%7 ==6 : print("토요일!!!")
# if day%7 ==0 : print("일요일!!!")

# print("입력한 데이터가 3의 배수인 경우 출력하시오.")
# num=int(input("수 입력 :"))
# if num%3==0 : print(num)

# print("\n절대값을 구하는 프로그램을 작성하시오.")
# num=int(input("수를 입력하세요."))
# if num>=0 : print(num)
# if num<0 : print(num*-1)

# print("\n수를 입력 받아 짝,홀수를 구분하여 출력하시오.")
# num=int(input("수 입력 :"))
# if num%2==0 : print("짝수")
# if num%2==1 : print("홀수")

# print("\n두수를 입력 받아 큰 수를 출력하시오.")
# num1=int(input("첫번째 수 : "))
# num2=int(input("두번째 수 : "))
# if num1>num2 : print(num1)
# if num1<num2 : print(num2)

# print("\n세수를 입력 받아 큰 수를 출력하시오.") 
# num1=int(input("첫번째 수 : "))
# num2=int(input("두번째 수 : "))
# num3=int(input("세번째 수 : "))
# if (num1>num2)and(num1>num3): print(num1)
# if (num2>num3)and(num2>num3): print(num2)
# if (num3>num1)and(num3>num2): print(num3)

# print("\n두수를 입력 받아 큰 수가 짝수이면 출력하시오.")
# num1=int(input("첫번째 수 : "))
# num2=int(input("두번째 수 : "))
# if num1>num2 : 
#     if num1%2==0 : print(num1) 
# if num1<num2 :
#     if num2%2==0 : print(num2)

# print("\n두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.")
# num1=int(input("첫번째 수 : "))
# num2=int(input("두번째 수 : "))
# sum=num1+num2
# if sum%2==0 : 
#     if sum%3==0 :print(sum)

##강사님 풀이
# #입력한 데이터가 3의 배수인 경우 출력하시오.
# num1= int(input("정수 입력 : "))
# if num1%3 == 0 :
# print("%d는 3의 배수이다"%num1)
# # 절대값을 구하는 프로그램을 작성하시오.
# num1= int(input("정수 입력 : "))
# if num1 < 0 :
# num1*=-1
# print("절대값 : %d"%num1)
# #수를 입력 받아 짝,홀수를 구분하여 출력하시오.
# num1= int(input("정수 입력 : "))
# if num1 %2 == 0 :
#   print("%d는 짝수다"%num1)
# # if num1 %2 :
# # print("%d는 홀수다"%num)
# if num1 %2!=0 :
#   print("%d는 홀수다"%num1)
# # 두수를 입력 받아 큰 수를 출력하시오.
# num1= int(input("정수1 입력 : "))
# num2= int(input("정수2 입력 : "))
# if num1 > num2 :
#   print("%d가 큰수이다"%num1)
# if num2 > num1 :
#   print("%d가 큰수이다"%num2)

# 세수를 입력 받아 큰 수를 출력하시오.

# num1= int(input("정수1 입력 : "))
# num2= int(input("정수2 입력 : "))
# num3= int(input("정수3 입력 : "))
# #알고리즘
# if num1 < num2 :
#     num1 = num2
# if num1 < num3 :
#     num1 = num3
# print("%d가 가장 큰수이다"%num1)

# if num1 > num2 and num1 > num3 :
#     print("%d가 큰수이다"%num1)
# if num2 > num1 and num2 > num3 :
#     print("%d가 큰수이다"%num2)
# if num3 > num1 and num3 > num2 :
#     print("%d가 큰수이다"%num3)

# # 두수를 입력 받아 큰 수가 짝수이면 출력하시오.
# num1= int(input("정수1 입력 : "))
# num2= int(input("정수2 입력 : "))
# if num1 > num2 and num1 %2== 0 :
#   print("%d가 큰수이며 짝수이다"%num1)
# if num2 > num1 and num2 %2== 0 :
#   print("%d가 큰수이며 짝수이다"%num2)

# # 두수를 입력 받아 합이 짝수이고 3의 배수인 수를 출력하시오.
# num1= int(input("정수1 입력 : "))
# num2= int(input("정수2 입력 : "))
# sum_= num1 + num2
# if sum_%2== 0 and sum_%3== 0 :
# print("두수의 합은 %d이고 짝수이며 3의 배수이다"%sum_)