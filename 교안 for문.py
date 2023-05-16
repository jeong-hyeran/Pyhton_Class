# PYTHON_PROGRAMMING 반복문
# 제어문 [for] 
# for 변수 in range(초기값 , 끝값 , 증감값) : print(“종속문장”) 
# 초기값 
# 끝값 거짓 
# 참
# 종속문장 
# 증감값 
# 예 제 
# print(1) 
# print(2) 
# print(3) 
# print(4) 
# print(5) 
# print(6) 
# print(7) 
# print(8) 
# print(9) 
# print(10)
# 예 제 
# for i in range(1 , 11 , 1) : print(i) 
# print('다음 문장')
# 예 제 
# for i in range(0 , 3 , 1) : 
# print("i : ",i,"for 문 이해하기^^") print('다음 문장들 실행')
# 예 제 
# for i in range(1 , 11 , 1) : 
# if i %2 == 0: 
# print("i = " , i , ": 값 확인") print("다음 문장")
# 예 제 
# for i in range(0 , 11 , 2) : print("i = " , i , ": 값 확인")
# 예 제 
# for i in range(10 , -1 , -1) : print(i , ": 10 ~ 0 까지 출력")
# Quiz 
# ❖ 1 ~ 10 까지의 합을 구하시오.
for i in range(1,10,1):
    print(i=+1)
# 예 제 
# for i in range(1,11,1): 
# print(i,end=" ") 
# ❖ 아래와 같이 출력 하시오 
# 1 2 3 4 5  6 7 8 9 10  11 12 13 14 15  16 17 18 19 20  21 22 23 24 25  26 27 28 29 30 
# Quiz 
# ❖ 수를 입력 받아 1 ~ 입력 받은 수 까지의 합을 구하시오 
# ❖ 수를 입력 받아 1 ~ 입력 받은 수 까지 짝수의 합과 홀수의 합을 구하시오.

# 수를 입력 받아 1 ~ 입력 받은 수 까지의 합을 구하시오 
# num=int(input("정수를 입력하시오."))
# sum=0
# for i in range(1,num,1):
#     sum+=i
# print(sum)

# # 수를 입력 받아 1 ~ 입력 받은 수 까지 
# # 짝수의 합과 홀수의 합을 구하시오.
# num=int(input("정수를 입력하시오."))
# sum=0
# for i in range(1,num,1):
#     if i %2
#     sum+=i
# print(sum)


# 예 제 
# i , Sum = 0 , 0 
# start , en , grow = 0 , 0 , 0 
# start = int(input("시작값 입력 : ")) 
# en = int(input("끝값 입력 : ")) 
# grow = int(input("증가값 입력 : ")) 
# for i in range ( start , en + 1 , grow ): 
# Sum = Sum + i 
# print("%d에서 %d 까지 %d씩 증가한 값의 합 : %d" % (start , en , grow , Sum))
# 예 제 
# Sum = 0 
# num = 0 
# num = int(input("값 입력 : ")) 
# for i in range ( num + 1 ): 
# print(i) 
# Sum = Sum + i 
# print("1에서 %d 까지 합 : %d" % (num,Sum))
# 예 제 
# for i in range(0,10): 
# print(i) 
# -------------------------------------- for i in range(10): 
# print(i) 
# -------------------------------------- for i in range(10,2): 
# print(i) 
# -------------------------------------- for i in range(0,10,2): 
# print(i)
# Quiz 
# ❖ 시작 값, 끝 값, 증가값(1) 입력받아 시작과 끝값 사이의 7의 배수를 출력 하시오. 
# ❖ 1 ~ 100 사이의 값 중 3의 배수 이며, 5의 배수에 해당하는 합을 구하시오. ❖ 두 수를 입력 받아 입력 받은 두 수의 범위 안의 합을 구하시오 
# ❖ 첫날에 10원을 예금하고, 다음날에는 전날의 2배를 예금하는 방식으로 한 달(30일) 동안 저축한 금액중 마지막 저금액을 구하시오. 
# (첫날 10, 둘째날 20 , 셋째날 40 . . .무조건 2배씩 증가되는 값이다)
# 예 제 
# for i in [1,2,3,4,5,6,7,8,9,10]: print("i : ",i)
# 예 제 
# ls = [1,2,3,4,5,6,7,8,9,10] for i in ls: 
# print("i : ",i) 
# for i in ls: 
# print(i,end=" ")
# 예 제 
# ls = [10 , "test" , 123.123] 
# print("list : ",ls) 
# print() 
# for i in ls: 
# print( "i에" , i , "대입한 후 print() 실행" ) print( type(i) )
# 예 제 
# st = "Hello Python" for i in st: 
# print("i : ",i)
# Quiz 
# ❖ st = "It is a fun Python class" 다음 문자열 중에서 ‘a’의 개수와 ‘s’의 개수 그리고 총 개수(공백 포함)도 구하시오 
# ❖ 결과 
# ❖ 총 개수 : 24 
# ❖ a 개수 : 2 
# ❖ s 개수 : 3
# format 
# print("{0}+{1}={2}".format(10,2,10+2)) 
# print("{2}+{1}={0}".format(10,2,10+2)) 
# print("{}+{}={}".format(10,2,10+2)) 
# print("{:,}".format(1000000)) 
# print("{:<10},왼쪽정렬,{:0<10}".format('첫번째','두번째')) print("{:>10},오른쪽정렬,{:9>10}".format('첫번째','두번째')) print("{:^10},가운데정렬,{:5^10}".format('첫번째','두번째'))
# PYTHON_PROGRAMMING 이중 FOR 문
# 중첩 [for] 
# ❖ 중첩 for문의 개념 
# ▪ 중첩 for문은 for문 내부에 또 다른 for문이 들어있는 형태
# 중첩 [for] 
# for i in range ( 0 , 3 , 1): 
# for k in range ( 0 , 5 , 1): 
# print("이중 for 문 (i : %d\tk : %d)" % (i , k )) ❖위의 내용을 바탕으로 구구단 만들기.
# Quiz 
# ❖아래와 같이 출력 되게 만드시오
# 중첩 포문 딱 한번으로 출력 가능 
# 상위포문 0 일때 하위 포문 :0 0 0 0 0  
# 상위포문 1 일때 하위 포문 :0 1 2 3 4  
# 상위포문 2 일때 하위 포문 :0 2 4 6 8  
# 상위포문 3 일때 하위 포문 :0 3 6 9 12  
# 상위포문 4 일때 하위 포문 :0 4 8 12 16 
# Quiz 
# ❖ 2중 for 문을 이용하여 아래와 같이 출력 하시오 
# 1 2 3 4 5 
# 6 7 8 9 10 
# 11 12 13 14 15 
# 16 17 18 19 20 
# 21 22 23 24 25