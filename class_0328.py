# ls = [10,5,20,7,9,31,12,11,19,32] 
# 리스트 2개를 만들어서 홀수번째의 값, 짝수번째의 값을 따로 넣고 
# 짝수번째 인덱스와 홀수번째의 차를 또다른 리스트에 넣어놓고 출력하시오. 
# (결과 : [-5, -13, 22, -1, 13]) 

# even=[ls%2==0]
# odd=[ls%2!=0]
# i=ls%2==0
# print(i)
# 나는 못해.. ㅠㅠ


# ls의 값 중 인덱스 홀수 번째와 짝수 번째의 합과 차를 구하시오 
# (짝수번째 [0,2,4,8] – [1,3,5,7,9]홀수번째) 
# (결과 : -16 ) 
# ls에 저장된 값을 invertLs에 거꾸로 저장하시오 
# ls의 값을 오름차순으로 sortLs에 저장 후 출력 
# ls의 값을 내림차순으로 reverseLs에 저장 후 출력

# 강사님 풀이
# ls = [10,5,20,7,9,31,12,11,19,32]
# hol_ls=[]
# jjak_ls=[]
# result_ls=[]
# for i in range(len(ls)) :
#     if i%2==0 :
#         hol_ls.append(ls[i])
#     else :
#         jjak_ls.append(ls[i])
# for k in range (len(hol_ls)) :
#     result_ls.append(jjak_ls[k]-hol_ls[k])
# print(result_ls)

# ls = [10,5,20,7,9,31,12,11,19,32]
# hol_sum=0 ; jjak_sum=0
# for i in range (len(ls)) :
#     if i%2 == 0 :
#         jjak_sum+=ls[i]
#     else :
#         hol_sum+=ls[i]
# print(jjak_sum-hol_sum)

# ls = [10,5,20,7,9,31,12,11,19,32]
# invertls=[]
# templs=ls[:]
# for i in range(len(ls)):
#     # invertls.append(ls.pop())=> 원본 훼손이 되었다..
#     invertls.append(templs.pop()) #=> 원본 훼손이 안 되었다..
# print(invertls)

# ls = [10,5,20,7,9,31,12,11,19,32]
# invertls=[]
# for i in range(1,len(ls)+1):
#     invertls.append(ls[-i])
# print(invertls)

# ls = [10,5,20,7,9,31,12,11,19,32]
# sortls=ls[:]
# for i in range (len(ls)-1) :
#   for j in range (i+1,len(ls)) :
#       if sortls[i] > sortls[j] :
#           sortls[i] ,sortls[j] = sortls[j] ,sortls[i]
# print(sortls)

# ls = [10,5,20,7,9,31,12,11,19,32]
# reversls=ls[:]
# for i in range (len(ls)-1) :
#     for j in range (i+1,len(ls)) :
#         if reversls[i] < reversls[j] :
#             reversls[i] ,reversls[j] = reversls[j] ,reversls[i]
# print(reversls)

# aa=[[1,2,3,4], 
# [5,6,7,8], 
# [9,10,11,12]]

# for i in range (len(aa)) :
#     for j in range(len(aa[i])):
#         print (aa[i][j],end="\t")
#     print ()
# print ()
# for i in aa:
#     for i in i:
#         print (j,end="Wt")
#     print ()
    
# aa=[ 
# [1,2,3,4], 
# [5,6,7,8], 
# [9,10,11,12]  
# ] 
# a = aa[0] 
# a[1]=20000 

# print('[0]',aa[0]) 
# print(a) 
# print(aa) 
#얕은 복사

# import copy 
# aa=[ 
# [1,2,3,4], 
# [5,6,7,8], 
# [9,10,11,12]  
# ] 
# #a = aa[0][:] 
# a = copy.deepcopy(aa[0]) a[1]=200000000 
# print('[0]',aa[0]) 
# print(a) 
# print(aa)

# ls_1=[];ls_2=[];value=1
# for i in range (3) :
#     for j in range (4) : #한행을 만들기 위한 반복
#         ls_1.append(value)
#         value+=1
#     ls_2.append(ls_1)
#     ls_1=[]
# # ls_1.clear()

# for i in ls_2 :
#     for j in i:
#         print(j,end="\t")
#     print()
# print(ls_2)

# be = ['2019','12','31'] 
# print(be) 


# af=list(map(int,be)) 
# print(af)
# 멥함수는 시퀀스 형 자료를 일관되게 한 함수로 변경할때 사용

# [튜플]

# tp = (10,20,30) 
# print("tp : ",tp) 
# print("tp type : ",type(tp)) 
# print("tp len : ",len(tp))

#=> 출력 값
# tp :  (10, 20, 30)
# tp type :  <class 'tuple'>
# tp len :  3

# tp1 = 10,20,30 
# print("tp1 : ",tp1) 
# print("tp1 type : ",type(tp1)) 

# print("tp1[0] type : ",type(tp1[0])) #=> 한번 사용한 인덱스는 다시 사용 수정 불가

