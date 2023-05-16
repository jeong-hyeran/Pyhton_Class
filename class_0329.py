# ❖ 하나의 대상을 선택하여 키값과 값을 입력받아 저장 후 출력 하시오 이름(key) 입력 : 겐지 
# 값(value) 입력 : 수리검 
# 이름(key) 입력 : 맥크리 
# 값(value) 입력 : 섬광탄 
# 이름(key) 입력 : 파라 
# 값(value) 입력 : 로켓런처 
# 이름(key) 입력 : 리퍼 
# 값(value) 입력 : 샷건 
# 이름(key) 입력 : 솔저 
# 값(value) 입력 : 나선로켓 
# {'솔저': '나선로켓', '맥크리': '섬광탄', '리퍼': '샷건', '파라': '로켓런처', '겐지': '수 리검'}
# #=> 강사님 풀이
# overWatch ={}

# for i in range(5):
#     name = input("이름 입력 : ")
#     skill = input("스킬 입력 : ")
#     overWatch[name]=skill #==>이게 무슨 말일까..?
# print(overWatch)

# 키는 박스 이름..!!
# 키이름이 동일하면 새로 만들어지는게 아니라 수정된다.
# 키 값은 중복 될 수 없다!!

# import collections
# #순서있는 사전
# overWatch = collections.OrderedDict()
# i=0; name=""; val = ""
# for i in range(5):
#     name = input("이름(key) 입력 : ")
#     val = input("값(value) 입력 : ")
#     overWatch[name]=val
# print(overWatch)

# 딕셔너리 함수 

# num = {1:"일",2:"이",3:"삼",4:"사"}
# print('keys()키: ', num.keys())
# print()
# print('values()값: ', num.values())

# num = { 1:"일" , 2:'이' , 3:'삼',4:"사"} 
# print("num.keys() : ",num.keys()) 
# print("list(num) : ",list(num)) 
# print('list(num.keys()) : ' , list(num.keys())) 
# print() 
# print("num.values() : ",num.values()) 
# print("list(num.values()) : ",list(num.values()))

# # =>출력값
# num.keys() :  dict_keys([1, 2, 3, 4])
# list(num) :  [1, 2, 3, 4]
# list(num.keys()) :  [1, 2, 3, 4]

# num.values() :  dict_values(['일', '이', '삼', '사'])
# list(num.values()) :  ['일', '이', '삼', '사']

# singer = {} 
# singer['이름']=input("가수 이름 입력 : ") 
# singer['구성원']=input("인원수 입력 : ") 
# singer['대표곡']=input("대표곡 입력 : ") 

# for i in singer.keys(): #키즈하면 완벽한 리스트는 아니지만 형태를 가지고 있다.
#     print('%s : %s' % (i,singer[i]))
# print(singer) #=>딕션너리 제대로 되어있는지 확인하려면 이렇게!

# menu={}; bl = True; num = 0 
# while bl: 
#     print("1.메뉴 등록"); 
#     print("2.메뉴별 가격 보기"); 
#     print("3.가격 수정"); print("4.종료") 
#     num=int(input(">>> ")) 
#     if num == 1: 
#         name = input("메뉴 입력 : "); menu[name] = input("가격 입력 : ") 
#     elif num == 2: 
#         for i in menu.keys(): 
#             print(i,":",menu[i]) 
#     elif num == 3: 
#         name = input("수정할 목록 입력"); 
#         menu[name] = input("수정가격 : ") 
#     elif num ==4: 
#         print("프로그램 종료 합니다") 
#         bl = False

# 버그 수정메뉴에서 추가가 된다.
# 메뉴 등록인데 수정이 된다.

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} 
# print(num) 
# print("num.get(3) : ",num.get(3)) 
# print("num.get(9) : ",num.get(9)) #=> 아무것도 지정하지 않으면None
# print("num.get(0) : ",num.get(0,'없음')) #=>'없음'을 지정해서 출력됨
# # 지정값은 아무거나 들어감
# su = int(input("찾고자하는 키 입력 : ")) 
# if num.get(su) == None: 
#     print("값이 없습니다") 
# else: 
#     print(num.get(su)) 

# => 출력값
# {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오'}
# num.get(3) :  삼
# num.get(9) :  None
# num.get(0) :  없음
# 찾고자하는 키 입력 :

