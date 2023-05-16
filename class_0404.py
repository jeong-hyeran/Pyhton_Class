# import statistics  
  
# points = [65, 75, 55]  
# print('평균 : ', statistics.mean(points))  
# print('분산 : ', statistics.variance(points))  
# print('표준편차 : ', statistics.stdev(points))  
# #-----------------------------------------  
# import statistics as st  #임폴트 가져올 모듈명 'as' 바꿀명
# # 너무 긴 모듈명을 간단하게 표현 하고 싶을때 이용
  
# points = [65, 75, 55]  
# print('평균 : ', st.mean(points))  
# print('분산 : ', st.variance(points))  
# print('표준편차 : ', st.stdev(points))  

# 출력값
# 평균 :  65
# 분산 :  100
# 표준편차 :  10.0
# 평균 :  65
# 분산 :  100
# 표준편차 :  10.0

# import calculator as cal  
# from calculator import info  
  
# print("1인치 : %.2fcm"%cal.inch)  
# print("1~10까지의 누적합:",cal.calc_sum(10))    
# info()  
# info()  
# info()  

#모듈명은 숫자로 시작하면 안된다.
#변수명의 규칙이랑 같댜
#공백도 안된다.
#한글은 된다.

#[렌덤]

# import random 

# i=0 
# for i in range(5): 
#     print(i," ",random.random())

# 출력값
# 0   0.5885576364110195
# 1   0.37189471326420964
# 2   0.5154434369114903
# 3   0.3834774518083608
# 4   0.18260533025578918

# import random 
# i=0 
# for i in range(5): 
#     print(i," ",int(random.random()*100))
# int를 입혀서 백분율로 나타나게 됨

# import random 
# i=0 
# for i in range(5): 
#     print(i," ",random.randrange(1,10))

#10은 절대 안나옴..범위가 10까지여서.. n+1로 범위 지정해야한다.

# import random
# print("가위, 바위, 보를 선택하세요.\n1.가위\n2.바위\n3.보")
# num=int(input("숫자입력 : "))
# pc = int(random.randrange(1,4))
# i=0
# while True:
#     if 0<num<4 :
#         # num=int(input("숫자입력 : "))
#         print(pc)
#         if num == pc:
#           print("무승부")
#         if num == 1:
#            if pc == 2:
#                print("패")
#            if pc == 3:
#               print("승리")
#         if num == 2:
#            if pc == 3:
#               print("패")
#            if pc == 1:
#               print("승리")
#         if num == 3:
#             if pc == 1:
#               print("패")
#             if pc == 2:
#               print("승리")
# else:
#     print("다시 입력하세요")

## 반복으로 진행이 안된다앙

#가위 바위 보 게임
# import random
# print("### 가위 바위 보 게임 ###")
# user = int(input("0.가위 1.바위 2.보\n>>>> "))
# computer = random.randrange(0,3)
# menu=["가위","바위","보"]
# print("User : %s VS Computer : %s"%(menu[user],menu[computer]))
# if user == computer :
#     print("무승부!!!")
# elif (user==0 and computer==2) or (user==1 and computer==0) or (user==2 and computer==1) :
#     print("승리!!!")
# else :
#     print("패배!!!")

# #가위 바위 보 게임
# import random
# print("### 가위 바위 보 게임 ###")
# user = int(input("0.가위 1.바위 2.보\n>>>> "))
# computer = random.randrange(0,3)
# menu=["가위","바위","보"]
# print("User : %s VS Computer : %s"%(menu[user],menu[computer]))
# if user == computer :
#     print("무승부!!!")
# elif user-computer == -2 or user-computer== 1 :
#     print("승리!!!")
# else :
#     print("패배!!!")
    

## 내가 한거

# import random
# print("가위, 바위, 보를 선택하세요.\n1.가위\n2.바위\n3.보")
# num=int(input("숫자입력 : "))
# pc = int(random.randrange(1,4))
# i=0

# if 0<num<4 :
#     # num=int(input("숫자입력 : "))
#     # print(pc)
#     if num == pc:
#       print("무승부")
#     if num == 1:
#         if pc == 2:
#            print("패")
#         if pc == 3:
#           print("승리")
#     if num == 2:
#         if pc == 3:
#            print("패")
#         if pc == 1:
#            print("승리")
#     if num == 3:
#         if pc == 1:
#            print("패")
#         if pc == 2:
#            print("승리")
# else : 
#    print("잘 못 입력하셨습니다.")
#=====> 단일 게임

# for i in range(1,4):
#     print(pc)
#     if num==int(random.randrange(1,4)):
#         print("무승부")
#     # elif num != int(random.randrange(1,4)):
#     #     if num == 1:

import random
lotto=[]
while True :
    ball = random.randrange(1,46)
    if lotto.count(ball)==0:
        lotto.append(ball)
    if len(lotto)>= 6 :
        break
print("이번주 추천번호 : ",lotto)