# PYTHON_PROGRAMMING 문자열
# 예제 
# Str = 'Have a nice day' 
# print("Str[0] : ",Str[0]) 
# print("Str[1] : ",Str[1]) 
# print("Str[2] : ",Str[2]) 
# print("Str[3] : ",Str[3]) 
# print() 
# print("문자열의 총 길이 : ",len(Str)) print("Str : ",Str) 
# ❖ 반복문으로 출력 하시오
# 예제 
# Str = 'Have a nice day' 
# for i in Str: 
# print(i,end="") 
# print() 
# for i in range(len(Str)): print(Str[i],end="")
# 문자열 slicing 
# Str = 'Have a nice day' 
# arr = Str[7:11] 
# print("Str : " ,Str) 
# print("arr : " , arr);
# 예제 
# Str = "즐거운 파이썬" 
# print("Str\t: " , Str) 
# print("Str[0]\t: " , Str[0]) print("Str[1:3] : " , Str[1:3]) print("Str[3: ] : " , Str[3 : ]) print("Str[ : 3] : " , Str[ : 3])
# 예제 
# Str = 'Have a' 
# print("변경 전 Str : ",Str) Str+=' nice day' 
# print("변경 후 Str : " , Str) print("Str * 3 : ",Str*3)
# 문자열 함수 
# 대문자/소문자의 변환
# 함 수 설 명 사용법 upper() 소문자를 대문자로 변경 Str.upper() lower() 대문자를 소문자로 변경 Str.lower() 
# swapcase() 대소문자를 상호 변경 Str.swapcase() title() 각 단어의 제일 앞 글자만 대문자로 변경 Str.title() 
# 예제 
# Str = 'Pythone is Easy. 그리고 programming 할만하다 ^^' print("Str : ",Str) 
# print() 
# print('Str.upper() : ',Str.upper()) #소문자를 대문자로 변경 print() 
# print('Str.lower() : ',Str.lower()) #대문자를 소문자로 변경 print() 
# print('Str.swapcase() : ',Str.swapcase()) #대소문자 상호 변경 print() 
# print('Str.title() : ',Str.title()) #각 단어의 첫번째 문자 대문자로 변경
# Quiz  
# ❖ 대문자는 소문자로, 특수문자, 숫자, 공백 다음의 첫 글자는 대문자로 변환 하시오 변경전 : NevEr -eVer 110gIVe up 
# 변경후 : Never -Ever 110Give Up
# 문자열 함수 
# 문자열 찾기
# 함 수 설 명 사용법 count() 찾을 문자열의 개수 Str.count(‘문자열‘) find() 찾을 문자열의 위치 없으면 -1 Str.find(‘문자열‘) rfind() 입력한 문자열이 존재하는 위치를 뒤 
# 에서부터 찾는다 없으면 -1Str.rfind(‘문자열’) 
# index() find()함수와 동일한 용도, 없으면 
# errorStr.index(‘문자열‘) 
# 예제 
# st = 'Have a nice day' 
# print("st : ",st) 
# print() 
# print("st안에 'a'문자 개수 : ",st.count('a')) print("st안에 'day'문자열 개수 : ",st.count('day')) print("st안에 'dak'문자열 개수 : ",st.count('dak'))
# Quiz  
# ❖ 이전에 문자의 개수를 세어주는 프로그램을 문자열 함수를 이용해서 바 꾸시오. 
# st = "It is a fun Python class" 
# cnt_a= cnt_s = cnt = 0 
# for i in st: 
# cnt+=1 
# if i == 'a': 
# cnt_a+=1 
# elif i == 's': 
# cnt_s+=1 
# print("총 개수 : ",cnt,"\na 개수:",cnt_a,"\ns 개수:",cnt_s)
# 예제 
# st = 'Have a nice day' 
# print("st : ",st) 
# print("find: 'day'위치 : ",st.find('day')) print("index: 'day'위치 : ",st.index('day')) print("find: 'kkk'위치 : ",st.find('kkk')) print("index: 'kkk'위치 : ",st.index('kkk'))
# 예제 
# st = 'Have a nice day' 
# print("st : ",st) 
# print("find: 'day'위치 : ",st.find('a')) print("find: 'day'위치 : ",st.find('a',2)) print("find: 'day'위치 : ",st.find('a',6)) print("find: 'day'위치 : ",st.find('a',14))
# Quiz  
# ❖ a의 총 개수와 첨자의 위치를 출력 하시오 
# ❖ st = 'Have a nice day Have a nice day Have a nice day' ❖ 결과 : [1, 5, 13, 17, 21, 29, 33, 37, 45]
# 문자열 함수 
# 문자열 변경
# 함 수 설 명 사용법 

