# PYTHON_PROGRAMMING 튜플
# Tuple 
# ❖ Tuple 
# • 사전적 의미는 tuple과 list가 비슷 
# - 리스트는 “목록“ 
# - 튜플은 “n개의 요소로 된 집합“ 
# ❖ 파이썬의 list와 tuple의 차이 
# • List는 데이터 변경 가능(리스트 생성 후 추가/수정/삭제 가능) • Tuple은 데이터 변경 불가능(튜플 생성 후 추가/수정/삭제 불가능) • List는 이름 그대로 목록 형식의 데이터를 다루는 데 적합 
# • Tuple은 위경도 좌표나 rgb색상처럼 작은 규모의 자료구조를 구성하기에 적합
# 예제 
# ❖ 튜플의 생성 
# ▪ 리스트는 대괄호[ ]로 생성하고 튜플은 괄호( )로 생성.  ▪ 하나의 값을 저장 할때는 ,(콤마)를 붙여줘야 한다. ▪ 괄호 생략이 가능하다 
# tp = (10,20,30) 
# print("tp : ",tp) 
# print("tp type : ",type(tp)) 
# print("tp len : ",len(tp))
# 예제 
# tp1 = 10,20,30 
# print("tp1 : ",tp1) 
# print("tp1 type : ",type(tp1)) 
# print("tp1[0] type : ",type(tp1[0])) tp1[0] = 100 #에러 발생
# 예제 
# tpType = "문자열",100,1.111 
# print("tpType : ",tpType) 
# print("type : ",type(tpType)) 
# print("tpType[0] type : ",type(tpType[0])) print("tpType[1] type : ",type(tpType[1])) print("tpType[2] type : ",type(tpType[2]))
# 예제 
# ▪ 튜플은 괄호를 생략 가능. 단, 하나의 항목만 가진 튜플을 만들 때는 주의 
# tpInt = (10) 
# print("tpInt : ",type(tpInt)); #<class ‘int’> 
# tpT1 = (10,) 
# Print(“tpT1 : “,type(tpT1)); #<class ‘tuple’> 
# tpT2 = 10, 
# print("tpT2 : ",type(tpT2)); #<class ‘tuple’>
# 예제 
# tt1 = ( 10 , 20 , 30 , 40 ) 
# tt2 = tt1[0]+tt1[1]+tt1[2]+tt1[3] print("튜플 합 : %d" % tt2) 
# print("tt1[1:3] : " , tt1[1:3]) print("tt1[1:] : " , tt1[1:]) 
# print("tt1[:3] : " , tt1[:3])
# 예제 
# a = 1,2,3 
# b = 4,5,6 
# c = a+b 
# print("a : ",a) print("b : ",b) print("c : ",c)
# 예제 ( packing & unpacking ) 
# pack = 1,2,"패킹" 
# print("packing\npack : ",pack) 
# a,b,c = pack 
# print("unpacking\na:",a,"b:",b,"c:",c)
# 튜플 함수 
# 함 수 설 명 사용법 index() 튜플 내 요소의 첨자를 알려 줌 tp.index(값) count() 일차하는 요소의 개수를 알려 줌 tp.count(값)
# tp = 100,200,"함수",100,'개수' 
# print("tp안의 200의 위치 : " ,tp.index(200),"번째 인덱스") print("tp안의 100의 개수 : ",tp.count(100)," 개") 
# 문제 
# ❖ 여러 개의 값을 패킹시킨 후 저장되어 있는 값을 빼내어 출력 하시오 (저장되어 있는 값은 몇 개나 있는지 알 수 없는 상태이다) (5개 값 저장) 튜플의 값을 리스트에 저장하시오 
# ---------------------------------------------------- ❖ 아래와 같이 출력 시키시오 
# (튜플) (리스트) 
# 회사정보 : 삼성전자 
# 제품명 : 겔럭시 
# 가격정보 : 100원 
# 출시일 : 미정 
# ---------------------------------------------------- ❖ 위의 내용을 업데이트 하시오.(변경은 리스트 함수 사용) : [2] = 110 (x) 가 격 : 100 -> 110 
# 출시일 : 미정 -> 이번달말
# 문제 풀이 
# #1번 문제 풀이 
# tp = 10,20,"튜플",1.11,'파이썬' ls = [] 
# i=0 
# for i in range(len(tp)): 
# ls.append(tp[i]) 
# print("tp : ",tp) 
# print("ls : ",ls) 
# ls2=list(tp) 
# print("ls2 : ",ls2)
# 문제 풀이 
# #2번문제 
# tp = "회사정보","제품명","가격정보","출시일" ls = ["삼성전자","겔럭시","100원","미정"] i=0 
# for i in range(len(ls)): 
# print("%5s\t"%tp[i],":",ls[i]) 
# for i in range(len(ls)): 
# print("{}\t:{:<5}".format(tp[i],ls[i])) for i in range(len(ls)): 
# print("{1}\t:{0:<5}".format(tp[i],ls[i])) for i in range(len(ls)): 
# print("{}\t:{:=^10}".format(tp[i],ls[i]))
# 문제 풀이 
# #3번 문제 풀이 
# print("100원 인덱스:",ls.index("100원")) print("출시일 인덱스:",ls.index("미정")) ls.insert(2,"110원") 
# ls.insert(3,"이번달말") 
# print(ls) 
# ls.remove("100원") 
# ls.remove("미정") 
# print(len(ls)) 
# for i in range(len(ls)): 
# print("%-5s"%tp[i],"\t:",ls[i])


