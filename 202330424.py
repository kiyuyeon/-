# list_input_a = [1,2,3,4,5]

# output_a = map(lambda x: x*x, list_input_a)
# print("map 함수의 실행결과")
# print("map(power, list_input_a):",output_a)
# print("map(power, list_input_a):",list(output_a))
# print()

# output_b = filter(lambda x: x<3, list_input_a)
# print("filter 함수의 실행결과")
# print("filter(under3, list_input_a):",output_b)
# print("filter(under3, list_input_a):",list(output_b))
# print()

# file = open("basic.txt","w")

# file.write("Hello Python Programming...!")

# file.close()

# with open("basic.txt","w") as file:
# 	#파일에 텍스트를 씁니다.
# 	file.write("Hello Python Programming...!")


# import random 

# hanguls = list("가나다라마바사아자차카타파하")

# with open("info.txt","w")as file: #파일 쓰기모드로 엽니다.
#     for i in range(1000):
#         #랜덤한 값으로 변수를 생성합니다.
#         name = random.choice(hanguls) + random.choice(hanguls)
#         weight = random.randrange(40,100)
#         height = random.randrange(140,200)
#         #텍스트를 씁니다.
#         file.write("{}, {}, {} \n".format(name,weight,height))
        
        
# with open("info.txt","r") as file:
#     for line in file:
#         #변수를 선언합니다.
#         (name,weight,height) = line.strip().split(",")
        
#         #데이터가 문제가 있는지 확인합니다.
#         if (not name) or (not weight) or (not height):
#             continue
    
#         #결과를 계산합니다.
#         bmi = int(weight) / ((int(height)/100)**2)
#         result = ""
#         if 25<= bmi:
#             result ="과체중"
#         elif 18.5 <= bmi:
#             result = "정상 체중"
#         else:
#             result = "저체중"
        
#         #출력합니다.    
#         print('\n'.join([
#             "이름 : {}",
#             "몸무게 : {}",
#             "키 : {}",
#             "BMI : {}",
#             "결과 : {}"
#         ]).format(name,weight,height,bmi,result))
#         print()


# number = [1,2,3,4,5,6]
# print("::".join(map(str,number)))

# #홀수 구하기
# numbers = list(range(1,10+1))
# print(list(filter(lambda x : x%2==1,numbers)))
# print()

# try:
#     number_input_a = int(input("정수 입력"))
    
#     print("원의 반지름 : " , number_input_a)
#     print("원의 둘레 : ",2*3.14*number_input_a)
#     print("원의 넓이",3.14*number_input_a*number_input_a)
# except:
#     print("숫자만 입력해주세요")

# list_input_a = ["52","273","스파이","103"]

# list_number = []
# for item in list_input_a:
#     try:
#         float(item)
#         list_number.append(item)
#     except:
#         print("에러가 발생했습니다.")
#         pass
# print("{} 내부에 있는 숫자는".format(list_input_a))
# print("{}입니다.".format(list_number))

# #변수 선언
# list_number = [52,273,32,72,100]

# #try except 구문으로 예외를 처리합니다.
# try:
#     #숫자를 입력 받습니다.
#     number_input = int(input("정수 입력 > "))
#     #리스트의 요소를 출력합니다.
#     print("{}번째 요소 : {}".format(number_input,list_number[number_input]))
    
# except ValueError as exception:
#         #valueError가 발생한 경우
#         print("정수를 입력해 주세요!")
#         print("exception :",exception)

# except IndexError as exection:
#         #Index Erro가 발생한 경우
#         print("리스트의 인덱스를 벗어났어요")
#         print("exception:",exception)

# except Exception as exection:
#     #이외의 에러가 발생한 경우
#     print("미리 파악하지 못한 예외가 발생했습니다.")
#     print("exception",exception)

# import math
# print(math.sin(1)) #사인
# print(math.cos(1)) #코사인
# print(math.tan(1)) # 탄겐트
# print(math.floor(2.5)) #내림
# print(math.ceil(2.5)) #올림

# from urllib import request

# target = request.urlopen("http://google.com")
# output = target.read()

# print(output)

from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

soup = BeautifulSoup(target,"html.parser")

for location in soup.select("location"):
    print("도시:",location.select_one("city").string)
    print("날씨:",location.select_one("wf").string)
    print("최저기온:",location.select_one("tmn").string)
    print("최고기온:",location.select_one("tmx").string)
    print()
    


