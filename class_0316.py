# year1=input("태어난 년도를 입력하세요.[4자리]",int())
# year2=input("올해 년도를 입력하세요.[4자리]",int())
# age=year2-year1+1
# print("당신의 나이는 %s살 입니다."% age)


# Quiz 
# ❖ 600kg제한의 화물용 엘리베이터가 있다. 2개의 물건에 대한 무게를 실수로 입 력 받아 현재 엘리베이터에 더 적재할 수 있는 무게를 구하시오 
# 첫 번째 물건의 무게를 입력하시오? 64.27 
# 두 번째 물건의 무게를 입력하시오? 75.25 
# 현재 엘리베이터에 허용무게는 460.48kg 입니다.

# max=600
# first=64.27
# second=75.25
# now=460.48
# sum=first+second
# print("현재 더 적재할 수 있는 무게 :",float(max-sum),"kg")

#강사님 풀이
# first_weight= float(input("첫 번째 물건의 무게 입력 : "))
# second_weight= float(input("두 번째 물건의 무게 입력 : "))
# result_weight= 600 - (first_weight+second_weight)
# print("현재 엘리베이터에 허용무게는 %.2fkg 입니다"%result_weight)

# Quiz 
# ❖ 다음과 같은 방법으로 표준 체중을 구할 수 있다. 
# 표준체중 = (현재 키 - 100) x 0.9 
# 키를 입력하여 표준 체중을 구하시오 
# ❖ 아래와 같이 실행되게 만드시오 
# ❖ Ex> 키를 입력하세요? 182 
# 표준체중은 73.8 입니다.

# height=float(input("키를 입력하세요. : "))
# averang=(height-100)*0.9
# print("당신의 표준 체중은 %.1f입니다."% float(averang))

# #강사님 풀이
# height = float(input("현재 키 입력 : "))
# standard_weight= (height-100) * 0.9
# print("표준 체중은 %.1fkg 입니다"%standard_weight)

# Quiz 
# ❖ 비만도 비율은 다음과 같은 방법으로 구할 수 있다. 
# 비만도(%) = (현재체중 / 표준 체중) x 100 
# 현재 체중을 입력하고 1번에서 구한 표준 체중을 이용하여 비만도를 구하시오 
# ❖ Ex> 키를 입력하세요 ? 182 
# 현재 체중을 입력하세요? 81 
# 표준 체중은 73.8이고 비만도는 109.76입니다.

# weight=float(input("현재 체중을 입력 : "))
# height = float(input("현재 키 입력 : "))
# standard_weight= float((height-100) * 0.9)
# obesity=float((weight/standard_weight)*100)
# print("표준 체중은 %.1f이고 비만도는 %.2f%%입니다."% (standard_weight,obesity))

#강사님 풀이
# height = float(input("현재 키 입력 : "))
# weight = float(input("몸무게 입력 : "))
# standard_weight= (height-100) * 0.9
# bimando =weight/standard_weight *100
# print("표준 체중은 %.1fkg 이고 비만도는 %.2f%%입니다"% (standard_weight,bimando))

# Quiz 
# -. 학생 이름과 국어, 영어, 수학 점수를 입력 받아 출력하시오 
# <결과> 
# 학생 이름 : 김개똥 
# 국어 점수 : 1 
# 영어 점수 : 2 
# 수학 점수 : 2 
# =================학생 정보================== 
# 이름 국어 영어 수학 합계 평균 
# 김개똥 1 2 2 5 1.67

# name=input("학생 이름 : ")
# korean=int(input("국어 점수 : "))
# english=int(input("영어 점수 : "))
# math=int(input("수학 점수 : "))
# total=int(korean+english+math)
# averang=float(total/3)

# print("=============학생 정보=============")
# print("이름","국어","영어","수학","평균","합계")
# print(name,korean,english,math,round(averang,2),total)

# print("=============학생 정보=============")
# print("이름\t국어\t영어\t수학\t평균\t합계")
# print(name,korean,english,math,round(averang,2),total)

# print("=============학생 정보=============")
# print("%4s%4s%4s%4s%4s%4s"%("이름","국어","영어","수학","평균","합계"))
# print("%6s%6s%6s%6s%6s%6s"%(name,korean,english,math,averang,total))

# print("=================학생 정보=================")
# print("이름\t국어\t영어\t수학\t평균\t합계")
# print("%s\t%s\t%s\t%s\t%.2f\t%s\t"%(name,korean,english,math,averang,total))

#강사님 풀이
# name = input("학생 이름 : ")
# kor = int(input("국어 점수 : "))
# eng = int(input("영어 점수 : "))
# mat = int(input("수학 점수 : "))
# sum_=kor+eng+mat
# avg=sum_/3
# print("================= 학생 정보 =================")
# print("이름\t국어\t영어\t수학\t합계\t평균")
# print("%s\t%d\t%d\t%d\t%d\t%.2f"%(name,kor,eng,mat,sum_,avg))

# [연산자]