# [딕셔너리]
# PYTHON_PROGRAMMING 딕셔너리
# Dictionary 
# ❖ 딕셔너리의 
# • 리스트와 비슷, 리스트처럼 첨자를 이용해서 요소에 접근 
# • 딕셔너리의 첨자는 키(key) 
# • 이 첨자 , 키가가리크는 곳에 저장되는 데이터를 값(value) 
# ❖ 탐색 속도가 빠르고, 사용하기도 편리 
# ❖ 특정 슬롯에 새로운 키-값을 입력하거나 딕셔너리 안에 있는 요소를 참조할 때 는 리스트와 튜플에서처럼 대괄호 []를 이용
# 딕셔너리 생성 
# ❖ 딕셔너리의 생성 
# ▪ 중괄호{ }로 묶여 있으며 키와 값의 쌍으로 이루어짐 ▪ 딕셔너리 변수 = { 키1 : 값1, 키2 : 값2, 키3 : 값3 . . . } ▪ dic1 = {1:'a' , 2:'b' , 3:'c'} 
# ▪ dic2 = {'이름':'홍길동' , ‘연락처':010... , 주소:'산골'}
# 딕셔너리 생성 
# student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'} print(student) 
# mobile = {"품명":"겔럭시","가격":100,"크기":10} print(mobile)
# 딕셔너리 생성 
# impo = {} 
# impo['파이썬'] = 'www.python.org' impo['네이버']='www.naver.com' impo['구글']='www.google.com' 
# print("파이썬 : ",impo['파이썬']) print("네이버 : ",impo['네이버']) print("구글 : ",impo['구글'])
# 딕셔너리 생성 
# impo = {} 
# name = input('키값 입력 : ') val = input('값 입력') 
# impo[name] = val 
# print(name,": ",impo[name])
# 문제 
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
# 딕셔너리 함수 
# 함 수 설 명 사용법 Keys() key list dic.keys() Values() value list dic.values() 
# Items() key,value 리스트 dic.items() Clear() 항목 모두 삭제 dic.clear() 
# Get() 키가 없으면 : None 
# 키가이 있으면 : value 출력 dic.get(키)
# 딕셔너리 함수 
# 함 수 설 명 사용법 Setdefault() key가 없으면 추가 설정 dic.setdefault(키,값) Update() 다른 사전의 내용으로 갱신 dic.update(obj) 
# Pop() Key를 이용해서 해당하는 값을 지움 dic.pop(key) 
# Fromkeys() (key,value)리스트나 튜플로 설정 dic=dic.fromkeys(키)  or (키,값)
# 예제 
# num = { 1:"일" , 2:'이' , 3:'삼',4:"사"} 
# print('keys() 키: ' , num.keys()) print() 
# print('values() 값: ',num.values())
# 예제 
# num = { 1:"일" , 2:'이' , 3:'삼',4:"사"} 
# print("num.keys() : ",num.keys()) 
# print("list(num) : ",list(num)) 
# print('list(num.keys()) : ' , list(num.keys())) print() 
# print("num.values() : ",num.values()) print("list(num.values()) : ",list(num.values()))
# 예제 
# singer = {} 
# singer['이름']=input("가수 이름 입력 : ") singer['구성원']=input("인원수 입력 : ") singer['대표곡']=input("대표곡 입력 : ") 
# for i in singer.keys(): 
# print('%s : %s' % (i,singer[i]))
# 예제 
# menu={}; bl = True; num = 0 
# while bl: 
# print("1.메뉴 등록"); print("2.메뉴별 가격 보기"); print("3.가격 수정");print("4.종료") num=int(input(">>> ")) 
# if num == 1: 
# name = input("메뉴 입력 : "); menu[name] = input("가격 입력 : ") 
# elif num == 2: 
# for i in menu.keys(): 
# print(i,":",menu[i]) 
# elif num == 3: 
# name = input("수정할 목록 입력"); menu[name] = input("수정가격 : ") elif num ==4: 
# print("프로그램 종료 합니다") 
# bl = False
# 예제 
# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} 
# print(num) 
# print("num.get(3) : ",num.get(3)) 
# print("num.get(9) : ",num.get(9)) 
# print("num.get(0) : ",num.get(0,'없음')) 
# su = int(input("찾고자하는 키 입력 : ")) 
# if num.get(su) == None: 
# print("값이 없습니다") 
# else: 
# print(num.get(su)) 
# ❖ 이전 예제의 1,3번의 내용 수정. 1.메뉴가 존재한다면, 3.메뉴가 없다면
# Quiz  