# # 버그 수정
# menu={}; bl = True; num = 0 
# while bl: 
#     print("1.메뉴 등록"); 
#     print("2.메뉴별 가격 보기"); 
#     print("3.가격 수정"); print("4.종료") 
#     num=int(input(">>> ")) 
#     if num == 1: 
#         name = input("메뉴 입력 : ")
#         menu[name] = input("가격 입력 : ")
#         # if name.keys() == name.keys(): print("이미 등록 된 메뉴입니다.")
#         # if name == name: print("이미 등록 된 메뉴입니다.") 
#     elif num == 2: 
#         for i in menu.keys(): 
#             print(i,":",menu[i]) 
#     elif num == 3: 
#         name = input("수정할 목록 입력"); 
#         if name == name:menu[name] = input("수정가격 : ") 
#         else:print("등록된 메뉴가 없습니다.")
#     elif num ==4: 
#         print("프로그램 종료 합니다") 
#         bl = False

# # 강사님 풀이
# menu={}; bl = True; num = 0 
# while bl: 
#     print("1.메뉴 등록"); 
#     print("2.메뉴별 가격 보기"); 
#     print("3.가격 수정"); print("4.종료") 
#     num=int(input(">>> ")) 
#     if num == 1: 
#         name = input("메뉴 입력 : ")
#         if menu.get(name)!= None: ##
#             print("이미 등록된 메뉴입니다.!")##
#         else:##
#             menu[name] = input("가격 입력 : ") 
#     elif num == 2: 
#         for i in menu.keys(): 
#             print(i,":",menu[i]) 
#     elif num == 3: 
#         name = input("수정할 목록 입력 : ")
#         if menu.get(name) == None :##
#             print("등록되지 않은 메뉴입니다.!!")##
#         else:##
#             menu[name] = input("수정가격 : ") 
#     elif num ==4: 
#         print("프로그램 종료 합니다") 
#         bl = False



# student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'} 
# print(student['학번']) 
# print(student['이름']) 
# print(student['학과']) 
# print() 
# print(student.items()) 
# print() 
# print(student)

# =>출력값
# 1234
# 홍길동
# it학과

# dict_items([('학번', 1234), ('이름', '홍길동'), ('학과', 'it학과')])
# =>키, 벨류 리스트 나열해준다.
# {'학번': 1234, '이름': '홍길동', '학과': 'it학과'}

# name={ '이순신':"거북선",'세종대왕':'훈민정음','파이썬':'프로그래밍 언어'} 
# for key,value in name.items(): 
#     print(key,":",value) 

# print("삭제 : ",name.clear()) 
# print("삭제 후 값:",name)

# =>출력값
# 이순신 : 거북선
# 세종대왕 : 훈민정음
# 파이썬 : 프로그래밍 언어
# 삭제 :  None
# 삭제 후 값: {}

# 언페킹.........
# 튜플에서 제일 중요한데 언페킹(투플로 만드는것),페킹???
# clear는 초기화 

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} 
# print("변경전 값 : ",num) 
# print() 
# print("num.setdefault(9) : ",num.setdefault(9,"구~우")) 
# print() 
# print("변경전 후 : ",num) 
# print() 
# # print("num.get(9)번째 value : ",num.get(9))
# print("num.get(9)번째 value : ",num.setdefault(9))

# =>출력값
# 변경전 값 :  {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오'}
# num.setdefault(9) :  구~우
# 변경전 후 :  {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 9: '구~우'}
# num.get(9)번째 value :  구~우

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} 
# aaa={6:"육",7:"칠",8:"팔"}
    # num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} 
    # aaa={5:"오~오",7:"칠",8:"팔" }
    # num.update(aaa)
    # print("update 후 num : ",num)    
    # =>출력값
    # update 후 num :  {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오~오', 7: '칠', 8: '팔'}
    # 키 값이 중복되면.. 갱신이 된다.!!
# print(num+aaa)=> 연산이 안되는 피연산자, 딕셔너리는 연산 불가
# print("update 전 num : ",num) 
# num.update(aaa) 

# print("update 후 num : ",num)

# =>출력값
# update 전 num :  {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오'}
# update 후 num :  {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔'}

# dic = {} 
# ls = [] 

# ls.append(input("등록할 키값 입력 : ")) 
# ls.append(input("등록할 키값 입력 : ")) 
# ls.append(input("등록할 키값 입력 : ")) 

# dic = dic.fromkeys(ls) 
# print("dic키 설정 : ",dic) 

# dic=dic.fromkeys(ls,0)#=>0 이 부분은 지정해서 바꿀 수 있다. 
# print("dic 키&값 설정 : ",dic)

# print(ls)

