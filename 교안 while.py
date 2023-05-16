# PYTHON_PROGRAMMING WHILE 문
# while 
# ❖ 정의 
# 주어진 조건식을 평가하여 그 결과가 참인 동안은 while 루프의 종속문장을 반복실행 

# While 조건식: 종속 문장 
# While 조건식: 종속 문장 
# Else: 
# 종속문장 
# 조건식 거짓 참
# 종속문장 

# 예 제 
# i=0 
# while i<5: 
# print(i, "종속 문장") 
# i+=1 
# print("다음 문장") 
# ❖for 으로 변경하시오.
# 예 제 
# i=1 
# odd,even=0,0 
# while i<=10: 
# if i % 2 ==0: 
# even+=i 
# else: 
# odd+=i 
# i+=1 
# print("1-10 짝수의 합 : ",even) print("1-10 홀수의 합 : ",odd) 
# ❖for 으로 변경하시오.
# 예 제 
# i=0 
# while i<5: 
# print(i, "종속 문장") 
# i+=1 
# else: 
# print("조건식이 거짓일 경우 : ",i) print("다음 문장")
# 예 제 
# i=1 
# while True: 
# print(i, "종속 문장",end=" ") i+=1
# 예 제 
# i=1 
# flag = True 
# while flag: 
# print(i, "종속 문장",end=" ") if i == 10: 
# flag = False 
# i+=1
# 기타 제어문 
# ❖ break문 (깨트리다..반복 순환을 깨는 것)
# ▪ for, while 문에서 실행 루프로부터 벗어나려고 할 때 사용 
# ❖ continue 문 
# ▪ for, while 문에서 실행 루프 내에서 
# 실행 순서를 무조건 제어 루프의 조건식으로 옮 겨서, 
# 다음 번의 반복 실행이 진행 
# While 조건식 : 
# if n<10 : 
# continue 
# if n>100 : 
# break 
# }
# 예 제 
# i=0 
# while True: 
# if i == 3: 
# break 
# print("3출력") 
# print(i,"출력") 
# i+=1 
# print("다음 문장")
# 예 제 
# i=0 
# while i<5: 
# i+=1 
# if i == 3: 
# continue 
# print("3출력") 
# print(i,"출력") 
# print("다음 문장") 
# ❖for 으로 변경하시오.
# 예 제 
# num,result,i=0,0,1 
# while True: 
# num = int(input("1~10사이의 숫자 입력 : ")) if num<1 or num>10: 
# print("잘못 입력 다시") 
# continue 
# break 
# else: 
# print("next...") 
# while i<=num: 
# result+=i; i+=1 
# else: 
# print("1~",num,"까지의 합 : ",result)
# Quiz 
# ❖10 ~ 20 사이의 숫자만 입력 받아 1부터 입력 받은 수까지의 합을 구하시오.
# 예 제 1 
# for i in range ( 0 , 3 , 1): 
# for k in range ( 0 , 5 , 1): 
# if k == 3: 
# break 
# print("(i : %d\tk : %d)" % (i , k )) 
# ❖ While 문으로 바꾸시오
# 문제 
# ❖ 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 
# 쥐 한 마리가 하루에 20g씩의 쌀을 먹고, 10일(10,20,30)마다 
# 쥐의 수가 2배씩 증가한다. 
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까. 
# 그리고 쥐는 총 몇 마리 인가? 
# (쌀 한 통 =  1kg)(쌀을 먹은 후 2배 증가하는 조건)