# ❖ 네비게이션 만들기. (복습)
# 1.등록 
# 2.목적지 수정 
# 3.검색 
# 4.종료
##=> 행선지를 등록하면 (집-주소,회사-주소,키-벨류)
# 목적지 수정할 때 (등록되지 않은 목적지면 안내)
# 검색(집 하면 그 주소를 볼 수 있게)


# 예제 
# student = { '학번':1234 , '이름':'홍길동' , '학과':'it학과'} 
# print(student['학번']) 
# print(student['이름']) 
# print(student['학과']) 
# print() 
# print(student.items()) 
# print() 
# print(student)
# 예제 
# name={ '이순신':"거북선",'세종대왕':'훈민정음','파이썬':'프로그래밍 언어'} for key,value in name.items(): 
# print(key,":",value) 
# print("삭제 : ",name.clear()) 
# print("삭제 후 값:",name)
# 예제 
# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} 
# print("변경전 값 : ",num) 
# print() 
# print("num.setdefault(9) : ",num.setdefault(9,"구~우")) print() 
# print("변경전 후 : ",num) 
# print() 
# print("num.get(9)번째 value : ",num.get(9))
# 예제 
# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} aaa={6:"육",7:"칠",8:"팔"} 
# print("update 전 num : ",num) 
# num.update(aaa) 
# print("update 후 num : ",num)
# 예제 
# dic = {} 
# ls = [] 
# ls.append(input("등록할 키값 입력 : ")) ls.append(input("등록할 키값 입력 : ")) ls.append(input("등록할 키값 입력 : ")) 
# dic = dic.fromkeys(ls) 
# print("dic키 설정 : ",dic) 
# dic=dic.fromkeys(ls,0) 
# print("dic 키&값 설정 : ",dic)
# 예제 
# num = { 1:"일" , 2:'이' , 3:'삼',4:"사"} 
# print("pop 전 num : ",num) 
# print('\npop(3) 실행 : ' , num.pop(3)) print("\npop 실행 후 num : ",num)
# 예제 
# num = { 1:"일",2:"이",3:"삼",4:"사",5:"오"} print("popitem() 전 num : %s\n" % num) 
# print("popitem 실행 결과 => ",end=" ") print(num.popitem()) 
# print("popitem() 후 num : %s\n" % num) 
# print("popitem 실행 결과 => ",end=" ") print(num.popitem()) 
# print("popitem() 후 num : %s" % num)
# 예제 ( 1 ) 
# ❖ 실행 후 정상 동작하게 만드시오 
# info={}; pe = []; bl = True; num = 0 
# while bl: 
# print("1.인적사항 등록"); print("2.검색"); print("3.종료") 
# num=int(input(">>> ")) 
# if num == 1: 
# pe.append(input("이름 입력 : ")); pe.append(input("점수 입력 : ")) info[pe[0]] = pe[1] 
# elif num == 2: 
# name = input("찾고자하는 학생 이름 입력 : ") 
# if info.get(name) == None: print("찾고자 하는 학생이 없습니다") else: print(name,"님 점수 : ",info.get(name)) 
# elif num ==3: 
# print("프로그램 종료 합니다") 
# bl = False
