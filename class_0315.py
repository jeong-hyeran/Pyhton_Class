# 전동 자전거로 100m를 가는데 11.27초가 걸린다면 
# 1시간 후 몇 km를 갈 수 있을까?(소수점 2자리까지만 표기하시오)

# second=3600
# # meter100=11.27
# # second_1=(round((100/11.27),2))
# second_1=100/11.27
# hour_1=(second*second_1)
# km=hour_1/1000
# print("1시간 후 이동한 거리는 %skm이다."%(round(km,2)))

# _1hour_sec=3600
# _1sec_meter=100/11.27
# _1hour=(_1hour_sec*_1sec_meter)
# km_1=_1hour/1000
# print("1시간 후 이동한 거리는 %skm이다."%(round(km_1,2)))

#강사님 풀이
# time=60*60 # 한시간을 초단위로 변환
# cnt=time/11.27 # 한시간에 11.27초가 몇번 진행되는지 확인
# meter=cnt*100 #11.27초마다 100m진행하니깐 위의 결과에 100을 곱하면 총거리가 나옴
# kilo=meter/1000 #단위를 km로 변환
# print("한시간뒤 총 이동거리 :",round(kilo,2),"Km")

# flt = 123.123 
# print("%.3f + %.3f = %.3f" % (flt,321.321,flt+321.321)) 
# print(flt,"+",321.321,"=",flt+321.321) 

# # =>출력값
# # 123.123 + 321.321 = 444.444
# # 123.123 + 321.321 = 444.444

# ch1,ch2 ,ch3= "파",'2',"썬" 
# print("%c + %c + %c = %s"%(ch1,ch2,ch3,ch1+ch2+ch3)) 
# print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3) 

# # =>출력값
# # 파 + 2 + 썬 = 파2썬
# # 파 + 2 + 썬 = 파2썬

# str_1 = "python "; str_2 = "test" 
# str_3 = str_1 + str_2 
# print("%s + %s = %s" % (str_1,str_2,str_1+str_2)) 
# print(str_1,"+",str_2,"=",str_1+str_2)

# # =>출력값
# # python  + test = python test
# # python  + test = python test

# 피연산자 + 피연산자 에서 +연산자의 연산속성
# 숫자(정수,실수) + 숫자(정수,실수)는 흔히 잘알고 있는 덧셈 연산
# 시퀀스형 자료형 + 시퀀스형 자료형 은 둘을 하난로 합티는 업데이트 연산이진행
# 단, 좌, 우의 피연산자들이 유형이 같아야 합니다.
# 숫자는 좌, 우 유형이 달라도 덧셈연산이 되지만
# 시퀀스형 자료형들은 좌, 우 유형이 다르면 연산이 되지 않습니다.
# 시퀀스형 자료형이란 ? 순서가 존재하면, 인덱스라는 보조첨자를 쓰는 자료형
# 시퀀스 자료형 => list(리스트), tuple(튜플), 문자열

# 변수의 자료형 확인 
# <class ‘int’>    정수형 
# <class ‘float’>  실수형
# <class ‘str’>    문자열
# <class ‘bool’>   블형(참과 거짓으로 표현)

# A=10 
# B=5 
# print("type :",type(A<B));print("type :",(A<B)) 
# num = 100;print("type : %s" % type(num)) 
# flt = 321.321;print("type : %s" % type(flt)) 
# ch = "A ";print("type : %s" % type(ch)) 
# st = "test";print("type : %s" % type(st)) 
# # type : 자료형을 보여주는 함수

# =>출력값
# type : <class 'bool'>
# type : False
# type : <class 'int'>
# type : <class 'float'>
# type : <class 'str'>
# type : <class 'str'>

# num = 100
# print("type : %s\tid : %s" % (type(num),id(num)))
# num = 321.321 
# print("type : %s\tid : %s" % (type(num),id(num))) 
# num = "A" 
# print("type : %s\tid : %s" % (type(num),id(num))) 
# num = "test" 
# print("type : %s\tid : %s" % (type(num),id(num))) 

#id함수는? 주소를 알려주는 함수

# =>출력값
# type : <class 'int'>    id : 140728845131904
# type : <class 'float'>  id : 2578590445856
# type : <class 'str'>    id : 2578592186752
# type : <class 'str'>    id : 2578592186864

# C언어는 프로그램이 시작과 동시에 변수의 속성을 지정해서 메모리공간에 할당부터
# 받으며 그 위치나 속성이 바뀌지 않는다.
# 하지만 파이썬에서는 대입되면서 변수의 속성과 위치가 정해진다.(메니지드언어인 파이썬)

# st1 = "Python" 
# st2 = "Test" 
# su = 100 #숫자의 속성
# flt = 1.11 #숫자의 속성

# num = '100' #문자형

# print(flt+su) 
# print(st1 + st2) #시퀀스로 좌우 순서대로 업그레이드
 #print(su+num) -> 요아이는 숫자형과 문자형의 연산이라 에러뜬다.

# => 출력값 
# 101.11
# PythonTest

# su = 100 
# print('type(su) : ',type(su)) 
# print('type(str(su)) : ',type(str(su))) 
# print('type(float(su)) : ',type(float(su)))
# print('type(su) : ',type(su)) 