# strip() 문자열 양 끝 문자 제거 양쪽 공백 제거 
# rstrip() 문자열 끝 문자 제거 오른쪽 공백 제거 
# lstrip() 문자열 처음 문자 제거 왼쪽 공백 제거 
# Str.strip()  
# or 
# Str.strip(‘문자’) 
# Str.rstrip()  
# or 
# Str.rstrip(‘문자’) 
# Str.lstrip()  
# or 
# Str.lstrip(‘문자’) 

# replace() 기존 문자열 새 문자열로 치환 Str.replace(‘기존 문 자열’,’치환문자열’) 
# 예제 
# st = ' 파 이 썬 ' 
# print('st\t\t:{}{}{}'.format('*',st,'*')) 
# print() 
# print('st.strip()\t:{}{}{}'.format('*',st.strip(),'*'))
# 예제 
# st = '파이썬파' 
# print('st\t\t:' ,st) 
# print() 
# print('Str.strip("파")\t:', st.strip('파')) 
# print("========================================") 
# st = '파이썬' 
# print('st\t\t:' ,st) 
# print() 
# print('Str.strip("파")\t:', st.strip('파'))
# 예제 
# st = '---파---이---썬---' 
# print('st\t\t:',st) 
# print('st.strip("-")\t:',st.strip('-')) print('st.rstrip("-")\t:',st.rstrip('-')) print('st.lstrip("-")\t:',st.lstrip('-'))
# 예제 
# st = '2015/04/02' 
# print('st\t\t:',st) 
# print('replace()\t:',st.replace('/','.')) 
# print('replace([0:4])\t:',st.replace(st[0:4],'2017'))
# 많은 문자열 처리 
# st = """ 
# 오늘 하루도 즐겁게 오늘 하루도 행복하게 오늘 하루도 최선을 """ 
# print(st)
# Quiz  
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
# 문자열 함수 
# 문자열 변경
# 함 수 설 명 사용법 

# split() 문자 열을 공백이나 다른 문자로 분리 해서 리스트를 반환 
# Str.split() 
# or 
# Str.split(‘문자’) 

# splitlines() 행 단위로 분리(\n을 기준으로 나눈다) Str.splitlines() join 기존의 문자열 과 새 문자열 합해줌 Str.join(‘문자’) 
# 예제 
# st = 'Never ever give up' 
# print('st\t\t: ' , st) 
# print('st.split()\t: ',st.split())
# 예제 
# st = '하나:둘:셋' 
# print('st\t\t: ' , st) 
# print('st.split(:)\t: ',st.split(':')) 
# st = '일,이,삼' 
# print('st.split(,)\t: ',st.split(','))
# 예제 
# st = 'Never ever give up' 
# print('st : ',st) 
# print('st.splitlines(): ',st.splitlines()) st = ''' 
# Never ever give up 
# Never ever give up 
# ''' 
# print('st.splitlines(): ',st.splitlines()) st = "하나\n둘셋" 
# print('st.splitlines(): ',st.splitlines())
# 예제 
# Str = '123' 
# print('"%".join(123)\t: ','%'.join(Str)) 
# print('123.join("%a")\t: ',Str.join('%a')) 
# li=['','123','456'] 
# print('"공백".join([123,456])\t: '," ".join(li)) 
# li=['','안녕하세요','만나서 반갑습니다','행복한 하루 되세요^^'] 
# print('"엔터".join(li)\t: ',"\n\n".join(li))
# 문자열 함수 
# 문자열 정렬
# 함 수 설 명 사용법 Str.center(정수) 

