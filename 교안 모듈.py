# PYTHON_PROGRAMMING  모듈 
# 모듈 
# ❖ 정의  
# • 모듈이란 함수나 변수 또는 클래스 들을 모아 놓은 파일이다. • 파이썬에서는 자주 사용하는 기능들을 표준 모듈로 구성해두어 함께  설치하므로 해당 모듈들을 언제든지 불러와 사용할 수 있다. 
# ❖ 표준모듈 : 이미 설치된 모듈 (파이썬에서 정의된모듈)    
# ❖ 사용자모듈 : 개발자(사용자)가 직접 정의한 모듈    
# ❖ 외부 모듈을 불러서 사용할 때는 import라는 키워드를 사용함.   
# 예제 
  
# import math  
  
# print(math.pi)  
# print(math.factorial(5)) # 5!= 5x4x3x2x1  
# print(math.sqrt(5))  
# print(math.log10(2))  
  
# - Import선언은 모듈에 정의된 변수, 함수, 클래스들을 전부   현재 모듈로 불러옴  
# - 불러온 이후에는 마치 우리 모듈 내부에 정의된 것처럼 자유롭게 호출함  - 다른 모듈의 함수나 변수를 사용할 때는 이름 앞에 모듈명을 명시하여   소속을 밝히고 사용함(중복방지)  
  
 
# 예제 
  
# from math import factorial, sqrt, pi    
# print(factorial(5))  
# print(sqrt(5))  
# print(log10(2))  
 
# 예제 
# from math import factorial, sqrt, pi  import math  
  
# print(factorial(5))  
# print(sqrt(5))  
# print(math.log10(2))  
# print(math.log10(3))  
# print(math.gcd(12,18)) #최대공약수 
# 예제 
# import statistics  
  
# points = [65, 75, 55]  
# print('평균 : ', statistics.mean(points))  
# print('분산 : ', statistics.variance(points))  
# print('표준편차 : ', statistics.stdev(points))  
# #-----------------------------------------  import statistics as st  
  
# points = [65, 75, 55]  
# print('평균 : ', st.mean(points))  
# print('분산 : ', st.variance(points))  
# print('표준편차 : ', st.stdev(points))  
  
 
# 예제 
# inch =2.54  
  
# def calc_sum(end):  
#  sum_=0  
#  for n in range(end+1):  
#  sum_ +=n  
#  return sum_  
# def info():  
#  print("모듈 임포트!! 연습!")  
  
  
# ※ 위의 내용을 편집기로 작성하여 calculator.py로 저장해본다.   그리고 다음 예제 확인 
# 예제 
# import calculator as cal  
# from calculator import info  
  
# print("1인치 : %.2fcm"%cal.inch)  
# print("1~10까지의 누적합:",cal.calc_sum(10))    
# info()  
# info()  
# info()  
 
