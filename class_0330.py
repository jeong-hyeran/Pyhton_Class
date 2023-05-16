# asia = {'korea', 'china', 'japan'} 
# print(asia) 
# asia2 = {'iraq', 'singapore', 'korea'} 
# asia.update(asia2) 
# print(asia) 

# print('-'*40) 

# asia = {'korea', 'china', 'japan'} 
# asia2 = {'iraq', 'singapore', 'korea'} 
# asia3=asia+asia2 
# print(asia3)
# # =>시퀀스 형이라 피연산자라 에러뜬다!!
# 오류 내용도 항상 확인해야한다.

# two={2,4,6,8,10,12} 
# three={3,6,9,12,15} 
# print('교집합',two & three) 
# print(two.intersection(three)) #=>인터섹션 함수 >교집합을 이렇게 표현 할 수 있다??
# print('합집합',two | three) 
# print(two.union(three)) #=>유니온 함수 >합집합을 이렇게 표현 할 수 있다??
# print('차집합',two - three) 
# print(two.difference(three)) #=>디퍼런스 함수 >차집합을 이렇게 표현 할 수 있다??
# print('배타적 차집합',two ^ three) 
# print(two.symmetric_difference(three))#=>시맥트릭 디퍼런스 함수 >배타적 차집합을 이렇게 표현 할 수 있다??

# =>출력값
# 교집합 {12, 6}
# {12, 6}
# 합집합 {2, 3, 4, 6, 8, 9, 10, 12, 15}
# {2, 3, 4, 6, 8, 9, 10, 12, 15}
# 차집합 {8, 2, 10, 4}
# {8, 2, 10, 4}
# 배타적 차집합 {2, 3, 4, 8, 9, 10, 15}
# {2, 3, 4, 8, 9, 10, 15}

# animal = {'호랑이', '사자','강아지','치타','햄스터','고양이'} 
# pet= {'강아지','고양이','햄스터'} 

# print(pet <= animal) 
# print(pet <= pet) 

# print(pet < animal) 
# print(pet < pet)

# =>출력값
# True
# True
# True
# False
# 갯수로 보는 걸까..? 아니면 안에 내용을 보는 것일까..?!

#[문자열]
# 시퀀스형 특징 -순서가 정해져있다, 인덱스를 사용 한다.반복문을 사용 할 수 있다.
Str = 'Have a nice day' 
# print("Str[0] : ",Str[0]) 
# print("Str[1] : ",Str[1]) 
# print("Str[2] : ",Str[2]) 
# print("Str[3] : ",Str[3]) 
# print() 
# print("문자열의 총 길이 : ",len(Str)) 
# print("Str : ",Str) 
# =>출력값 
# Str[0] :  H
# Str[1] :  a
# Str[2] :  v
# Str[3] :  e

# 문자열의 총 길이 :  15
# Str :  Have a nice day
# sum=0
# for i in Str:
#     i=1
#     sum+=i
#     print(sum)
#     print(end="Str : i")

# 시퀀스형 자료니깐 len를 사용
# => 강사님 풀이
# Str = 'Have a nice day'
# for i in range (len(Str)) :
#     print(Str[i],end="")
# print("\n")
# for i in Str :
#     print(i,end="")
# print()

# [문자열 slicing] 
# Str = 'Have a nice day' 
# arr = Str[7:11] 
# print("Str : " ,Str) 
# print("arr : " , arr);

# => 출력값
# Str :  Have a nice day
# arr :  nice
# 슬라이싱은 자르는게 아니고 지정하는것이다.
# 7번 부터 11번 까지 지정하는 것
# 문자열에서 가장 많이 사용하는 것이 슬라이싱

# Str = "즐거운 파이썬" 
# print("Str\t: " , Str) 
# print("Str[0]\t: " , Str[0]) 
# print("Str[1:3] : " , Str[1:3]) 
# print("Str[3: ] : " , Str[3 : ]) 
# print("Str[ : 3] : " , Str[ : 3])

# =>출력값
# Str     :  즐거운 파이썬
# Str[0]  :  즐->0번 인덱스,2바이트 문자를 하나의 인덱스로 잡아준다.
# Str[1:3] :  거운
# Str[3: ] :   파이썬
# Str[ : 3] :  즐거운

# Str = 'Have a' 
# print("변경 전 Str : ",Str) 

# Str+=' nice day' 

# print("변경 후 Str : " , Str) 
# print("Str * 3 : ",Str*3)

# =>출력값
# 변경 전 Str :  Have a
# 변경 후 Str :  Have a nice day
# Str * 3 :  Have a nice dayHave a nice dayHave a nice day