#강제 형 변환 ??? 히이히이하ㅓ이ㅏ허ㅣ아ㅓㅎ힝
# =>출력값
# type(su) :  <class 'int'>
# type(str(su)) :  <class 'str'>
# type(float(su)) :  <class 'float'>
# type(su) :  <class 'int'>
# 숫자형을 문자열로 변환하는 건 문제가 안된다.
# 문자열로 숫자형으로 변환하는 건 문제가 된다.
# su = '100.1'
# print(int(su))
# 문자형에서 실수형으로 정수형으로 변경해야한다.

# su = 100 
# num = '100' 
# flt = "1.111" 
# 아래와 같이 출력 하시오.(각각의 값들은 하나씩만 사용할 것) 
# 200 
# 101.111 
# 100100

###***강사님 풀이 다시 보기!!!!!!!!!!!!!!
# su = 100 
# num = '100' 
# flt = "1.111"

# print(su+(int(num)))
# print(su+float(flt))
# print(str(su)+num)

##[입력함수]

# print("숫자 입력")
# num1 = input()
# print("입력 받은 값 :",num1)

#입력함수를 만나는 순간 프로그램이 멈추고 대기하고 있다.
#어떠한 값을 넣고 엔터를 치는 순간 

# Quiz 
# ❖ 아래와 같이 실행되게 만드시오. 
# 출력 : 이름 입력 
# 입력 : 홍길동 
# 출력 : 나이 입력 
# 입력 : 20 
# 결과 출력 : 홍길동 님의 나이는 20 살 입니다

# print("이름 입력")
# num=input()
# print("나이 입력")
# age=input()
# #print(num"님의 나이는" age"살 입니다.")
# print("%s님의 나이는 %s살 입니다."%(num,age))

# print("이름 입력 : ")
# name=input()
# print("나이 입력 : ")
# age=input()
# print(name,"님의 나이는" ,age,"살 입니다.")
# print("%s님의 나이는 %s살 입니다."%(name,age))

# print("두 수의 합을 구해 줍니다") 
# print("두 수 입력") 

# num1 = input() 
# num2 = input() 
# num3 = num1 + num2 
# print("두 수의 합 ", num1,"+",num2,'=',num3) 

# print("num1 type : ",type(num1)) 
# print("num2 type : ",type(num2)) 
# print("num3 type : ",type(num3))

# => 출력값
# 두 수의 합을 구해 줍니다
# 두 수 입력
# 1
# 2
# 두 수의 합  1 + 2 = 12
# num1 type :  <class 'str'>
# num2 type :  <class 'str'>
# num3 type :  <class 'str'>
## 입력함수는 문자형으로만 인식하는가?
## 입력함수로 입력하것은 (제일 에러가 없는)문자열로 입력이 된다!

# print("두 수의 합을 구해 줍니다") 
# print("두 수 입력")
# num1 = input() 
# num2 = input() 
# num3 = int(num1) + int(num2) 
# print("두 수의 합 ", num1,"+",num2,'=',num3) 

# print("num1 type : ",type(num1)) 
# print("num2 type : ",type(num2)) 
# print("num3 type : ",type(num3))

# num1 = int(input()) 
# num2 = int(input()) 
# result = num1 + num2 

# print(num1, "+", num2, "=", result)  

# result = num1 - num2 
# print(num1, "-", num2, "=", result) 

# result = num1 * num2 
# print(num1, "*", num2, "=", result)

# result = num1 / num2 
# print(num1, "/", num2, "=", result) 

# print("문자열 입력")
# name=input()
# print("정수 입력")
# age=int(input())
# print("실수 입력")
# flt=float(input())

# print("name 값:", name, "\t type: ", type(name))
# print("age 값:",age,"\t type :", type(age))
# print("flt 값 :",flt,"\t type:",type(flt))

# #데이터를 입력 받을때 정확하게 입력받을 수 있도록 정확히 작성해야한다.
# #에러유형을 눈여겨 봐두면 좋다.
 
# name=input("이름을 입력 하세요: ")
# age=int(input("나이를 입력하세요: "))
# addr=input("주소를 입력 하세요 :")
# print("이름 : ", name,"\n나이 : ",age,"\n주소 : ", addr)
###
# name=input("이 안에는 정수 실수 함수 모든게 올 수 있지만 단 하나만 와야 한다.")





# Quiz 
# 올해 년도와 태어난 년도를 구하여 나이를 계산하는 프로그램을 코딩하시오 
# 올해의 년도를 4자리로 입력하세요? 
# 당신이 태어난 년도를 4자리로 입력하세요? 
# 당신의 나이는 ?? 살 입니다.


# print("올해의 년도를 4자리로 입력하시오.")
# input(int())
# print("당신이 태어난 년도를 4자리로 입력하시오.")
# input(int())
# # year1=input
# # year2=input
# # # print("당신의 나이는 age살 입니다.")

# now_year=int(input("올해의 년도 입려 [4자리] : "))
# birth_year=int(input("태어난 년도 입려 [4자리] : "))
# age=now_year-birth_year+1
# print("당신의 나이는 %d살 입니다."%age)



# year1=(print("올해의 년도를 4자리로 입력하시오.",int(input())))
# year2=(print("당신이 태어난 년도를 4자리로 입력하시오.",int(input())))
# age=year2-year1
# print("당신의 나이는 age살 입니다.")

# year1=int(input("올해의 년도 입력 [4자리]"))
# year2=int(input("태어난 년도 입력 [4자리]"))
# age=year1-year2+1
# print("당신의 나이는 %d입니다."%age)