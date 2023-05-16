# st = """ 
# 김개똥 -2017년 03월 24일 
# 홍길동구리 -2015년 04월 02일 
# 선우선녀 -2018년 05월14일 
# """ 
# ❖ 위의 내용을 아래와 같이 변경 하시오 
# ❖ – (바) : (콜론으로 변경), 년도를 1999년으로 모두 변경 
# 김개똥 :1999년 03월 24일 
# 홍길동구리 :1999년 04월 02일 
# 선우선녀 :1999년 05월14일

# st = """
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월14일
# """
# st=st.replace('-',':')
# lo=0
# while True :
#     lo=st.find("년",lo)
#     if lo != -1 :
#         st=st.replace(st[lo-4:lo],'1999')
#         lo+=1
#     else :
#         break
# print(st)

# st = """
# 김개똥 -2017년 03월 24일
# 홍길동구리 -2015년 04월 02일
# 선우선녀 -2018년 05월14일
# """
# st=st.replace('-',':')
# lo=0
# while True :
#     lo=st.find(":",lo)
#     if lo != -1 :
#         st=st.replace(st[lo+1:lo+5],'1999')
#         lo+=1
#     else :
#         break
# print(st)

# 문자열 함수 
# 문자열 변경
# 함 수         설 명        사용법 
# split() 문자 열을 공백이나 다른 문자로 분리해서 리스트를 반환 Str.split() or Str.split(‘문자’) 
# splitlines() 행 단위로 분리(\n을 기준으로 나눈다) Str.splitlines()
# join 기존의 문자열 과 새 문자열 합해줌 Str.join(‘문자’) 

# st = 'never ever give up'
# print('st\t\t:' , st)
# print('st.split()\t:',st.split())
# # split()->공백을 나눔

# =>출력값
# st              : never ever give up
# st.split()      : ['never', 'ever', 'give', 'up']
# split() 문자 열을 공백이나 다른 문자로 분리해서 리스트를 반환

# st = '하나 : 둘 : 셋'
# print('st\t\t: ', st)
# print('st.split(:)\t: ',st.split(':')) #=>공백까지 나눠줌
# st = '하나:둘:셋'
# print('st\t\t: ', st)
# print('st.split(:)\t: ',st.split(':'))
# st = '일,이,삼' 
# print('st.split(,)\t: ',st.split(',')) #=>없는 구성요소로 지정하면 에러가 뜨는게 아니고 분할이 안되고 하나로 나옴

# # =>출력값
# st              :  하나:둘:셋
# st.split(:)     :  ['하나', '둘', '셋']
# st.split(,)     :  ['일', '이', '삼']

# st = 'never ever give up'
# print('st: ' ,st)
# print('st.splitlines():',st.splitlines())
# st="""      
# Never ever give up
# Never ever give up
# """
# ##\n이 포함 되어있어서 splitlines로 나눠준다.
# print('st,splitlines(): ',st.splitlines())
# st="하나\n둘셋"
# print('st.splitlines():',st.splitlines())
# 행 단위로 분리(\n을 기준으로 나눈다)
# =>출력 값
# st:  never ever give up
# st.splitlines(): ['never ever give up']
# st,splitlines():  ['', 'Never ever give up', 'Never ever give up']
# st.splitlines(): ['하나', '둘셋']

# Str = '123'
# print('"%".join(123)\t:','%'.join(Str))
# print('123.join("%a")\t:',Str.join('%a'))\
# #join 앞의 자료를 뒤에 붙히는것이 아니다.!
# # B.join(A)
# # 구성요소 사이사이에다가 A 구성요소 사이사이에 B를 넣는것이다.
# li=['','123','456']
# print('"공백". join([123,456]\t:',"".join(li))
# li=['','안녕하세요','만나서 반갑습니다.','행복한 하루 되세요^^']
# print('"엔터"join(li)\t:',"\n\n".join(li))
# # 기존의 문자열 과 새 문자열 합해줌

# =>출력값
# "%".join(123)   : 1%2%3
# 123.join("%a")  : %123a
# "공백". join([123,456]  : 123456
# "엔터"join(li)  :

