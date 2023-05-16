# def cal(su1,op,su2):
#     result=0
#     result = su1+su2
#     print('cal 실행')
#     return result # return은 함수를 종료하는 키워드, 함수호출한곳으로 특정값을
#                   # 반환시키기도 함
#     # return 0 #으로 넣으면 실해값이 0으로 나옴
# su1,op,su2 = int(input("숫자 : ")), input("부호 : " ), int(input("숫자 : "))
# result = cal(su1,op,su2)
# print(su1,'+',su2,'=',result)
# print("다음 문장 실행")

# def showAvrg(a,b,c):
#     print("{}와 {}의 평균".format(a,b))
#     print("값은 {}입니다.".format(round(c,1)))
# def avrg(j,k):
#     total=j+k
#     f=total/2
#     return f;

# i=2;j=3
# f=avrg(i,j)
# showAvrg(i,j,f)
# print("다음 문장 실행")

#함수의 순서는 상관없댜!
# 함수를 정의하는 건 순서 상관없지만
# 함수를 호출 하는 것은 순서를 신경써야 한다.

# def func2(a,b):
#     a+=5;b*=10;
#     print("func2:a={},b={}".format(a,b))
# def func1():
#     a=5;b=10
#     func2(a,b)
#     print("func1 : a={}, b={}".format(a,b))
# func1()

# def aa(a):
#     if a == 1:
#         print('1입력')
#     print('다음 문장 실행')
# a=aa(1)
# print("리턴 값 : ",a)
# print("프로그램 종료")

#출력 값
# 1입력
# 다음 문장 실행
# 리턴 값 :  None
# 프로그램 종료

# def aa(a):
#     if a == 1:
#         return # 리턴을 만나는 순간 함수는 종료가 된다.
#         print('1입력')
#     print('다음 문장 실행')
# a=aa(1)
# print("리턴 값 : ",a)
# print("프로그램 종료")


# #출력 값
# 리턴 값 :  None
# 프로그램 종료

# def move():
#     print('이동')
# def attack():
#     print('공격')
# def defense():
#     print('방어')
# move()
# attack()
# defense()

#출력값
# 이동
# 공격
# 방어

# def move():
#     pass
# def attack():
#          pass
# def defense():
#               pass
# move()
# attack()
# defense()
# pass는 반복문, 종속문 등등 아직 기술 하기 힘들때 사용 할 수 있다.

# def func1() : 
#     a=100 
#     print("func1의 a : %d" % a) 
# def func2() : 
#     a=200 
#     print("func2의 a : %d" % a) 
# func1() 
# func2()

#출력값
# func1의 a : 100
# func2의 a : 200

# def func1() : 
#     print("func1의 a : %d" % a) 
# def func2() : 
#     print("func2의 a : %d" % a) 
    
# a =200 #전역 변수 
# # 모든 함수에 영향을 줄 수 있는 함수
# 함수 밖에서 설정하는 함수를 전역 변수라 한다.
# func1() 
# func2()

# 출력값
# func1의 a : 200
# func2의 a : 200

# def func1() : 
#     a = 123 
#     print("func1의 a : %d" % a) 
# def func2() : 
#     print("func2의 a : %d" % a) 
# a =200 #전역 변수 
# func1() 
# func2()
# #함수안에 있는 변수(지역변수)가 우선권을 가지고 이싿.?

# 출력값
# func1의 a : 123
# func2의 a : 200

# def func1() : 
#     global a #전역변수를 그대로 쓰겠다는 키워드
#     a = 1222 
#     print("func1의 a : %d" % a) 
# def func2() : 
#     print("func2의 a : %d" % a) 
# a =200 #전역 변수 
# func1() 
# func2()

# 출력값
# func1의 a : 1222
# func2의 a : 1222

# num = 10 
# sum=0 
# def display(): 
#     sumFunc() 
#     print("10까지의 합 :" , sum) 
# def sumFunc() : 
#     global sum 
#     for i in range(num+1): 
#         sum+=i 
# display()
#전역변수 지역 변수를 써야 할때를 구분해야한다.
# 지역변수를 더 많이 쓰는것이 프로그래밍 할때 좋댜
# 전역변수는 메모리를 많이 사용한다.


