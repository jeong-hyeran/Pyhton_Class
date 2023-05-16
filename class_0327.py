# ls=[10,20,30]
# arr=[40,50,60]

# print("ls:", ls)
# print("arr:", arr)

# Str=ls+arr
# print("ls+arr=>Str:",Str)

# string=ls*3
# print("ls*3=>string:",string)

#=>출력값
# ls: [10, 20, 30]
# arr: [40, 50, 60]
# ls+arr=>Str: [10, 20, 30, 40, 50, 60]
# ls*3=>string: [10, 20, 30, 10, 20, 30, 10, 20, 30]
#시퀀스형이여서 업데이트 연산이 되었다!

# ls=[10,20,30]
# arr=[40,50,60]

# for ls in range(10,31,10):
#     for arr in range(40,61,10):
#         # print("ls:", ls,"arr:", arr)
#         Str=ls+arr
#         print("ls + arr => Str : ",Str)

#         string=ls*3
#         print("ls * 3 => string : ",string)
# print()

# 강사님 풀이
# ls = [ 10 , 20 , 30 ]
# arr = [ 40 , 50 , 60 ]
# Str=[0,0,0]#=> 초기화는 해둬야 한다.
# string=[0,0,0]
# for i in range(len(ls)) :
#     Str[i] = ls[i] + arr[i]
#     string[i]=ls[i]*3
# print(Str)
# print(string)
#=>출력값
# [50, 70, 90]
# [30, 60, 90]

#[알고리즘]
#선택정렬 알고리즘
#=> 강사님 풀이
# ls=[4,8,2,7,6]
# for i in range (len(ls)-1):#기준 인덱스를 위한 반복(len(ls-1)첫번째 표시)
#     for j in range(i+1,len(ls)):
#         if ls[i] > ls[j]:
#             ls[i],ls[j]=ls[j],ls[i]
# print(ls)
# #=>출력값
# [2, 4, 6, 7, 8]

#순위 구하기 알고리즘
# 등수,석차가 필요하다.
# 1로 초기화가 되어있어야 한다.

# ls=[82,85,76,79,96]
# rank=[1,1,1,1,1]
# for i in range(len(ls)-1):
#     for j in range (i,len(ls)):
#         if ls[i] >= ls[i+1]:
#             rank+=1
# print("점수 : %d, 등수 : %d"%(ls,rank))
#나는 뭐 하나도 모르겠다..

#강사님 풀이
# jumsu=[82,85,76,79,96]
# rank=[1,1,1,1,1]
# for i in range(len(jumsu)):#기준 인덱스
#     for j in range(len(jumsu)):#비교 인덱스
#         if jumsu[i] < jumsu[j]:
#             rank[i]+1
# for k in range (len(rank)):
#     print("점수 : %d / %d등"%(jumsu[k],rank[k]))

#리스트 조작 함수
# ls =[10,20,30]
# ls.append(1000)
# #리스트 맨 뒤에 1000을 추가 한다.
# for i in range(len(ls)):
#     print("ls[{}]:{}".format(i,ls[i]))
# print("리스트의 총 개수:",len(ls))
# print("ls:",ls)
# ls=[]
# print("ls 초기화 후 : ",ls)

#=>출력값   
# ls[0]:10
# ls[1]:20
# ls[2]:30
# ls[3]:1000
# 리스트의 총 개수: 4
# ls: [10, 20, 30, 1000]
# ls 초기화 후 :  []

# ls = [] #리스트 자료형으로 초기화
# for i in range(0 , 4) : 
#     ls.append(0) 
# Sum = 0 

# for i in range(0 , len(ls)) : 
#     ls[i] = int(input(str(i+1) + "번째 숫자 : ")) 
#     Sum += ls[i] 
# for i in range(0 , len(ls)) : 
#     print("입력 받은 값 ls[{}] : {}".format( i , ls[i] )) 
# print("합 계 : %d " % Sum)

#출력값
# 1번째 숫자 : 1
# 2번째 숫자 : 2
# 3번째 숫자 : 3
# 4번째 숫자 : 4
# 입력 받은 값 ls[0] : 1
# 입력 받은 값 ls[1] : 2
# 입력 받은 값 ls[2] : 3
# 입력 받은 값 ls[3] : 4
# 합 계 : 10

