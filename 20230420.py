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
    

# score = float(input("학점을 입력하세요"))

# if score == 4.5:
#     print("신")
# elif 4.2<= score:
#     print("교수님의 사랑")
# elif 3.5<= score:
#     print("현 체제의 수호자")
# elif 2.8<= score:
#     print("일반인")
# elif 2.3<= score:
#     print("일탈을 꿈꾸는 소시민")
# elif 1.75<= score:
#     print("오락문화의 선구자")
# elif 1.0<= score:
#     print("불가촉천민")
# elif 0.5<= score:
#     print("자벌레")
# elif 0<= score:
#     print("플랑크톤")
# else:
#     print("시대를 앞서나가는 혁명의 씨앗")


# if x> 10 & x<20:
#     print("조건의맞습니다.")
# else:
#     print("조건의 맞지 않습니다.")
    
# birth_year = int(input("태어난 해를 입력하세요 : "))

# if birth_year%12==0:
#     print("원숭이 띠")
# elif birth_year%12==1:
#     print("닭 띠")
# elif birth_year%12==2:
#     print("개 띠")
# elif birth_year%12==3:
#     print("돼지 띠")
# elif birth_year%12==4:
#     print("쥐 띠")
# elif birth_year%12==5:
#     print("소 띠")
# elif birth_year%12==6:
#     print("범 띠")
# elif birth_year%12==7:
#     print("토끼 띠")
# elif birth_year%12==8:
#     print("용 띠")
# elif birth_year%12==9:
#     print("뱀 띠")
# elif birth_year%12==10:
#     print("말 띠")
# elif birth_year%12==11:
#     print("양 띠")
    
    
# import datetime #날짜/시간과 관련된 기능을 가져온다.
# now = datetime.datetime.now() # now에 날짜/시간을 구한다.

# hi = str(input("인사 : "))

# if hi in "안녕하세요" or "안녕":
#     print("안녕하세요")

# time = str(input("시간 물어보기 : "))

# if time in "지금 몇시야" or "지금 몇 시에요":
#     print("{}시{}분{}초".format(now.hour,now.minute,now.second))

# a = str(input("지정되지 않는 문자 : "))

# if a == a:
#     print(a)
    
# num = int(input("정수를 입력하세요 : "))

# if num %2 == 0:
#     print(num,"은 2로 나누어 떨어지는 숫자입니다.")
# else:
#     print(num,"은 2로 나누어 떨어지는 숫자가 아닙니다.")    
# if num %3 == 0:
#     print(num,"은 3로 나누어 떨어지는 숫자입니다.")
# else:
#     print(num,"은 3로 나누어 떨어지는 숫자가 아닙니다.")
# if num %4 == 0:
#     print(num,"은 4로 나누어 떨어지는 숫자입니다.")
# else:
#     print(num,"은 4로 나누어 떨어지는 숫자가 아닙니다.")
# if num %5 == 0:
#     print(num,"은 5로 나누어 떨어지는 숫자입니다.")
# else:
#     print(num,"은 5로 나누어 떨어지는 숫자가 아닙니다.")

# list_a = [1,2,3]
# list_b = [4,5,6]

# print("#리스트")
# print("list_a = ",list_a)
# print("list_b = ",list_b)
# print()

# print("리스트 기본 연산자")
# print("list_a + list_b = ",list_a + list_b)

# print("list_a * 3  = ",list_a*3)

# print("#길이 구하기")
# print("len(list_a) = ", len(list_a))


# print("list_a[1]+list_b[2] = ",list_a[1]+list_b[2])

# list_a = [1,2,3]

# print("#리스트 뒤에 요소 구하기")

# list_a.append(4)
# list_a.append(5)
# print(list_a)
# print()

# print("# 리스트 중간에 요소 추가하기")
# list_a.insert(0, 10)
# print(list_a)

# list_of_list =[[1,2,3],[4,5,6,7],[8,9]]

# for items in list_of_list:
#     for item in items:
#         print(items)

# a= [1,2,3,4]
# b=[*a,*a]
# print(b)

# numbers = [273,103,5,32,65,9,72,800,99]

# for num in numbers:
#     if num%2==0:
#         print("짝수입니다",num)
#     else:
#         print("홀수입니다.",num)
        
# for num in numbers:
#     print(num,"는",len(str(num))," 자릿수 입니다.")
    
# numbers = [1,2,3,4,5,6,7,8,9]

# output = [[],[],[]]

# for number in numbers:
#     output[(number+2)%3].append(number)#[(number+2)%3] = 1 + 2 % 3 =0 2+2%3 =1 []배열안에 append(number) 값을 넣어라 

# print(output)



# for i in range(0,len(numbers) // 2): # 0번 부터 숫자길이만큼 나누기 2 만큼 반복해라

#     j = (i*2)+1
#     print(f"i = {i}, j={j}")
#     numbers[j] = numbers[j]**2
# print(numbers)

# dictinary = {
#     "name" : "7D 건조망고",
#     "type" : "당절임" ,
#     "ingredient" : ["망고","설탕","메타중아화안나트륨","치자황색소"],
#     "origin" : "필리핀"

# }   

# print("name : ", dictinary["name"])
# print("type : ", dictinary["type"])
# print("ingredient : ", dictinary["ingredient"])
# print("origin : ", dictinary["origin"])

# dictinary["name"] = "8D 건조 망고"
# print("name :", dictinary["name"])

# numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
# counter = {}

# for number in numbers:
#     if number in counter:
#         counter[number] = counter[number]+1
#     else:
#         counter[number] = 1
        
# print(counter)

# character = {
#     "name" : "기사",
#     "level" : 12,
#     "item" : {
#         "sword" : "불꽃의 검",
#         "armor" : "풀플레이트"
#     },
#     "skill" : ["베기","세게 베기", "아주 세게 베기"]
# }

# for key in character:
#     print(key) 
#     if type(character[key]) is dict:
#         for small_key in character[key]:
#             print(small_key,":",character[key][small_key])
#     elif type(character[key]) is list:
#         for item in character[key]:
#             print(key,":",item)
#     else:
#         print(key,":",character[key])

#별을 찍어보자 10번까지    
# output = ""

# for i in range(1,10):
#     for j in range(0,i):
#         output += "*"
#     output += "\n"

# print(output)

# for i in range(1,15):
#     for j in range(14,i,-1):
#         output += ' '
#     for k in range(0,2*i-1):
#         output += '*'
#     output += '\n'
# print(output)        