# =>출력값(입력값:잉,엥,웅)
# 등록할 키값 입력 : 잉
# 등록할 키값 입력 : 엥
# 등록할 키값 입력 : 웅
# dic키 설정 :  {'잉': None, '엥': None, '웅': None}
# dic 키&값 설정 :  {'잉': 0, '엥': 0, '웅': 0}image.png
# 튜플을 이용해서 키값을 초기화 할때 사용하는 것

# num = { 1:"일" , 2:'이' , 3:'삼',4:"사"} 

# print("pop 전 num : ",num) 
# print('\npop(3) 실행 : ' , num.pop(3)) 
# print("\npop 실행 후 num : ",num)

# =>출력값
# pop 전 num :  {1: '일', 2: '이', 3: '삼', 4: '사'}
# pop은 추출 후 삭제,키를 지정해서 삭제 할 수 있어서 좋다.

# pop(3) 실행 :  삼

# pop 실행 후 num :  {1: '일', 2: '이', 4: '사'}

# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} 

# print("popitem() 전 num : %s\n" % num) 

# print("popitem 실행 결과 => ",end=" ") 
# print(num.popitem()) 
# print("popitem() 후 num : %s\n" % num) 

# print("popitem 실행 결과 => ",end=" ") 
# print(num.popitem()) 
# print("popitem() 후 num : %s" % num)

# =>출력값
# popitem() 전 num : {1: '일', 2: '이', 3: '삼', 4: '사', 5: '오'}

# popitem 실행 결과 =>  (5, '오')
# popitem() 후 num : {1: '일', 2: '이', 3: '삼', 4: '사'}

# popitem 실행 결과 =>  (4, '사')
# popitem() 후 num : {1: '일', 2: '이', 3: '삼'}
# 마지막 값이 하나씩 삭제 된다.
# 키와 벨류를 아이템으로....튜플로 리스트로 변경해서 마지막값을 삭제하는 함수를 만든것이다.???
# POP은 딕셔너리가 마지막이 없기때문에 마지막을 삭제 할 수 없어서
# popitem을 이용해서 마지막 값을 삭제한다.

# info={}; pe = []; bl = True; num = 0 
# while bl: 
#     print("1.인적사항 등록"); print("2.검색"); print("3.종료") 
#     num=int(input(">>> ")) 
#     if num == 1: 
#         pe.append(input("이름 입력 : ")); pe.append(input("점수 입력 : ")) 
#         info[pe[0]] = pe[1] #
#     elif num == 2: 
#         name = input("찾고자하는 학생 이름 입력 : ") 
#         if info.get(name) == None: print("찾고자 하는 학생이 없습니다") 
#         else: print(name,"님 점수 : ",info.get(name)) 
#     elif num ==3: 
#         print("프로그램 종료 합니다") 
#         bl = False
#     pe=[]
# print(info)
# print(pe)

#버그 두번째 등록한 학생 부터 검색 불가
# 딕셔너리가 상수
# 리스트를 초기화 시켜주면 된다.

# [set]
# 합집합 생각하면 된다.

# names={'허준','신사임당','권율','홍길동','허준'}

# print(type(names))
# print(len(names))
# print(names)

# =>출력값
# <class 'set'>
# 4
# {'권율', '신사임당', '홍길동', '허준'}
# 왜 허준은 어디갔데에엥? 중복값이라!!!
# 똑같게 출력하면 순서가 뒤바뀐다.. 순서개념이 없기 때문!
# names={'허준 ','신사임당','권율','홍길

# s = set({}) #=> 세트 자료형은 꼭 함수로 초기화를 해야한다.
# print(type(s)) 

# print(set('programming')) 
# print(set([12,15,17,11,15])) 

# dic = {'a':1, 'b':2, 'c':3} #딕셔너리는 키값만..

# print(set(dic))

# =>출력값
# <class 'dict'>
# {'o', 'g', 'i', 'm', 'r', 'p', 'a', 'n'}
# {17, 11, 12, 15}
# {'c', 'a', 'b'}
# 세트 함수를 이용해서 자료형을 바꿀 수 있다.

# for x in {'가','나','다','라'}: 
#  print(x) 
# # 출력값은 순서가 뒤죽박죽.. 왜 인덱스가 존재하지 않기 때문이다.

# asia = {'korea','china','japan'} 
# print(asia) 

# asia.add('thailand') 
# print(asia) 
# asia.add('china') 
# print(asia) 
# asia.remove('japan') 

# print(asia)

# =>출력값
# {'china', 'korea', 'japan'}
# {'china', 'korea', 'thailand', 'japan'}
# {'china', 'korea', 'thailand', 'japan'}
# {'china', 'korea', 'thailand'}