# num = int(input('몇개의 공간 만들겠습니까? :')) 
# ls = [] 
# Sum = 0 
# for i in range(num) : 
#     ls.append(int(input(str(i+1) + "번째 숫자 : "))) 
#     Sum += ls[i] 
# for i in range(0 , len(ls)) : 
#     print("입력 받은 값 ls[{}] : {}".format( i , ls[i] )) 
# print("합 계 :", Sum)

# 리스트 조작 함수( pop, sort, reverse ) 
# List = [ 30 , 20 ,10 ] 
# print("현재 리스트 : " , List) 

# List.append(40) 
# print("append(40) 후 리스트 : " , List) 

# print("pop() 으로 추출한 값 : " , List.pop()) 
# print("pop() 후 리스트 : " , List) 

# List.sort() 
# print("sort() 후 리스트 : " , List) 

# List.reverse() 
# print("reverse() 후 리스트 : " , List) 

# del(List[2]) 
# print("del() 후 리스트 : " , List)

#출력 값
# 현재 리스트 :  [30, 20, 10]
# append(40) 후 리스트 :  [30, 20, 10, 40]
# pop() 으로 추출한 값 :  40 # 맨뒤의 값 뺌
# pop() 후 리스트 :  [30, 20, 10] # pop로 추출 후
# sort() 후 리스트 :  [10, 20, 30]# 오름 차순 정렬
# reverse() 후 리스트 :  [30, 20, 10] # 항목을 역순으로 정렬(내림차순)
# del() 후 리스트 :  [30, 20] #[2](세번째 값 삭제)

#강사님 설명을 위해 리스트 수정
#뒤죽박죽 규칙성 없게
# List = [ 98,1,75,14,2,16,8,14,9,31,15,77 ] 
# print("현재 리스트 : " , List) 

# List.append(40) 
# print("append(40) 후 리스트 : " , List) 

# a=List.pop()
# print(a)
# a=List.pop(2)=> 인덱스 위치를 지정할 수도 있다.
# print(a)

# print("pop() 으로 추출한 값 : " , List.pop()) 
# print("pop() 후 리스트 : " , List) 

# List.sort() 
# print("sort() 후 리스트 : " , List) 

# List.reverse() 
# print("reverse() 후 리스트 : " , List) 

# del(List[2]) 
# print("del() 후 리스트 : " , List) => 삭제가 목적

# 리스트 조작 함수( index, insert, remove, extend ) 
# List = [ 30 , 20 ,10 ] 
# print("현재 리스트 : " , List) 

# print(" 10 값의 위치 : " , List.index(10)) #인덱스 위치를 알려줌

# List.insert(2,200) 
# print("insert(2,200) 후 리스트 : " , List) # 지정된 위치에 값을 입력, 인덱스가 뒤로 밀려!

# List.remove(200) 
# print("remove(200) 후 리스트 : " , List) # 지정된 값을 삭제

# List.extend( [ 555 , 666 , 555 ] ) 
# print("extend( [ 555 , 666 , 555 ] ) 후의 리스트 : " , List) # 리스트 뒤에 리스트를 추가한다.

# print("555 값의 개수 : " , List.count(555)) # 지정된 값의 개수 파악

# List = [ 98,1,75,14,2,16,8,14,9,31,15,77 ] 

# ls = [10,5,20,7,9,31,12,11,19,32] 
# # 리스트 2개를 만들어서 홀수번째의 값, 짝수번째의 값을 따로 넣고 
# # 짝수번째 인덱스와 홀수번째의 차를 또다른 리스트에 넣어놓고 출력하시오. 
# # (결과 : [-5, -13, 22, -1, 13]) 

# # even=[ls%2==0]
# # odd=[ls%2!=0]
# i=ls%2==0
# print(i)

# ls의 값 중 인덱스 홀수 번째와 짝수 번째의 합과 차를 구하시오 
# (짝수번째 [0,2,4,8] – [1,3,5,7,9]홀수번째) 
# (결과 : -16 ) 

# ls에 저장된 값을 invertLs에 거꾸로 저장하시오 
# ls의 값을 오름차순으로 sortLs에 저장 후 출력 
# ls의 값을 내림차순으로 reverseLs에 저장 후 출력
