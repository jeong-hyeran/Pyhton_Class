# PYTHON_PROGRAMMING 변수
# 변 수 
# ❖ 변수란? 
# -. 한가지 값으로 고정되지 않고 여러 가지 값으로 변할 수 있는 공간
# -> 데이터를 사용하기 위해 메모리에 공간을 할당 받는데 할당 받은 공간에 
#이름을 정해 두고 원할 때 꺼내 쓰거나, 변경 할 수 있음

# 변수명 작명 규칙 
# ❖ 변수의 이름은 알파벳, 숫자, 언더바(_)로 구성 
# ❖ 대소문자 구분 
# ❖ 변수의 이름은 숫자로 시작할 수 없음 
# ❖ 키워드(예약어)는 변수이름으로 사용 불가능 
# ❖ 공백이나 특수 기호는 포함될 수 없음 
# ❖ 예약어 
# ❖ 프로그래밍 언어 중에서 의미가 고정되어 있고, 
#사용자가 작성하는 프로그램 상태에 따라서 의미를 변경할 수 없는 단어
# 예 제 
# num = 100 
# print("정수 형 변수 사용 : %d" % num) print("정수 형 변수 사용 : ",num)
# 예 제 
# num = 5 
# print("변경 전 num : ",num) num = num + 10 
# print("변경 후 num : ",num)
# 예 제 
# num1=5; 
# num2=10; 
# sum = num1 + num2 print("두 수의 합 : ",sum)
# 예 제 
# num1 = 5 
# num2 = 10 
# sum_ = num1+num2 
# print("id num1 : ",id(num1)) print("id num2 : ",id(num2)) print("id sum : ",id(sum_))
# Quiz 
# ❖ 다음과 같은 결과가 나오도록 코딩하시오 ▪ 
#num1(10) + num2(20) = 30
# Quiz 
# num1=7 
# num2=5 
# 위 값의 연산 결과를 각각의 변수에 저장 후 출력 하시오. ( + , - , * , / )
# Quiz 
# ❖ 다음과 같이 나오도록 코딩하시오.(단, 변수를 사용하시오) ▪ 파이썬 100점 
# ❖ 다음과 같이 나오도록 코딩하시오.(단, 변수를 사용하시오) ▪ 나는 27살이다. 
# ❖ 파이썬, C언어, Java 3과목의 점수를 입력하고 합계와 평균을 구하는 
#프로그램을 작성하시오. (평균 소수점 2자리 까지) 
# Quiz 
# ❖ 당신은 놀이공원을 가기 위해 11개의 지하철 역을 지나왔다.  
#출발 역에서 도착역까지 37분이 걸렸다면 
# 한 역을 지나는데 걸리는 시간은 얼마인가? 
# (소수점 2자리 까지 출력)
# 예 제 
# flt = 123.567 
# print("round(flt) : " , round(flt)) print("round(flt,1)" , round(flt,1)) print("round(flt,2) : " , round(flt,2))
# Quiz 
# ❖ 호텔 한 층의 높이는 260cm이다. 총 14개의 층을 쓰고 있으며 1층은 500.23cm라면 이 건물의 높이는 총 몇 m인가? 
#(단, 소수점 3자리까지만 출력하시오.)
# Quiz 
# ❖ 전동 자전거로 100m를 가는데 11.27초가 걸린다면 1시간 후 몇 km를 갈 수 있을까?(소수점 2자리까지만 표기하시오)
# 예 제 
# flt = 123.123 
# print("%.3f + %.3f = %.3f" % (flt,321.321,flt+321.321)) print(flt,"+",321.321,"=",flt+321.321) 
# ch1,ch2 ,ch3= "파",'2',"썬" 
# print("%c + %c + %c = %s"%(ch1,ch2,ch3,ch1+ch2+ch3)) print(ch1,"+",ch2,"+",ch3,"=",ch1+ch2+ch3) 
# str_1 = "python "; str_2 = "test" 
# str_3 = str_1 + str_2 
# print("%s + %s = %s" % (str_1,str_2,str_1+str_2)) print(str_1,"+",str_2,"=",str_1+str_2)
# type 
# ❖ 변수의 자료형 확인 
# <class ‘int’> 
# <class ‘float’> 
# 정수형 
# 실수형
# <class ‘str’> 
# 문자열
# <class ‘bool’> 
# 블형



# A=10 
# B=5 
# print("type :",type(A<B));print("type :",(A<B)) 
# num = 100;print("type : %s" % type(num)) 
# flt = 321.321;print("type : %s" % type(flt)) 
# ch = "A ";print("type : %s" % type(ch)) 
# st = "test";print("type : %s" % type(st)) 
# type 
# num = 100 
# print("type : %s\tid : %s" % (type(num),id(num))) num = 321.321 
# print("type : %s\tid : %s" % (type(num),id(num))) num = "A" 
# print("type : %s\tid : %s" % (type(num),id(num))) num = "test" 
# print("type : %s\tid : %s" % (type(num),id(num))) 
# type 
# st1 = "Python" st2 = "Test" 
# su = 100 
# flt = 1.11 
# num = '100' 
# print(flt+su) 
# print(st1 + st2) #print(su+num)
# type 
# su = 100 
# print('type(su) : ',type(su)) 
# print('type(str(su)) : ',type(str(su))) print('type(float(su)) : ',type(float(su)))
# Quiz 
# su = 100 
# num = '100' 
# flt = "1.111" 
# ❖ 아래와 같이 출력 하시오.(각각의 값들은 하나씩만 사용할 것) 200 
# 101.111 
# 100100