# 문자열 함수 
# 다른 시퀀스형에 비해 함수가 되게 많다.
# 공부하긴 힘들겠지만 이용하기가 쉽다.
# 이런 함수가 있구나 하는 것만 알고 있어도 실무에 가면 좋댜
# 함 수                설 명                                사용법 
# upper()     소문자를 대문자로 변경                      Str.upper() 
# lower()     대문자를 소문자로 변경                      Str.lower() 
# swapcase()  대소문자를 상호 변경                        Str.swapcase() 
# title()     각 단어의 제일 앞 글자만 대문자로 변경      Str.title() 

# Str = 'Pythone is Easy. 그리고 programming 할만하다 ^^' 
# print("Str : ",Str) 
# print() 
# print('Str.upper() : ',Str.upper()) #소문자를 대문자로 변경 print() 
# print('Str.lower() : ',Str.lower()) #대문자를 소문자로 변경 print() 
# print('Str.swapcase() : ',Str.swapcase()) #대소문자 상호 변경 print() 
# print('Str.title() : ',Str.title()) #각 단어의 첫번째 문자 대문자로 변경

# =>출력값
# Str.upper() :  PYTHONE IS EASY. 그리고 PROGRAMMING 할만하다 ^^
# Str.lower() :  pythone is easy. 그리고 programming 할만하다 ^^
# Str.swapcase() :  pYTHONE IS eASY. 그리고 PROGRAMMING 할만하다 ^^
# Str.title() :  Pythone Is Easy. 그리고 Programming 할만하다 ^^

# st = 'NevEr -eVer 110gIVe up'

# st=st.title()

# print(st)

# # =>출력값
# # Never -Ever 110Give Up

# st = 'NevEr-eVer110gIVeup'

# st=st.title()

# print(st)
# # =>출력값
# # Never-Ever110Giveup
# # 공백도 문자... 연속적으로 나열 됨
# # 연속적으로 단어를 구분해서 첫 문자만 대문자, 나머지는 소문자!

#  문자열 함수 
# 문자열 찾기
# 함 수                 설 명                               사용법 
# count()       찾을 문자열의 개수                      Str.count(‘문자열‘) 
# find()        찾을 문자열의 위치 없으면 -1            Str.find(‘문자열‘) 
# rfind()       입력한 문자열이 존재하는 위치를 
#               뒤에서부터 찾는다 없으면 -1             Str.rfind(‘문자열’) 
# index()       find()함수와 동일한 용도, 없으면 error  Str.index(‘문자열‘) 

# st = 'Have a nice day' 
# print("st : ",st) 
# print() 
# print("st안에 'a'문자 개수 : ",st.count('a')) 
# print("st안에 'day'문자열 개수 : ",st.count('day')) 
# print("st안에 'dak'문자열 개수 : ",st.count('dak'))

# =>출력값
# st :  Have a nice day

# st안에 'a'문자 개수 :  3
# st안에 'day'문자열 개수 :  1
# st안에 'dak'문자열 개수 :  0

# st = 'Have a nice day' 
# print("st : ",st) 
# print("find: 'day'위치 : ",st.find('day')) 
# print("index: 'day'위치 : ",st.index('day')) 
# print("find: 'kkk'위치 : ",st.find('kkk')) 
# print("index: 'kkk'위치 : ",st.index('kkk')) #=>에러가 뜬다

# =>출력값
# st :  Have a nice day
# find: 'day'위치 :  12
# index: 'day'위치 :  12
# find: 'kkk'위치 :  -1
# Traceback (most recent call last):
#   File "E:\3월 평일 0308 파이썬 기초_정혜란\class_0330.py", line 199, in <module>
#     print("index: 'kkk'위치 : ",st.index('kkk'))
# ValueError: substring not found


# st = 'Have a nice day' 
# print("st : ",st) 

# print("find: 'day'위치 : ",st.find('a')) 
# print("find: 'day'위치 : ",st.find('a',2)) 
# print("find: 'day'위치 : ",st.find('a',6)) 
# print("find: 'day'위치 : ",st.find('a',14))
# 문자만 지정하면 첫번째, 뒤에 숫자는 찾기 시작할 인덱스를 지정하는 것이다.

# # =>출력값
# # st :  Have a nice day
# # find: 'day'위치 :  1
# # find: 'day'위치 :  5
# # find: 'day'위치 :  13
# # find: 'day'위치 :  -1

# a의 총 개수와 첨자의 위치를 출력 하시오 
# 결과 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
# st = 'Have a nice day Have a nice day Have a nice day' 
# print("a의 총 개수는 %d개다."%st.count('a'))
# # while print(st.find('a')):
#     if st == -1:
#             print()
# print(st)
# print()