# 안녕하세요

# 만나서 반갑습니다.

# 행복한 하루 되세요^^

# Str = 'python' 
# print('Str\t\t:',Str)
# print('Str.center(10)\t:',Str.center(10))
# # 10을 확보하고 중간에다 정렬
# print('Str.center(10,"-"):',Str.center(10,'-'))
# # '-'빈 공간에 채워준다. 한글도 가능 하지만 칸 수가 넘어갈 수 있다.?
# print('Str.ljust(10)\t: ',Str.ljust(10),Str.ljust(10))
# print('Str.ljust(10)\t: ',Str.ljust(10),Str.ljust(10,'-')) 
# #Str.ljust(10)   :  python     python----
# print('Str.rjust(10)\t: ',Str.rjust(10),Str.rjust(10)) 
# print('Str.zfill(10)\t: ',Str.zfill(10))
# #zfill은 외쪽 빈공간에 0을 채우기 때문에 다른 글로 지정이 불가하다.

# =>출력물
# Str             : python
# Str.center(10)  :   python
# Str.center(10,"-"): --python--
# Str.ljust(10)   :  python     python
# Str.rjust(10)   :      python     python
# Str.zfill(10)   :  0000python3

# accountBook="shoes 03/02 59000,coffee 03/03 2500,food 03/04 7000,dress 03/13 130000"
# replaceAB = accountBook.split(',')#,rlwnsdmfh fltmxm wjwkd
# k = 0
# for i in replaceAB:
#     replaceAB[k]=i.lstrip()#각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress)
#     k+=1
# kk='$ '#=>공백을 줘야 삽입된다.
# print('item'.ljust(10),end='')
# print('date'.ljust(10),end='')
# print('$(price)'.ljust(10))
# for i in range(len(replaceAB)):
#     z=replaceAB[i].split()#공백을 기준으로 리스트로 저장
#     for k in range(len(z)): 
#         if k == 0 : 
#             print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력 
#         elif k ==1 : 
#             print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력 
#         elif k == 2 :  
#             print("{:,}".format(int(z[k])).join(kk).ljust(10)) 

#  문자열 함수 
# 문자열 구성 파악 
# • True 또는 False를 반환
# 함 수 설 명 사용법 
# isdigit() 전체가 숫자로만 되어 있는가 Str.isdigit() 
# isalpha() 전체가 글자(한글/영어)로 되어 있는가 Str.isalpha() 
# isalnum() 전체가 글자와 숫자가 섞여 있는가 Str.isalnum() 
#공백만 없으면 false, true가 나오면 위에꺼를 다 봐야한다.
# islower() 전체가 소문자로 되어 있는가 Str.islower() 
# isupper() 전체가 대문자로 되어 있는가 Str.isupper() 
#전체 문자가 대소문자..
# isspace() 전체가 공백 문자로 되어 있는가 Str.isspace()

# Str = 'prthon te12st 1234'
# print("Str.isdigit():",Str.isdigit())#숫자로만 구성
# print("Str[9:11].isdigit():",Str[9:11].isdigit())#숫자로만 구성

# print("Str.isalpha():",Str.isalpha())#글자로 구성
# print("Str[:6].isalpha():",Str[:6].isalpha())#글자로 구성

# print("Str.isalnum():",Str.isalnum())#글자+숫자
# print("Str[7:13].isalnum():",Str[7:13].isalnum())#글자+숫자

# print("Str.islower() : ",Str.islower())#소문자 
# print("Str.isupper() : ",Str.isupper())#대문자 
# print("Str.isspace() : ",Str.isspace())#공백
# #=>출력값
# Str.isdigit(): False
# Str[9:11].isdigit(): True
# Str.isalpha(): False
# Str[:6].isalpha(): True
# Str.isalnum(): False
# Str[7:13].isalnum(): True
# Str.islower() :  True
# Str.isupper() :  False
# Str.isspace() :  False