# num1 = 9; num2 = 2 
# print(num1 , " + " , num2 , " = " , num1 + num2) 
# print(num1 , " - " , num2 , " = " , num1 - num2) 
# print(num1 , " * " , num2 , " = " , num1 * num2) 
# print(num1 , " / " , num2 , " = " , num1 / num2) 
# print(num1 , " // " , num2 , " = " , num1 // num2) 
# print(num1 , " % " , num2 , " = " , num1 % num2) 
# print(num1 , " ** " , num2 , " = " , num1 ** num2)
# =>출력 값
# 9  +  2  =  11
# 9  -  2  =  7
# 9  *  2  =  18
# 9  /  2  =  4.5
# 9  //  2  =  4 나누기(몫만 표현) 
# 9  %  2  =  1 (나누고 나머지값)
# 9  **  2  =  81

# su1=3.1; su2=3 

# print("su1 >= su2 : ",(su1 >= su2)) 
# print("su1 <= su2 : ",(su1 <= su2)) 
# print("su1 == su2 : ",(su1 == su2)) 
# print("su1 != su2 : ",(su1 != su2))
##true,false 표현됨
# #=>출력값
# su1 >= su2 :  True
# su1 <= su2 :  False
# su1 == su2 :  False
# su1 != su2 :  True
### print(3==3)  =>그냥 프린트 함수에서조차 'true,false'로 표현
# su1=3.1; su2=3 
# print("su1 >= su2 : %s"%(su1 >= su2)) 
# print("su1 <= su2 : %s"%(su1 <= su2)) 
# print("su1 == su2 : %s"%(su1 == su2)) 
# print("su1 != su2 : %s"%(su1 != su2))
# #=> 출력값
# su1 >= su2 : True
# su1 <= su2 : False
# su1 == su2 : False
# su1 != su2 : True
#서식제어문이나 그냥이나 같다.
# su1=3.1; su2=3 
# print("su1 >= su2 : %d"%(su1 >= su2)) 
# print("su1 <= su2 : %d"%(su1 <= su2)) 
# print("su1 == su2 : %d"%(su1 == su2)) 
# print("su1 != su2 : %d"%(su1 != su2))
#=> 출력값
# su1 >= su2 : 1
# su1 <= su2 : 0
# su1 == su2 : 0
# su1 != su2 : 1
#모든것들은 다 참인데 숫자 0만 거짓이다.

# su1 = su2 = 5 
# su1+=1 
# print("su1 + 1 = " ,su1) #sul+1=6
# su1-=1 
# print("su1 - 1 = ",su1)  #sul-1=4 
# #위에 (print("su1 + 1 = " ,su1)) 값을 끌고 와야한다.
# su1*=su2 
# print("su1 * su2 = ",su1) #sul1*sul2=25
# su1//=su2 
# print("su1 // su2 = ",su1) #sul1//sul2=1
# su1%=su2 
# print("su1 % su2 = ",su1) #sul1%sul2=0
#=> 출력값
# su1 + 1 =  6
# su1 - 1 =  5
# su1 * su2 =  25
# su1 // su2 =  5
# su1 % su2 =  0

# su1 = 5 
# su2 = 3 
# su1**=su2 #5의 3제곱은 125
# su1-=2 #125-2=123
# print("su1 / 4 = ",su1 / 4) #su1 / 4 = 123/4 = 30.75
# print("su1 // 4 = ",su1 // 4) #su1 // 4 = 30
# print("su1 % 4 = ",su1 % 4) #su1 % 4 = 75
#=> 출력값
# su1 / 4 =  30.75
# su1 // 4 =  30
# su1 % 4 =  3(이거는 왜 다를까..나머지값이라서.. 3.. 소숫점 뒷자리가 아니댜아아 )

# print(0 or 0," : ",False or False) 
# print(1 or 0," : ",True or False) 
# print(0 or 1," : ",False or True) 
# print(1 or 1," : ",True or True) 
# print("not : ",not(0 or 0)," : ",not(False or False)) 
# print("not : ",not(1 or 1)," : ",not(True or True))
# => 출력값
# 0  :  False
# 1  :  True
# 1  :  True
# 1  :  True
# not :  True  :  True
# not :  False  :  False

# print(0 and 0," : ",False and False) 
# print(1 and 0," : ",True and False) 
# print(0 and 1," : ",False and True) 
# print(1 and 1," : ",True and True) 
# print("not : ",not 0," : ",not False) 
# print("not : ",not 1," : ",not True)
# # => 출력값
# 0  :  False
# 0  :  False
# 0  :  False
# 1  :  True
# not :  True  :  True
# not :  False  :  False

# a=20
# b=10
# print(False or(a+b))
# print(True or(a+b))
# print(False and(a+b))
# print(True and(a+b))
# #=> 출력값
# 30(or 연산자부터 앞에 False가 오면 뒤에를 봐야한다.)
# True(or 연산자부터 앞에 true가 오면 뒤에를 볼필요가 없다..)
# False
# 30
# 정수값은 그대로 출력된다.

# |->버티컬 라인이라 함,\기호에 함께 있는것
#
# ^