# center() 숫자만큼 전체 자릿수를 잡은 후 문자 열을 가운데 배치 
# or 
# Str.center(정수,’값’) 

# ljust() 왼쪽에 붙여 출력 Str.ljust(정수) rjust() 오른쪽에 붙여 출력 Str.rjust(정수) 

# zfill() 오른쪽으로 붙여 쓰고 왼쪽 빈 공간은 0으로 채움 
# Str.zfill(정수) 

# 예제 
# Str = 'python' 
# print('Str\t\t: ',Str) 
# print('Str.center(10)\t: ',Str.center(10)) 
# print('Str.center(10,"-"): ',Str.center(10,'-')) 
# print('Str.ljust(10)\t: ',Str.ljust(10),Str.ljust(10)) 
# print('Str.rjust(10)\t: ',Str.rjust(10),Str.rjust(10)) 
# print('Str.zfill(10)\t: ',Str.zfill(10))
# Quiz  
# ❖ 아래의 값을 그림처럼 바꿔서 출력 하시오. 
# accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000"
# 풀이 
# accountBook = "shoes 03/02 59000, coffee 03/03 2500, food 03/04 7000, dress 03/13 130000" replaceAB = accountBook.split(',')#,기준으로 리스트로 저장 
# k=0 
# for i in replaceAB: 
# replaceAB[k]=i.lstrip() #각 문자열의 왼쪽 공백 삭제 후 저장(_coffee,_food,_dress) k+=1 
# kk='$ ' 
# print('item'.ljust(10),end='') 
# print('date'.ljust(10),end='') 
# print('$(price)'.ljust(10)) 
# for i in range(len(replaceAB)): 
# z=replaceAB[i].split() #공백을 기준으로 리스트로 저장 
# for k in range(len(z)): 
# if k == 0 : 
# print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력 
# elif k ==1 : 
# print(z[k].ljust(10),end="") #10칸 확보후 왼쪽 출력 
# elif k == 2 :  
# print("{:,}".format(int(z[k])).join(kk).ljust(10)) 
# 문자열 함수 
# 문자열 구성 파악 
# • True 또는 False를 반환
# 함 수 설 명 사용법 isdigit() 전체가 숫자로만 되어 있는가 Str.isdigit() isalpha() 전체가 글자(한글/영어)로 되어 있는가 Str.isalpha() isalnum() 전체가 글자와 숫자가 섞여 있는가 Str.isalnum() islower() 전체가 소문자로 되어 있는가 Str.islower() isupper() 전체가 대문자로 되어 있는가 Str.isupper() isspace() 전체가 공백 문자로 되어 있는가 Str.isspace() 
# 예제 
# Str = 'python te12st 1234' 
# print("Str.isdigit() : ",Str.isdigit())#숫자로만 구성 
# print("Str[9:11].isdigit() : ",Str[9:11].isdigit())#숫자로만 구성 
# print("Str.isalpha() : ",Str.isalpha())#글자로 구성 
# print("Str[:6].isalpha() : ",Str[:6].isalpha())#글자로 구성 
# print("Str.isalnum() : ",Str.isalnum())#글자 + 숫자 print("Str[7:13].isalnum() : ",Str[7:13].isalnum())#글자 + 숫자 
# print("Str.islower() : ",Str.islower())#소문자 
# print("Str.isupper() : ",Str.isupper())#대문자 
# print("Str.isspace() : ",Str.isspace())#공백
# # Quiz 
# ❖ 뒤의 주민번호를 ******* 로 변경 하시오 
# info = """ 
# jo 9abc08-3022023 
# cho 900402-1011232 
# test 1234567-1234567  
# lee 980908-3a2b0c3 
# kim 900514-2022023 
# """