# 뒤의 주민번호를 ******* 로 변경 하시오 
# info = """ 
# jo 9abc08-3022023 
# cho 900402-1011232 
# test 1234567-1234567  
# lee 980908-3a2b0c3 
# kim 900514-2022023 
# """
# lo=0
# while True:
#     lo=info.find("-",lo)#'-'를 찾아서
#     if lo != -1:#'-'이 있을 경우 ==> 여기까지 맞음..
#         if info[lo+1:lo+8].isdigit(info[lo+1:lo+8]) and info[lo-6:lo].isdigit() and not(info[lo-7:lo].isdigt())
#         #'-'앞에 값이 7자리가 아니면! 7자리가 참이면 안된다.그래서 not를 붙힘
#         # if info.isdigit(info[lo+1:lo+8]):  내꺼..
#              info=info.leplace(info[lo+1:lo+8],"*******")
#         lo+=1
#     else:
#         break


# #         # if len(lo) == 7:#뒤에가 7자리일 경우
# #         #     info.isdigit()#숫자로만 이루어질 경우
# #         #     lo.replace(lo,'*')#뒷자리를 *로 변경
# #         # else:
# #         #     break
# # print(info)   

# #강사님 풀이
# info = """
# jo 9abc08-3022023
# cho 900402-1011232
# test 1234567-1234567
# lee 980908-3a2b0c3
# kim 900514-2022023
# """
# lo=0
# while True :
#     lo=info.find('-',lo)
#     if lo != -1 :
#         if info[lo+1:lo+8].isdigit() and info[lo-6:lo].isdigit() and not(info[lo-7:lo].isdigit()) :
#             info=info.replace(info[lo+1:lo+8],"*******")
#         lo+=1
#     else :
#         break
# print(info)

# PYTHON_PROGRAMMING 함수
# 함수란?
# 함수 = function = 기능
# 어떠한 기능을 가진 소규모의 프로그램을 정의해놓은 키워드

# 함수는 표준함수와 사용자 정의 함수로 나뉨

# 함수를 정의 할때는 def라는 키워드를 사용함

# 함수를 사용하는 목적
# 1)코드의 간소화
# 2)프로그램의 흐름을 한눈에 알아보기 쉽다.
# 3)프로그램의 부품화로 생산성이 높아진다.
# 4)수정 편집이 용이해진다.

# result,tamp=0,0
# result=int(input("수 입력 : "))
# while True:
#     temp = result%10
#     result = result//10
#     print(temp,end="")
#     if not result: break;
# print("\n프로그램 종료")
# # =>뭔말인지 모르겠다..

# def reverseCode():
#     result,temp = 0,0
#     result = int(input("수 입력 : "))
#     while True:
#         temp = result%10
#         result = result//10
#         print(temp,end="")
#         if not result: break;
# print("프로그램 시작")
# reverseCode()
# print("\n프로그램 종료")

#함수를 공부하는 방법
# def reverseCode():
#     result,temp = 0,0
#     result = int(input("수 입력 : "))
#     while True:
#         temp = result%10
#         result = result//10
#         print(temp,end="")
#         if not result: break;
# print("프로그램 시작")
# reverseCode()#함수를 호출하는 것
# # 위에 저장되어있는 함수가 실행되는것!!
# print("\n프로그램 종료")

# def reverseCode(result):
#     while True:
#         temp = result%10
#         result = result//10
#         print(temp,end="")
#         if not result: break;
# print("프로그램 시작")
# result = int(input("수 입력 : "))
# reverseCode(result)
# print("\n프로그램 종료")

# def calc():
#     result=0
#     su1,op,su2=int(input("숫자")),input("부호:"),int(input("숫자"))
#     result = su1+su2
#     print(su1,'+',su2,'=',result)
# calc()
# 부호를 무엇을 입력하든 함수에 입력된 +로만 연산된다.

# def cal(su1,op,su2):#()안에 매게 아래와 이름과 같지 않아도 된다.
#     resulr=0

#     result=su1+su2
#     print(su1,'+',su2,'=',result)

# su1,op,su2 = int(input("숫자")),input("부호"),int(input("숫자"))
# cal(su1,op,su2)#()안에 인수


