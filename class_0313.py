# print("========================\n")
# print("\t /)/)")
# print("\t(  ..)")
# print("\t(  >♡")
# print("    Have a good Time.\n")
# print("========================\n")

# print("\n")

# print("\t""\t""###회비 정보###")
# print("=================================================")
# print("이름\t""\t""나이\t""전화번호\t""회비")
# print("=================================================")
# print("홍길동\t""\t""\"15\"\t""010-123-1234\t""\\20,000")
# print("임꺽정\t""\t""\"20\"\t""010-234-2345\t""\\30,000")
# print("김말이\t""\t""\"28\"\t""010-345-3456\t""\\50,000")
# print("-------------------------------------------------")
# print("총합계\t""\t""\t""\t""\t""\\100,000")
# print("=================================================")

#강사님 답
# print("=====================")
# print("\t /)/)")
# print("\t( ..)")
# print("\t( >♥)")
# print(" Have a Good Time.")
# print("=====================")
# print("\t #### 회비 정보 ####")
# print("========================================")
# print("이름\t나이\t전화번호\t회비")
# print("========================================")
# print('홍길동\t"15"\t010-123-1234\t\\20,000')
# print("임꺽정\t\"20\"\t010-234-2345\t\\30,000")#이름 뒤에 왜... '\'두번 들어갈까..? 왜 \t\으로 들어가는 걸까?
# print("김말이\t\"28\"\t010-345-3456\t\\50,000")
# print("----------------------------------------")
# print("총합계\t\t\t\t\\100,000")
# print("========================================")

# print(123+123)

# print(542-242)

# print(2*123)

# print(120/3)

# print("덧셈 결과 : ",123+123)
# #데이터랑 데이터 사이를 구분할 때 ,를 사용한다. 문자열과 문자열, 문자열과 숫자열 등등 모든 구분할때 사용)
# print("뺄셈 결과 :",542-242)
# print("곱셈 결과 :",2*123)
# print("나눗셈 결과 :",123/3)

# print("12 + 54 = ",12+54,"입니다.")
# print("268 - 42 = ",268-42,"입니다.")
# print("2 * 23 = ",2*23,"입니다.")
# print("120 / 3 = ",120/3,"입니다.")
#,연산자가 들어가면 ' 앞뒤로 공백이 발생한다.
#n진수

# print(0b01111011)
# print(0o173)
# print(0x7b)
# print(123)
# #값은 다 같은데...정수형태가 다르다.print는 어떤 정수형태여도 10진 형태로 표현된다.

# print("2진수 : ",bin(0b01111011))#bin(2진수),oct(8진수),hex(10진수)-정수형태를 지정해 주는 함수
# print("8진수 : ",oct(0b01111011))
# print("16진수 :",hex(0b01111011))
# print("10진수 :",0b01111011)

# print("%d"% 123)
# # print("%d%d%" 123)#첫번째 칸에는 들어갈 정수가 있는데 두번째 칸에는 들어갈 정수가 없어서 오류가 뜬다.
# # print("%d"%(123,321))#들어갈칸은 하나인데 호출될 정수가 두가지 있어서 오류가 뜬다.
# #중간 괄호를 벗기면 첫 정수가 서식제어문에 들어가고 뒤에 있는 정수는 그냥 출력이 된다.
##print("%d"%123,321)
# print("%d%d"%(123,321))
# print("%d+%d=%d"%(123,321,123+321))
# #서식제어문을 쓸 때 %를 사용한다.


# print("10진 정수 : %d"% 123)
# print("10진 정수 : %d"% 0o173)
# print("10진 정수 : %d"% 0x7b)

# print("8진 정수 : %o"% 123)
# print("8진 정수 : %o"% 0o173)
# print("8진 정수 : %o"% 0x7b)

# print("16진 정수 : %x"% 123)
# print("16진 정수 : %x"% 0o173)
# print("16진 정수 : %x"% 0x7b)
# #어떤 형태로 있든지 서식제어문 형태에 맞춰서 출력 된다.

# print(" 정수 표현 : %d"% 123)
# print(" 정수 표현 : %d"% 123.123)#(실수값을 반올림이 아니고 짤려서 정수만 표현됨)
# print(" 정수 표현 : %d %d"% (123,456))

# print("\n 실수 표현 : %f"% 456)
# print(" 실수 표현 : %f"% 456.456)
# print(" 실수 표현 : %f %f"% (456.456, 123.123))

# print("문자 표현 : %c %c"%("한","글"))
# print("문자 표현 : %c %c"%('표','현'))

# print("\n문자열 표현 : %s"%"안녕")
# print("문자열 표현 : %s\t%s"%("문자열","표현방식"))

# print("%c %c "%('a','A'))
# print("%c %c "%(97,65))#%c문자 상수를 문자로 바꿔주는 제어 문자다(소문자-대문자는 32다. 확인 필요)
# # print("%c %c "%(97,65))
# #아스키 코드 48(0(숫자)),65(A)만 외워라... 소문자와 대문자 변환로 생각해야한다...

# print("기본 값:%d"% 123)
# print("설정 값:%5d"% 123)#5는 칸수를 의미 양수는 오른쪽, 음수는 왼쪽으로 정렬 
# #(\t는 8칸이지만 이거는 칸수를 지정할 수 있다.그리고 왼쪽부터 지정, 8칸을 넘어가면 8칸이 더 생기지만 요거는 무시됨)
# print("설정 값:%05d"% 123)#5칸 중에 남은 곳에 0으로 표현된다.
# print("설정 값:%5d%5d"% (123,123))
# print("설정 값:%-5d%-5d" % (123,123))

# print("기본 값 :%f" % 123.45678)

# print("설정 값 : %10.3f" % 123.45678)
# # %a,bf 에서 a는 소수점을 포함한 전체칸 확보수
# #b는 표현할 소수자리지정[단 반올림해서 출력됨]
# print("설정 값 : %3.1f" % 123.45678)
# print("설정 값 : %1.1f" % 123.45678)

# print("설정 값 : %.2f" % 123.45678)
#************** #이해 전혀 안됨...힝.. ㅜ***영상 다시 보기!!!

# print("기본 값 :%s" % "python test") 
# print("설정 값 :%20s" % "python test")
# print("1234567890123456789012345678901234567890")
# print("%10s%10s"%("대한민국","만세"))
# print("설정 값 :%20.4s" % "python test")

# print("============출력결과===============")
# print("%-6s:%s"%("이름","홍길동"))
# print("%s%8s"%("이름",":홍길동"))

# print("%-4s:%s"%("나이","20"))
# print("%s%5s"%("나이",":20"))
# print("%-4s:%d"%("나이",20))

# print("%-6s:%s-%s-%s"%("Tel","010","1234","1234"))
# print("%s%7s-%s-%s"%("Tel",":010","1234","1234"))
# print("%-6s:%s"%("Tel","010-1234-1234"))
# print("%s%17s"%("Tel",":010-1234-1234"))
# #'-'요 아이는 칸을 0.5만 차지 하는가!?
# print("%-6s:%03d-%d-%d"%("Tel",10,1234,1234))

# print("%-5c:%1.1f"%("키",178.5))
# print("%s%10s"%("키",":178.5"))

# print("%-7s:%d"%("몸무게",75))
# print("%s%7s"%("몸무게",":75"))

# print("%-7s:%s"%("혈액형","O"))
# print("%s%6s"%("혈액형",":O"))
# print("%-7s:%c"%("혈액형",79))

# #print(12345678901234567890)