# 출력값
# 10까지의 합 : 55

# def sum_func(x1,x2,x3 = 100) : 
#     result = 0 
#     result =x1 + x2 + x3 
#     return result 
# def display(): 
#     Sum = 0 
#     a,b,c = 10 , 20 , 30 
#     Sum = sum_func(a , b) 
#     print("매개변수 2개 함수 호출 : " , Sum) 
#     Sum = sum_func(a ,b , c) 
#     print("매개변수 3개 함수 호출 : " , Sum) 
# display()
# 디폴드 파라미터(기본 매개변수)
# 직접전달 하는 정수가 먼저됨..

# 출력값
# 매개변수 2개 함수 호출 :  130
# 매개변수 3개 함수 호출 :  60

# def alba(day=30,time=8,won=8500): #디폴트 매개변수
#     result = day * time * won 
#     return result 
# def display(): 
#     num = int(input('1.기본급\n2.일한 날짜 입력\n')) 
#     if num == 1: 
#         result = alba() 
#     elif num==2: 
#         day = int(input('일한 날짜 입력(몇일) : ')) 
#         result=alba(day) 
#     print("당신의 급여 :{}원 입니다".format(result)) 
# display()

# def sum_func(*par) : 
#     result = 0 
#     print("type : ",type(par)) 
#     print("par : ",par) 
#     for num in par : 
#         result = result + num 
#         print("num : %d" % num) 
#     return result 
# Sum = 0 
# Sum = sum_func(10 , 20) 
# print("매개변수 2개 함수 : %d" % Sum) 
# Sum = sum_func(10 , 20 , 30 , 40) 
# print("매개변수 4개 함수 : %d" % Sum)

#가변길이 매개변수
# 출력값
# type :  <class 'tuple'>
# par :  (10, 20)
# num : 10
# num : 20
# 매개변수 2개 함수 : 30
# type :  <class 'tuple'>
# par :  (10, 20, 30, 40)
# num : 10
# num : 20
# num : 30
# num : 40
# 매개변수 4개 함수 : 100

# def dic_func(**par) : 
#     print("type(par):",type(par)) 
#     for k in par.keys() : 
#         print("{} : {} 명입니다".format(k , par[k])) 

# dic_func(똭뚝뽹 = 123 , 꿔익꿔익 = 8 , test = '테스뚜')
#인수를 던져줄때 대입연산식으로 던져준다.
# 그럼 딕셔너리로 받아준다.

#출력값 
# type(par): <class 'dict'>
# 똭뚝뽹 : 123 명입니다
# 꿔익꿔익 : 8 명입니다
# test : 테스뚜 명입니다

# def change(a,b,c): 
#     return a+10,b+20,c+30 

# a,b,c=change(10,20,30) 
# d = change(10,20,30) 
# print("a,b,c :",a,b,c) 
# print("d:{}, type{}".format(d,type(d)))
#리턴값을 튜플이라는 자료형으로 전달 할 수 있다.

#출력값 
# a,b,c : 20 40 60
# d:(20, 40, 60), type<class 'tuple'>

# def swap(x,y): 
#     return y,x 
# a=10; b=20 
# print("바꾸기 전 : ",a,b) 
# a,b=swap(a,b) 
# print("바꾼 후 : ",a,b)

# 출력값
# 바꾸기 전 :  10 20
# 바꾼 후 :  20 10

# swap = lambda a,b:[b,a] 
# a=swap(10,20) 
# print("swap 결과",a)
# 람다함수는 한줄에 간단히 표현되면서 자주 사용할 필요가 없는
# 1회성 함수에 많이 사용 되어지는 문법이다.

# # 출력값
# swap 결과 [20, 10]

# lam = lambda a:a*10 
# hap = lambda a,b:a+b 
# noData = lambda : print("인자값 없는 람다") 