# tp1[0] = 100 #에러 발생

#=> 출력 값
# tp1 :  (10, 20, 30)
# tp1 type :  <class 'tuple'>
# tp1[0] type :  <class 'int'>
# Traceback (most recent call last):
#   File "E:\3월 평일 0308 파이썬 기초_정혜란\class_0328.py", line 152, in <module>
#     tp1[0] = 100 #에러 발생
# TypeError: 'tuple' object does not support item assignment

# tpType = "문자열",100,1.111 

# print("tpType : ",tpType) 
# print("type : ",type(tpType)) 
# print("tpType[0] type : ",type(tpType[0])) 
# print("tpType[1] type : ",type(tpType[1])) 
# print("tpType[2] type : ",type(tpType[2]))
# # => 출력값
# # tpType :  ('문자열', 100, 1.111)
# # type :  <class 'tuple'>
# # tpType[0] type :  <class 'str'>
# # tpType[1] type :  <class 'int'>
# # tpType[2] type :  <class 'float'>
# # 계속하려면 아무 키나 누르십시오 . . .

# tpInt = (10) 
# print("tpInt : ",type(tpInt)); #<class ‘int’> 

# tpT1 = (10,) 
# print("tpT1 : ",type(tpT1)); #<class ‘tuple’> 
      
# tpT2 = 10, 
# print("tpT2 : ",type(tpT2)); #<class ‘tuple’>
# # => 출력값
# # tpInt :  <class 'int'>
# # tpT1 :  <class 'tuple'>
# # tpT2 :  <class 'tuple'>
# ','(콤마를 사용 하면 튜플형이 된다.)

# ls=[1,]
# print(ls)
# => 출력값
# [1] 맨뒤에 오는 콤마는 상관없댜

# tt1 = ( 10 , 20 , 30 , 40 ) 
# tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3] 
# print("튜플 합 : %d" % tt2) 

# print("tt1[1:3] : " , tt1[1:3]) #(:)슬라이싱은 자르는 것이 아니라 범위를 지정하는 문법
# print("tt1[1:] : " , tt1[1:]) 
# print("tt1[:3] : " , tt1[:3])

# a = 1,2,3 
# b = 4,5,6 
# c = a+b 
# print("a : ",a) 
# print("b : ",b) 
# print("c : ",c)

# =>출력값
# a :  (1, 2, 3)
# b :  (4, 5, 6)
# c :  (1, 2, 3, 4, 5, 6) 업데이트 연산이 필요하다

# 예제 ( packing & unpacking ) 
# 튜플에서 제일 중요함!!

# pack = 1,2,"패킹" 
# print("packing\npack : ",pack) 
# a,b,c = pack #+=> 그릇이 모자라도 에러, 그릇이 많아도 에러
# #=> 데이터와 그릇은 정확하게 매칭해야한다.
# print("unpacking\na:",a,"b:",b,"c:",c)

# =>출력값
# packing
# pack :  (1, 2, '패킹')
# unpacking
# a: 1 b: 2 c: 패킹

# tp = 100,200,"함수",100,'개수' 
# print("tp안의 200의 위치 : " ,tp.index(200),"번째 인덱스") 
# print("tp안의 100의 개수 : ",tp.count(100)," 개") 

# =>출력값
# tp안의 200의 위치 :  1 번째 인덱스
# tp안의 100의 개수 :  2  개

# [딕셔너리] 키와 벨류로 표현
# student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'} 
# print(student) 
# mobile = {"품명":"겔럭시","가격":100,"크기":10} 
# print(mobile)
# # =>출력값
# {'학번': 1234, '이름': '홍길동', '학과': 'it학과'}
# {'품명': '겔럭시', '가격': 100, '크기': 10}

# impo = {} 
# impo['파이썬'] = 'www.python.org' 
# impo['네이버']='www.naver.com' 
# impo['구글']='www.google.com' 

# print("파이썬 : ",impo['파이썬'])
# print("네이버 : ",impo['네이버']) 
# print("구글 : ",impo['구글'])
# # => 출력값
# # 파이썬 :  www.python.org
# # 네이버 :  www.naver.com
# # 구글 :  www.google.com
# print(impo)
# # => 출력값
# # {'파이썬': 'www.python.org', '네이버': 'www.naver.com', '구글': 'www.google.com'}

# impo = {} 
# name = input('키값 입력 : ') 
# val = input('값 입력 : ') 
# impo[name] = val 

# print(name,": ",impo[name])
# # => 키값과 벨류 값을 입력 함수를 이용할 수 있다.
# print(impo)
# impo={}
# # for i in range :
# #     if len(name)==5
# name = input('이름 입력 : ')
# value = input('값 입력 : ')
# impo[name] = value
# print(impo)

# name={'겐지:수리검','맥크리:섬광탄','파라:로켓런처','리퍼:샷건','솔저:나선로켓'}
# valul={'겐지:수리검','맥크리:섬광탄','파라:로켓런처','리퍼:샷건','솔저:나선로켓'}
# print(name:valul)
# print(impo)