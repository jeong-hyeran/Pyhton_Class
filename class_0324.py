# # 이중 포문을 와일 문으로 변환하는뎅..이중 와일문으로 변환
# for i in range ( 0 , 3 , 1): 
#     for k in range ( 0 , 5 , 1): 
#         if k == 3: 
#             break 
#         print("(i : %d\tk : %d)" % (i , k )) 

# print("---------------")
# i=0
# k=0
# while i<3 :
#     i+=1
#     # print(i-1) #확인 차 만듦
#     while k<5 :
#         k+=1
#         # print(k-1) #확인 차 만듦
#     # if k==3:
#     #     break
#         print("(i : %d\tk : %d)" % (i-1 , k-1 ))
## 못 풀었댜!!! 

# i=0
# while i < 3 :
#     k=0 #-> k의 초기화 값... 
#     while k < 5 :
#         if k == 3:
#             break
#         print("(i : %d\tk : %d)" % (i , k ))
#         k+=1
#     i+=1
# ##=> 순서대로 진행된다.!!
# # 23번 진행, 25번진행 되면서 26번 조건에 닿을때까지 29번까지 반복
# # 27번 break에 닿으면 30번으로 빠져나가서 반복


# ❖ 쌀 100통이 저장되어 있는 창고에 암수 1쌍의 쥐가 있다. 
# 쥐 한 마리가 하루에 20g씩의 쌀을 먹고, 10일(10,20,30)마다 
# 쥐의 수가 2배씩 증가한다. 
# 며칠 만에 창고의 쌀이 모두 쥐의 먹이가 될까. 
# 그리고 쥐는 총 몇 마리 인가? 
# (쌀 한 통 =  1kg)(쌀을 먹은 후 2배 증가하는 조건)
# --->>쌀을 먹은 후 2배 증가하는 조건 : 순서를 잘 생각해봐야한다.
# -->결과도 보내라!

#=>강사님 풀이 (사람 말을 그대로 옮겨라)
# rice=100*1000 #쌀을 그램으로 환산
# day =0; mouse=2
# while rice > 0:
#     day+=1
#     rice-=(mouse*20)
#     if day%10 == 0:
#         mouse*=2
# print("쌀을 다 먹은날 %d일이고 쥐는 총 %d마리입니다."%(day,mouse))



# to_day= 0 # 며칠만에 모두 먹이가 되었을까
# to_mouse=0 #총 몇 마리인가
# rice=1000 #쌀 한통 g
# to_rice=rice*100 # 총 쌀의 무게
# day1=20 #한 마리가 하루에 섭취하는 g
# day2=to_day*40 #두 마리가 하루에 섭취하는 g
# mouse=2 #최초 쥐
# cycle=10 #10일 마다 2배가 된다.
# cycle = 0
#  #
# day2=40
# while day2<100000: # 모든 쌀을 2마리의 쥐가 다 먹을때
#     # while cycle>10:
#     print("2마리의 쥐가%d일동안 %dg 먹음"%cycle,day2)
#     day2+=40
#     # cycle+=1

# while day2 < to_rice: # 40g씩(쥐 두마리) 모든 쌀을 다 먹을동안
#     # print(day2)#두마리가 모든 쌀을 다 섭취 
#     if day2 %10==0:day2*2 #10일 마다 2배를 표시해야함
#     print("10일 만에%d" %day2)
#     break
#     # day2*=2
    # print("%d마리가 %d일 만에 모든 쌀을 섭취"%to_mouse,to_day)

# while to_day < 11:
    
#     day2*=2
#     day2=to_day*40
#     print("%d일 동안, 두마리가 %dg을 섭취"%to_day,day2)

#[리스트-자료형]

# ls=[500,200,300,400]

# print("is:",ls) #>ls:500,200,300,400
# print("is:[0]",ls[0]) #>ls:500
# print("is:[1]",ls[1]) #>ls:200
# print("is:[2]",ls[2]) #>ls:300
# print("is:[3]",ls[3]) #>ls:400

# print("is:[-4]",ls[-4]) 
# print("is:[-3]",ls[-3]) 
# print("is:[-2]",ls[-2]) 
# print("is:[-1]",ls[-1])#=> 몇개의 인덱스가 있든 '-1'하면 맨 끝의 값을 출력할 수있다
# # 외쪽에서 부터 -찾아 들어간다?

#출력값
# is: [500, 200, 300, 400]
# is:[0] 500
# is:[1] 200
# is:[2] 300
# is:[3] 400

# is:[-4] 500
# is:[-3] 200
# is:[-2] 300
# is:[-1] 400

