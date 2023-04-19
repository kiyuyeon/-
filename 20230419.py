# #반지름을 입력받고 원의 둘레 구해보기
# pi = 3.14159265
# r= int(input("반지름이 값 : "))
# a = 2*pi*r
# b = r*r*pi

# print(pi)
# print(r)

# print("원의둘레 =",a)
# print("원의넓이 =",b)

# #input을 이용해서 숫자를 입력받는 방법
# number = int(input("숫자 입력 : "))
# print("number: " ,number)

# number += 10
# print("number: " ,number)

# number += 20
# print("number: " ,number)

# number += 30
# print("number: " ,number)

# #input 기본
# string = input("글자 입력 : ")
# string += "!"
# print("string = ",string)
# string += "!"
# print("string = ",string)

# string = input("인사말 입력 : ")
# print(string)

# print(type(string))

# string = int(string)
# print(string)
# print(type(string))

# #문자를 입력받고 숫자로 변환해보기
# string_a = input("입력 = A>")
# print(type(string_a))

# int_a = int(string_a)
# print(type(int_a))

# string_b = input("입력 = B>")
# print(type(string_b))

# int_b = int(string_b)
# print(type(int_b))

# print("문자열 자료 :",string_a + string_b)
# print("숫자 자료 :",int_a+int_b)

# #int 함수 float 함수 입력받고 출력하기
# output_a = int("52")
# output_b = float("52.273")

# print(type(output_a),output_a)
# print(type(output_b),output_b)

# #float 함수로 입력받고 계산하기
# intput_a = float(input("첫번째 숫자>"))
# intput_b = float(input("두번째 숫자>"))

# print("덧셈 결과 :",intput_a + intput_b)
# print("뺄셈 결과 :",intput_a - intput_b)
# print("곱셈 결과 :",intput_a * intput_b)
# print("나눗셈 결과 :",intput_a / intput_b)

# output_a = str(52)
# output_b = str(52.273)
# print(type(output_a),output_a)
# print(type(output_b),output_b)

# #inch 단위를 입력받고 cm 단위로 변환하기
# row_intch = int(input("인치단위 입력하기"))
# cm = row_intch * 2.54

# print(row_intch,"inch단위를 cm 단위를 변환합니다. ",cm,"cm입니다")

# #format 함수를 사용하여 출력해보기
# format_a = "{}만원".format(5000)
# format_b = "파이썬 열공하여 첫 연봉 {}만원".format(5000)
# format_c = "{} {} {}".format(3000,4000,5000)
# format_d = "{} {} {}".format(1,"문자열",True)

# print(format_a)
# print(format_b)
# print(format_c)
# print(format_d)

# #format 함수 활용 방법

# output_a = "{:d}".format(52) #기본
# #특정칸의 출력하기
# output_b = "{:5d}".format(52) #5칸
# output_c = "{:10d}".format(52) #10칸

# #빈칸을 0으로 채우기
# output_d = "{:05d}".format(52) #양수
# output_e = "{:05d}".format(-52) #음수
# print("# 기본")
# print("기본",output_a)

# print("# 특정칸 출력하기")
# print("특정칸의 출력하기 5칸",output_b)
# print("특정칸의 출력하기 10칸",output_c)

# print("# 빈칸을 0으로 채우기")
# print("format 값의 양수",output_d)
# print("format 값의 음수",output_e)

# #부동 소수점 출력 하기
# output_a = "{:f}".format(52.273) 
# output_b = "{:15f}".format(52.273 ) # 15칸 만들기  
# output_c = "{:+15f}".format(52.273) # 15칸에 부호 추가하기 
# output_d = "{:015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기

# print(output_a)
# print(output_b)
# print(output_c)
# print(output_d)

# #부동 소수점 아래 지정하기
# output_a = "{:15.3f}".format(52.273) #15칸 뛰고 소수점 3자리수 만 나옴
# output_b = "{:15.2f}".format(52.273 ) #15칸 뛰고 소수점 2자리수 만 나옴
# output_c = "{:+15.1f}".format(52.273) #15칸 뛰고 소수점 1자리수 만 나옴

# print(output_a)
# print(output_b)
# print(output_c)

# # 의미 없는 소수점 제거하기
# output_a = "{:.g}".format(52.0) 
# print(output_a)

# #upper , lower 사용하기 비파괴적 함수
# a = "Hello World"
# print(a.upper())
# print(a.lower)
# print(a)#비파괴적 함수이므로 원본은 바뀌지 않는다.

# b=a.upper()#b에서 a를 할당하여 파괴적인 함수로 변환한다.
# print(b)

# c=a.lower()#c에서 a를 할당하여 파괴적인 함수로 변환한다.
# print(c)

# #문자열 공백 제거하기 
# input_a = """
#     안녕하세요
# """
# print(input_a.strip())

# #문자열의 구성 파악하기

# print("TrainA10".isalnum())

# #문자열 찾기 find(),rfind()
# output_a = "안녕안녕하세요".find("안녕")
# print(output_a)

# output_b = "안녕안녕하세요".rfind("안녕")
# print(output_b)

# #in 연산자 문자열 확인하기
# print("안녕"in "안녕하세요")
# print("잘자"in "안녕하세요")

# #문자열 자르기 split
# a="10,20,30,40,50".split(",")
# print(a)

# "3 + 4 = {}".format(3+4)

# a= input("1번")
# b = input("2번")
# print("{}+{}={}".format(a,b,int(a)+int(b)))

# #구의 부피와 겉넓이

# r = int(input("반지름 넓이"))
# pi = 3.141592
# print("구의 부피 ={}".format(4/3*pi*r**3))
# print("구의 겉넓이 ={}".format(4*pi*r**2))

# #피타고라스의 정리 밑변**2 + 높이**2 = 빗편**2
# c = float(input("밑변의 길이"))
# d = float(input("높이의 길이"))
# print("빗변의 길이는 {}".format((c**2 + d**2)**0.5)) # 밑변**2 + 높이**2 = 빗편**2 이고 루트는 나올때 2/1을 나눠지기 때문에 0.5**

# # IF문 기본 사용
# number = int(input("정수 입력 >"))

# if number > 0:
#     print("양수입니다.")
# elif number <0 :
#     print("음수입니다.")
# else:
#     print("0입니다.")

# import datetime #날짜/시간과 관련된 기능을 가져온다.
# now = datetime.datetime.now() # now에 날짜/시간을 구한다.
# print("{}년{}월{}일{}시{}분{}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

# if 3<=now.month <=5:
#     print("이번 달은 {}월로 봄인다.".format(now.month))
# elif 6<=now.month <=8:
#     print("이번 달은 {}월로 여름인다.".format(now.month))
# elif 9<=now.month <=11  :
#     print("이번 달은 {}월로 가을인다.".format(now.month))
# else:
#     print("이번 달은 {}월로 겨울인다.".format(now.month))

#홀수 짝수 구별하기
num = int(input("정수를 입력하세요"))

if num%2==0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
    

#홀수 짝수 구별하기 in 사용
number = input("정수 입력 : ")
last_character = number[-1]

if last_character in "02468":
    print("짝수입니다.")
else:
    print("홀수입니다.")