# => 강사님 풀이
# lo=0 #위치
# ls=[] #인덱스 만들어야 하니깐
# while True : # 무한 반복
#     lo=st.find('a',lo) # st에서 a를 찾으면 그게 lo
#     if lo != -1: #lo가 -1이 아니면, ls.append로 이용해서 인덱스 추가
#         ls.append(lo)
#         lo+=1 # lo에 1을 추가하여 찾기 시작하는 위치 지정
#     else: # -1일 경우엔 빠져 나가서 다시 반복!
#         break
# print(ls)

# 문자열 함수 
# 문자열 변경
# 함 수 설 명 사용법 

# strip() 문자열 양 끝 문자 제거 양쪽 공백 제거  Str.strip() or  Str.strip(‘문자’) 
# rstrip() 문자열 끝 문자 제거 오른쪽 공백 제거  Str.rstrip() or Str.rstrip(‘문자’) 
# lstrip() 문자열 처음 문자 제거 왼쪽 공백 제거  Str.lstrip() or Str.lstrip(‘문자’) 
# replace() 기존 문자열 새 문자열로 치환 Str.replace(‘기존 문 자열’,’치환문자열’) 

# st = '          파 이 썬         ' 
# print('st\t\t:{}{}{}'.format('*',st,'*')) 
# print() 
# print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))

# => 출력값
# st              :* 파 이 썬 *
# 연속된 공백은 다 날아간다아아앙
# st.strip()      :*파 이 썬*

# st = '파이썬파' 

# print('st\t\t:' ,st) 
# print() 
# print('Str.strip("파")\t:', st.strip('파')) 
# print("========================================") 

# st = '파이썬' 
# print('st\t\t:' ,st) 
# print() 
# print('Str.strip("파")\t:', st.strip('파'))

# => 출력값
# st              : 파이썬파

# Str.strip("파") : 이썬
# ========================================
# st              : 파이썬

# Str.strip("파") : 이썬

# st = '---파---이---썬---' 
# print('st\t\t:',st) 
# print('st.strip("-")\t:',st.strip('-')) 
# print('st.rstrip("-")\t:',st.rstrip('-')) 
# print('st.lstrip("-")\t:',st.lstrip('-'))

# =>출력값
# st              : ---파---이---썬---
# st.strip("-")   : 파---이---썬        > 양쪽'-'삭제
# st.rstrip("-")  : ---파---이---썬     > 오른쪽'-'삭제
# st.lstrip("-")  : 파---이---썬---     > 왼쪽'-'삭제

# st = '2015/04/02' 

# print('st\t\t:',st) 
# print('replace()\t:',st.replace('/','.')) 
# print('replace([0:4])\t:',st.replace(st[0:4],'2017'))
# =>출력값
# st              : 2015/04/02
# replace()       : 2015.04.02 > / -> . 변경 전체 바뀜
# replace([0:4])  : 2017/04/02 > 인덱스 0-4번까지를 2017로 변경


# st = '2015/04/02
 

# print('st\t\t:',st) 
# print('replace()\t:',st.replace('/','.')) 
# print('replace([0:4])\t:',st.replace(st[0:4],'2017'))
# =>출력값
# st              : 2015/04/02
# replace()       : 2015.04.02 > / -> . 변경 전체 바뀜
# replace([0:4])  : 2017/04/02 > 인덱스 0-4번까지를 2017로 변경' 

# st = '2015/04/02 2015/04/02'
# print('st\t\t:',st) 
# print('replace()\t:',st.replace('/','.')) 
# print('replace([0:4])\t:',st.replace(st[0:4],'2017'))
# =>출력값
# st              : 2015/04/02 2015/04/02
# replace()       : 2015.04.02 2015.04.02
# replace([0:4])  : 2017/04/02 2017/04/02
# ==>> 요거 다시 보기!! 꼭

# st = """ 
# 오늘 하루도 즐겁게 
# 오늘 하루도 행복하게 
# 오늘 하루도 최선을 
# """ 
# #> 블럭 주석... 주석 처리 문법도 맞지만 줄이 바뀌는 여러행이 들어가는 문자열을 표현할 때 이렇게 사용한다.
# 블럭주석은 문자열로 파악해서 에러 날 경우가 있다!
# print(st)

# =>출력값
# 오늘 하루도 즐겁게 
# 오늘 하루도 행복하게 
# 오늘 하루도 최선을

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

# print(st.replace('-',':'))
# while True :
#     sin=st.find('-')
#     if sin != -1:
#         print(st.replace(st[sin,4],'1991'))
#     sin+=1
#     else:
#         break

# print(sin)
# while True :
#     sin=st.find('년')
#     if sin == -4:
#         print(st.replace(st[0:4],'1999'))
#     else:
#         break
# print()