# print(lam(10)) 
# print(hap(5,10)) 
# noData()

# 출력값
# 100
# 15
# 인자값 없는 람다

# def startGame(): 
#     print("Game Start!!!!") 
# def test(): 
#     print("1.게임 시작") 
#     print("2.게임 종료") 
#     num = input("선택 : ") 
#     if num=="1": 
#         startGame() 
#     elif num=="2": 
#         end() 
# end = lambda :print("게임 종료") 
# test()

# 예외처리[try ~except) 
# n1= 10 
# n2=0 
# try: 
#     result=n1/n2 
#     print("%d / %d = %d" %(n1,n2,result)) 
# except: 
##에러가 날 것 같은 부분에 익셉트를 실행,여기는 절대 에러가 있으면 안됨
#     print("0으로 나눌 수 없습니다.") 
# print("프로그램 정상 종료!!")

# 출력값
# 0으로 나눌 수 없습니다.
# 프로그램 정상 종료!!

# while True: 
#     try : 
#         n1= int(input('정수1: ')) 
#         n2= int(input('정수2: ')) 
#         break 
#     except: 
#         print('숫자로만 입력하세요~') 
#     # print('%d / %d = %d'%(n1,n2,result)) 
# try: 
#     result=n1/n2 
#     print('%d / %d = %d'%(n1,n2,result)) 
# except: 
#     print('0으로 나눌 수 없습니다.') 
# print('프로그램 정상 종료!!')

# s = input('정수: ') 
# try :  
#     point = int(s) 
#     print(150 /point) 
# except ValueError: #익센트 유형
#     print('숫자로만 입력하세요~') 
# except ZeroDivisionError: #익센트 유형
#     print('0으로 나눌 수 없습니다.') 
# except: #전혀 생각할 수 없는 오류일 경우를 대비해서 만들어둠
#     print('알수 없는 오류 발생. 점검 후 조치하겠습니다..') 
# print('프로그램 정상 종료!')
# #에러 유형이 있으니 봐야한다.
# # 에러 유형에 따라 안내 문구를 출력해준다.

# pet = ['거북이', '타란튤라','전갈'] 
# for i in range(4): 
#     try:  
#         print(pet[i],'키울래용!') 
#     except: 
#         print('애완동물의 정보가 없습니다.') 
#     finally:#예외처리(에러)와 상관없이 꼭 실행되야 하는경우 
#         print('애완동물 넘 조아~~') 
# print('프로그램 정상 종료!')

# 출력값
# 거북이 키울래용!
# 애완동물 넘 조아~~
# 타란튤라 키울래용!
# 애완동물 넘 조아~~
# 전갈 키울래용!
# 애완동물 넘 조아~~
# 애완동물의 정보가 없습니다.
# 애완동물 넘 조아~~
# 프로그램 정상 종료!


# 모듈

# import math 
# print(math.pi)  
# print(math.factorial(5)) # 5!= 5x4x3x2x1  
# print(math.sqrt(5))  #루트를 표현
# print(math.log10(2)) 
# #어느 모듈에 있는지 출처를 밝혀야한다.!

# 출력값
# 3.141592653589793
# 120
# 2.23606797749979
# 0.3010299956639812

# from math import factorial, sqrt, pi    

# print(factorial(5))  
# print(sqrt(5))  
# print(log10(2))  

#출력값
# 120
# 2.23606797749979
# Traceback (most recent call last):
#   File "E:\3월 평일 0308 파이썬 기초_정혜란\class_0403.py", line 387, in <module>
#     print(log10(2))
# NameError: name 'log10' is not defined

# from math import factorial, sqrt, pi  
# import math  
  
# print(factorial(5))  
# print(sqrt(5))  
# print(math.log10(2))  
# print(math.log10(3))  
# print(math.gcd(12,18)) #최대공약수 

# 쓰겠다하는 함수나, 모듈은 순서가 중요하지 않다.
# 혹시나 사용할 문법은 모듈로 불러온다.