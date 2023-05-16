# # 아래와 같이 출력 되게 만드시오
# for i in range(0,5,1): 
#     print("상위포문 %d일때 하위 포문 :"%i,end="")
#     for j in range(0,5,1):
#         print(i*j,end=" ")
#     print() 
#강사님 풀이->
# for i in range(5): 
#     print("상위포문 %d일때 하위 포문 :"%i ,end="")
#     for j in range(5):
#         print("%3d"%(i*j),end="")#=> 3d를 한 이유는 칸 수 맞추기 위해!!
    # print() 

# 2중 for 문을 이용하여 아래와 같이 출력 하시오 
# 1       2       3       4       5
# 6       7       8       9       10
# 11      12      13      14      15
# 16      17      18      19      20
# 21      22      23      24      25
# 1번째
# for i in range(1,26,5):
#     print("%3d"%((i+5)-5),end="")
#     for j in range(2,6,1):
#         print("%3d"%(j+i),end="")
#     print()

    
#2번째
# for i in range(1,26,5): 
#     print(i,end="")
#     for j in range(1,5,1):
#         print("%3d"%(j+i),end="")
#     print()

#3번째
# for i in range(5,6,1):
#     for i in range(1,5,1):
#         print("%3d"%(i),end="")
#     for j in range(5,6,1):
#         print(j)
#================이거 왜 이렇게 되는지 파악해보자아아

#강사님 풀이
# for i in range(1,22,5):
#     print(i,end="\t")
#     for j in range(1,5):
#         print(i+j,end="\t")
#     print()

# for i in range(5):
#     for j in range(1,6):
#         print(i*5+j,end="\t")
#     print()

# su1=0
# su2=1
# for i in range(1,6,1):
#     su1=i*5
#     for j in range(su2,su1+1,1):
#         print(j,end="\t")
#     print()
#     su2=su1+1

#[[while문]]
# for는 제한적 반복
# while는 무한적 반복
# 패턴이 규칙적일 때 for문에서 range 사용
# while문은 불규칙적일 때 유용하다

# i=0 #for의 시작 값
# while i<5:#for의 끝 값
#     print(i,"종속 문장")
#     i+=1#for의 증감 값
# print("다음 문장")

# # for문으로 변경하시오
# # i=0
# # for j in range(5):
# #     print(i,"종속 문장")
# #     i+=1
# # print("다음 문장")

#강사님
# for i in range (0,5,1):
#     print(i,"종속 문장")
# print("다음 문장")

# i=1
# odd,even=0,0
# while i<=10:
#     if i %2 ==0:
#         even+=i
#     else:
#         odd+=i
#     i+=1
# print("1-10 짝수의 합: ",even)
# print("1-10 홀수의 합: ",odd)

# i=0
# while i < 5:
#     print(i,"종속 문장")
#     i+=1
# else:
#     print("조건식이 거짓일 경우 : ",i)
# print("다음 문장")
#마지막 거짓일때 뭘 출력을 해야할 경우 while를 사용 할 수 있다.

# i=1
# while True:#=>끝 값이 계속 무한 방법, 거짓일 경우가 없댜..그래서 무한 반복
#     print(i,"종속 문장",end="")
#     i+=1
# # => 무한 반복이 된다....

# i=1
# flag = True
# while flag:#(flag=항복을 의미,개발자들 사이에선 스위칭이 되고있다라는 의미를 포함)
#     print(i,"종속 문장",end="")
#     if i == 10:
#         flag = False
#     i+=1

# # 기타 제어문 
# ❖ break문 (깨트리다..반복 순환을 깨는 것)
# ▪ for, while 문에서 실행 루프로부터 벗어나려고 할 때 사용 
# ❖ continue 문 
# ▪ for, while 문에서 실행 루프 내에서 
# # 실행 순서를 무조건 제어 루프의 조건식으로 옮겨서, 
# 다음 번의 반복 실행이 진행 
#continue,break는 아래가 코드가 와도 실행되지 않는다..

# i=0
# while True:
#     if i ==3:
#         break
#         print("3출력")#=>break아래여서 실행 안됨
#     print(i,"출력")
#     i+=1
# print("다음 문장")

# i=0
# while i<5:
#     i+=1
#     if i == 3:
#         continue
#         print("3출력")#=> 3일경우엔 다시 위로 올라가서 다시 while문 실행됨
#     print(i,"출력")
# print("다음 문장")

# num,result,i=0,0,1
# while True:
#     num = int(input("1~10사이의 숫자 입력: "))
#     if num <1 or num >10:
#         print("잘못 입력 다시")
#         continue
#     break
# else:
#     print("next...")#===> 이게 출력이 안된다.해결하는 방법 3가지
# while i < num:
#     result+=i;i+=1
# else:
#     print("1~",num,"까지의 합 :",result)

# 내가 한거 버그 못 잡음..
# num,result,i=0,0,1
# while True:
#     num = int(input("1~10사이의 숫자 입력: "))
#     if num <1 or num >10:
#         print("잘못 입력 다시")
#         continue
#     else:
#         print("next...")
#         break
# while i < num:
#     result+=i;i+=1
# else:
#     print("1~",num,"까지의 합 :",result)

#1st
# num,result,i=0,0,1
# flag=True
# while flag:
#     num = int(input("1~10사이의 숫자 입력: "))
#     if num <1 or num >10:
#         print("잘못 입력 다시")
#         continue
#     else :
#         flag=False
# else:
#     print("next...")#===> 이게 출력이 안된다.해결하는 방법 3가지
# while i < num:
#     result+=i;i+=1
# else:
    # print("1~",num,"까지의 합 :",result)

# 이중 포문을 와일 문으로 변환하는뎅..이중 와일문으로 변환
# for i in range ( 0 , 3 , 1): 
#     for k in range ( 0 , 5 , 1): 
#         if k == 3: 
#             break 
#         print("(i : %d\tk : %d)" % (i , k )) 
#===>i를 0~3을 실행 시키고,k 종속 for문은 0~5까지 실행 시키는뎅..
# k가 3이면 깨지는 코드

# for i in range ( 0 , 3 , 1): 
#     for k in range ( 0 , 5 , 1): 
#         if k == 3: 
#             continue #이거는 break랑 차이를 알기 위해 한것,
                       #차이는 브레이크는 아예 벗어나고, 
                       #컨티뉴는 처음으로 실행 안되고 돌아가서 다음거 다시 진행됨
#         print("(i : %d\tk : %d)" % (i , k )) 
# print("---------------")
# i=0
# k=0
# while i<3 :
#     i+=1
#     # print(i-1)
#     while k<5 :
#         k+=1
#         # print(k-1)
#     # if k==3:
#     #     break

#         print("(i : %d\tk : %d)" % (i-1 , k-1 ))