# ls =[0,0,0,0];Sum=0
# ls[0]=int(input("첫번째 숫자 입력 : "))
# ls[1]=int(input("두번째 숫자 입력 : "))
# ls[2]=int(input("세번째 숫자 입력 : "))
# ls[3]=int(input("네번째 숫자 입력 : "))
# Sum = ls[0] + ls[1] + ls[2] + ls[3]
# print("ls[0]:",ls[0])
# print("ls[1]:",ls[1])
# print("ls[2]:",ls[2])
# print("ls[3]:",ls[3])
# print("리스트의 합: %d"% Sum)

# ls = [0 , 0 , 0 , 0]; Sum = 0 
# #=> 여기 입력된 값은 아무 소용이 없다.그냥 박스만 만들기 위해 만들어둔것 
# #  대신 비워두면 안된다.
# ls[0]=int(input("첫번째 숫자 입력 : ")) 
# ls[1]=int(input("두번째 숫자 입력 : ")) 
# ls[2]=int(input("세번째 숫자 입력 : ")) 
# ls[3]=int(input("네번째 숫자 입력 : ")) 
# Sum = ls[0] + ls[1] + ls[2] + ls[3] 
# print("ls[0] :", ls[0]) 
# print("ls[1] :", ls[1]) 
# print("ls[2] :", ls[2]) 
# print("ls[3] :", ls[3]) 
# print("리스트의 합 : %d" % Sum)

# ls = [0 , 0 , 0 , 0]; Sum = 0 

# print("len(ls) : ",len(ls)) 
# #len (랭스)함수: 인덱스의 순번을 알려줌
# for i in range(len(ls)): 
#     ls[i]=int(input(str(i)+"째 숫자 입력 : ")) 
#     #정수형과 문자형 연산이 안되서 문자열로 변환
#     Sum += ls[i] 
# for i in range(len(ls)): 
#     print("ls[%d] :"% i,ls[i]) 
# print("리스트의 합 :", Sum) 

# 리스트 slicing -> 자르다
# ls = [10 , 20 , 30 , 40] 
# print("ls : ",ls) 
# print("\nls[1:3] => ls[1] ~ [2] :",ls[1:3]) 
    #첫번째:시작 인데스, 두번째:우리가 보는 몇번째 인덱스
# print("ls[0:3] => ls[0] ~ [2] :",ls[0:3]) 
# print("ls[2:] => ls[2] ~ [끝까지] :",ls[2:]) #아주많이 쓰이는 문법
# print("ls[:2] => ls[0] ~ [1] :",ls[:2])

# 리스트 (얕은 복사) -> 메모리의 주소 값만 복사
# ls =[10,20,30,40]
# arr =ls
# print("ls:{}ls,id:{}".format(ls,id(ls)))
# print("arr:{}arr,id:{}".format(arr,id(arr)))

# ls =[10,20,30,40]
# arr =ls
# arr[2]=20000 
# print("ls:{}ls,id:{}".format(ls,id(ls)))
# print("arr:{}arr,id:{}".format(arr,id(arr)))
# 주소 값은 계속 같다

# 리스트 (깊은 복사) 
# ls=[10,20,30,40]
# arr=ls[:]
# arr[2]=20000
# print("ls:{},ls id:{}".format(ls,id(ls)))
# print("arr:{},arr id:{}".format(arr,id(arr)))
# # 객채가 2개인것
# # 변수에다 값을 대입해 새롭게 정의한것

# import copy #=>가져오다,수입하다.
# ls=[10,20,30,40]
# #arr=ls[:]
# arr=copy.deepcopy(ls)#copy라는 모듈 안에 있는 딮카피를 가져와 사용한다는 출처를 보여준다.
# arr[2]='deepcopy'

# print("ls:{},ls id:{}".format(ls,id(ls)))
# print("arr:{},arr id:{}".format(arr,id(arr)))
# #깊은 복사는 딮카피, 슬라이싱 함수를 사용하는데
# # 가급적이면 딮카피를 사용 해야한다.


# # import copy #=>가져오다,수입하다.
# from copy import deepcopy #>이렇게 출처를 밝히면 아래에 copt.모듈을 표시 안해도 된다.!
# ls=[10,20,30,40]
# #arr=ls[:]
# arr=deepcopy(ls).
# arr[2]='deepcopy'

# print("ls:{},ls id:{}".format(ls,id(ls)))
# print("arr:{},arr id:{}".format(arr,id(arr)))



# # 표준함수
# # 미리 정의해둔 여러가지 함수
# # 내장함수
# # -인터프리터에 포함되어있다.
# # 외부함수
# # -외부함수는 인터프리터에 포함되지 않고 파일(모듈)로 저장되어있다가
# # 필요시 import라는 키워드를 사용해서 가져다 사용할 수 있다.
# # 미리 정의해놓은 표준함수는 가져오면 되고, 사용자 정의함수도 모률로
# # 저장해놓고 얼마든지 다른프로그램에서도 사용할 수 있다.

