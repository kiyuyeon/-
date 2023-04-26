# 4월 1주차 수업

이 문서는 수업에 대한 내용을 다룹니다.

## 1주차 일정

- 월요일: OT
- 화요일: Python 자료형
- 수요일: Python 자료형 , if 조건문
- 목요일: if조건문, 딕셔너리 와 반복문
- 금요일:

# 수업 2023.4.17

Top 10 ML/AI Trends

Automated machine learning(autoML)

AL-enabled conecepual design 

Multi-modal learning 

Models that can achieve multiple objectives 

Ai-based cybersecurity

Inproved language modeling

computer vison in business expands but ROI a challenge

Democratized Ai

Bias removal in ML

Digital twins drive the industrial metaverse

Q 선형 방정식 미분 수치해석 (전통적 방식) 으로 미래를 예측한다. 

⇒ 통계학적 / 전통적인 기계학습 뉴럴네트워크(뇌세포,딥러닝)

스냅시스 연결고리

오늘 수업에서는 인공지능과 머신러닝에 대한 다양한 주제를 다루었습니다. 특히, 자연어 처리와 컴퓨터 비전 분야에서의 딥러닝 기술의 중요성과 활용 방법에 대해 배웠습니다. 또한, AI 보안과 바이어스 감지 같은 실제 사례에 대해도 배웠습니다.

인공지능과 머신러닝은 현재 많은 분야에서 활용되고 있으며, 이에 따라 더 많은 최신 동향과 발전 과정이 관심을 받고 있습니다. 이번 수업에서는 이러한 동향과 발전에 대한 이론적인 내용뿐만 아니라, 실제 적용 사례와 함께 배울 수 있는 기회를 가졌습니다.

open Ai robot humanoid

# 수업 2023.4.18

Low level language 컴퓨터가 이해가 쉬움

High level language 사람이 이해가 쉬움

파이썬을 하려면 파이썬 코드를 입력할 수 있는 텍스트 에디터와 파이썬을 실행할 수 있는 파이썬 인터프리터가 필요하다

파이썬은 명령 프롬프트의 >>>에 코드를 입력하면 실행 결과를 볼수 있는데, 이는 한마디씩 주고 받는 것처러 대화한다고 해서 interactive shell(대화형 셸)이라고 한다

파이썬을 작성한 파일은 해당 폴더의 윈도우 파워셀이나 명령 프롬프트에서 python 명령어로 실행 할 수 있습니다.

Q 커피잔 티스푼 커피믹스 물 전기포트가 준비되어 있습니다.

커피를 만드는 과정을 순서대로 적어 보세요

전기포트의  물을 넣고 끓인다 → 커피잔에 믹스를 넣는다. → 끓은 물을 넣는다. → 티스푼으로 젓는다 → 커피를 마신다;

커피잔에 믹스를 넣는다.→전기포트의  물을 넣고 끓인다 → 끓은 물을 넣는다. → 티스푼으로 젓는다 → 커피를 마신다

object = 커피잔 티스푼 커피믹스 물 전기포트

하는일을 세분화 해야하지만 하는방법은 모두 다르다. 

change ***directory***

cd C:\Users\chwo6\Documents

cd .. 상위 폴더로 이동

확장자: 파일 성격을 구분하는 꼬리 등
문장: 실행할 수 있는 최소 단위
프로그램: 문장들이 모였을 때
키워드: 파이썬에서 예약해 놓은 단어
표현식: 파이썬에서 값을 만들어 내는 간단한 코드
식별자: 프로그래밍 언어에서 이름을 붙일 때 사용, 변수 또는 함수 등으로 사용
snake_case : 단어 사이에 _ 기호를 붙인 경우
CamelCase : 첫 글자를 대문자로 만든 경우

변수 : 값을 저장할 때 사용하는 식별자

변수 in range(시작, 끝, 증가폭):
CamelCase로 정의 : 클래스
스네이크 케이스: 괄호가 있다면 함수, 괄호가 없다면 변수

| 예시 | 스네이크 케이스 | 캐멀 케이스 |
| --- | --- | --- |
| hello coding | hello_coding | HelloCoding |
| hello python | hello_python | HelloPython |
| we are the world | we_are_the_world | WeAreTheWorld |
| create output | create_output | CreateOutput |
| create request | create_request | CreateRequest |

Data Type

string : 메일 제목 , 메세지 내용

number : 물건의 가격  학생 성적

boolean : 참과 거짓

```python
print(type("안녕하세요")
print(type(222)
print(type(true)

```

이스케이프 문자를 사용해 문자열 만들기

\” : 큰따옴표를 의미

\’ : 작은따옴표를 의미

\n : 줄바꿈

\t : 탭을 의미

\\ : 역슬레시를 의미합니다

“”” : 주석 기능도 있지만 여러줄 문자열 기능도 지원한다.

```python
print("\"안녕하세요\"라고 말했습니다")
print('\'배가 고픕니다\'라고 생각했습니다')
print("안녕하세요\n안녕하세요")
print("안녕하세요\t안녕하세요")
print("""동해 물과 백두산이
마르고 닳도록
하느님이 보우하사
우리나라 만세""")

```

문자열 연산자

“문자열” + “문자열”

문자열 반복 연산자

“문자열” * 숫자

문자 선택 연산자(인덱싱) []

문자 선택 연산자 : 문자열 내부의 문자 하나를 선택하는 연산자

인덱스 : 대괄호 안에 선택할 문자의 위치를 지정하며 이 숫자를 인덱스라고 한다.

| 안 | 녕 | 하 | 세 | 요 |
| --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 |

범위 선텍 연산자

```python
print("안녕하세요"[1:4])
```

| 안 | 녕 | 하 | 세 | 요 |
| --- | --- | --- | --- | --- |
| 0 | 1 | 2 | 3 | 4 |

IndexError (index pit pf range) 예외 : 리스트/문자열 수를 넘는 요소/글자를 선택할 때 발생

문자열 길이 구하기

len 함수 : 문자열의 길이를 구해라

 

```python
print(len("안녕하세요"))
```

숫자

integer : 0,1,234,-52

floating point : 0.0,52.273,-1.2

사칙연산

| 연산자 | 설명 | 구분 |
| --- | --- | --- |
| + | 덧셈 연산자 | 숫자 + 숫자 |
| - | 뺄셈 연산자 | 숫자 - 숫자 |
| * | 곰셈 연산자 | 숫자 * 숫자 |
| / | 나눗셈 연산자 | 숫자 / 숫자 |
| // | 정수 나누기 연산자 | 숫자 // 숫자 |
| % | 나머지 연산자 | 숫자 % 숫자 |
| ** | 제곱 연산자 | 숫자 ** 숫자 |

      7  →몫

2   15

14

1 → 나머지

연산자의 우선순위

연산자는 왼쪽에서 오른쪽 순서로 계산

Type Error 예외 : 서로 다른 자료를 연산하면 Type Error 예외가 발생합니다.

# 수업 2023.4.19

*PEP8*은 *파이썬 *****코드의 작성규칙(coding convention)에 대해 설명하는 문서이다

변수 선언 변수 할당 참조 input() int float() str()

원의 둘레 공

원의 둘레 = 반지름 × 2 × 3.14
원의 넓이 = 반지름 × 반지름 × 3.14

원의 둘레 길이(원주, l)와 넓이(S)
l = 2 × 반지름 × 3.14 = 2πr
S = 반지름 × 반지름 × 3.14 = πr

input 값을 받아서 원의 둘레 , 넓이 구하기

```python
pi = 3.14159265
r= int(input("반지름이 값 : "))
a = 2*pi*r
b = r*r*pi

print(pi)
print(r)

print("원의둘레 =",a)
print("원의넓이 =",b)
```

복합대입 연사자

| 연산자 | 설명 |
| --- | --- |
| += | 숫자 덧셈 후 대입 |
| -= | 숫자 뺄셈 후 대입 |
| *= | 숫자 곱셈 후 대입 |
| /= | 숫자 나눗셈 후 대입 |
| %= | 숫자 나머지를 구한 후 대입 |
| **= | 숫자 제곱 후 대입 |

문자열도 복합 대입 연산자를 이용 가능

```python
number = int(input("숫자 입력 : "))
print("number: " ,number)

number += 10
print("number: " ,number)

number += 20
print("number: " ,number)

number += 30
print("number: " ,number)

string = input("글자 입력 : ")
string += "!"
print("string = ",string)
string += "!"
print("string = ",string)
```

input()

명령 프롬프트에서 사용자로 부터 데이터를 입력받을 때 사용

input 함수의 기본은 string

block : 프로그램 실행중 잠시 멈추는 것

cast : 문자열을 숫자로 바꾸기

숫자를 입력 받고 String type → float type 으로 변환뒤 계산하기  

```python
intput_a = float(input("첫번째 숫자>"))
intput_b = float(input("두번째 숫자>"))

print("덧셈 결과 :",intput_a + intput_b)
print("뺄셈 결과 :",intput_a - intput_b)
print("곱셈 결과 :",intput_a * intput_b)
print("나눗셈 결과 :",intput_a / intput_b)
```

VlaueError 예외

자료형을 변환을 할수 없는것  

1. 숫자가 아닌것을 변환하려 할때
2. 소수점이 있는 수사자형식을 int()함수로 변환하려고 할 때

숫자를 문자열로 바꾸기

```python
output_a = str(52)
output_b = str(52.273)
print(type(output_a),output_a)
print(type(output_b),output_b)
```

str()를 사용하여 변환함

inch 단위를 입력받은 후 cm 단위로 변화해보기

inch 단위를 cm 단위를 변경하기 위해서는 inch * 2.54이다.

```python
row_intch = int(input("인치단위 입력하기"))
cm = row_intch * 2.54

print(row_intch,"inch단위를 cm 단위를 변환합니다. ",cm,"cm입니다")
```

python tutor : 프로그래밍 초보자가 흐름을 쉽게 이해할 수 있도록 파이썬 코드를 분석해 주는 도구

변수 선언 : 변수를 생성하는 것을 의미

변수 할당 : 변수에 값을 넣는 것을 의미

변수 참조 : 변수에서 값을 꺼내는 것

swap = 변수의 교체 

format : 문자열을 가지고 있는 함수 {}를 포함한 문자열 뒤에 마침표(.)를 찍고 format 함수를 사용 중괄호의 개수와 format 함수 괄호 안 매개변수의 개수는 반드시 같아야한다.

```python
format_a = "{}만원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만원".format(5000)
format_c = "{} {} {}".format(3000,4000,5000)
format_d = "{} {} {}".format(1,"문자열",5000)

print(format_a)
print(format_b)
print(format_c)
print(format_d)
```

format 활용법 

```python
#정수
output_a = "{:d}".format(52)

output_b = "{:5d}".format(52) #5칸
output_c = "{:10d}".format(52) #10칸

output_d = "{:05d}".format(52) #양수
output_e = "{:05d}".format(-52) #음수
print("# 기본")
print("기본",output_a)

print("# 특정칸 출력하기")
print("특정칸의 출력하기 5칸",output_b)
print("특정칸의 출력하기 10칸",output_c)

print("# 빈칸을 0으로 채우기")
print("format 값의 양수",output_d)
print("format 값의 음수",output_e)
```

format 부동소수점 출력하기

```python
#부동 소수점 출력 하기
output_a = "{:f}".format(52.273) 
output_b = "{:15f}".format(52.273 ) # 15칸 만들기  
output_c = "{:+15f}".format(52.273) # 15칸에 부호 추가하기 
output_d = "{:015f}".format(52.273) # 15칸에 부호 추가하고 0으로 채우기

print(output_a)
print(output_b)
print(output_c)
print(output_d)
```

부동소수점은 기몬적으로 .뒤에 6자리이다.(기본값)

format 부동소수점 아래 지정하기

```python
#부동 소수점 아래 지정하기
output_a = "{:15.3f}".format(52.273) #15칸 뛰고 소수점 3자리수 만 나옴
output_b = "{:15.2f}".format(52.273 ) #15칸 뛰고 소수점 2자리수 만 나옴
output_c = "{:+15.1f}".format(52.273) #15칸 뛰고 소수점 1자리수 만 나옴

print(output_a)
print(output_b)
print(output_c)
```

다음 코드처럼 .을 입력하고 뒤에 몇 번째 자리수까지  표시할지 지정하면 된다.

의미 없는 소수점 제거하기

파이썬은 0과 0.0을 출력했을 때 내부적으로 자료형이 달므로 서로 다른 값으로 출력합니다. 그런데 의미 없는 0을 제거하고 출력하고 싶을떼 {:g}를 사용하면됩니다.

 

```python
# 의미 없는 소수점 제거하기
output_a = "{:.g}".format(52.0) 
print(output_a)
```

파괴적 함수 : 원본은 변한다.

비파괴적 함수 : 원본은 변하지 않는다. 

대소문자 바꾸기(원본은 바꾸지 않는다.)

upper() : 알파벳 모두를 대문자로 만듭니다.

lower() : 알파벳 모두를 소문자로 만듭니다.

```python
#upper , lower 사용하기 비파괴적 함수
a = "Hello World"
print(a.upper())
print(a.lower)
print(a)#비파괴적 함수이므로 원본은 바뀌지 않는다.

b=a.upper()#b에서 a를 할당하여 파괴적인 함수로 변환한다.
print(b)

c=a.lower()#c에서 a를 할당하여 파괴적인 함수로 변환한다.
print(c)
```

문자열 양옆에 공백 제거하기 

strip() : 문자열 양옆에 공백을 제거합니다. 

lstrip() : 문자열 왼쪽에 공백을 제거합니다.

rstrip() : 문자열 오른쪽에 공백을 제거합니다.

```python
#문자열 공백 제거하기 
input_a = """
    안녕하세요
"""
print(input_a.strip())
```

문자열 구성 파악하기 isOO()

isalnum() : 문자열이 알파벳 또는 숫자로만 구성되어 있는지 확인합니다.

isalpha() : 문자열이 알파벳으로만 구성되어 있는지 확인합니다.

isidentifiter(): 문자열이 식별자로 사용할 수  있는지 확인합니다.

isdecimal() : 문자열이 정수 형태인지 확인합니다.

isdigit() : 문자열이 숫자로 인식될 수 있는지 확인합니다.

isspace() : 문자열이 공백으로만 구성되어 있는지 확인합니다.

islower() : 문자열이 소문자로만 구성되어 있는지 확인합니다.

isupper() : 문자열이 대문자로만 구성되어 있는지 확인합니다.

문자열 찾기 

find() : 왼쪽으로부터 찾아서 처음 등장하는 위치를 찾습니다.

rfind() : 오른쪽부터 찾아서 처음 등장하는 위치를 찾습니다.

| 0 | 1 | 2 | 3 | 4 | 5 | 6 |
| --- | --- | --- | --- | --- | --- | --- |
| 안 | 녕 | 안 | 녕 | 하 | 세 | 요 |

```python
#문자열 찾기 find(),rfind()
output_a = "안녕안녕하세요".find("안녕")
print(output_a)

output_b = "안녕안녕하세요".rfind("안녕")
print(output_b)
```

문자열과 in 연산자

in : 문자열 내부에 어떤 문자열이 있는지 확인할때 사용한다

```python
#in 연산자 문자열 확인하기
print("안녕"in "안녕하세요")
print("잘자"in "안녕하세요")
```

문자열 자르기

split() : 문자열을 특정한 문자로 자를 때는 split()

```python
#문자열 자르기 split
a="10,20,30,40,50".split(",")
print(a)
```

f-문자열

f - 문자열 : 문자열 앞에 f를 붙이고 붙자열 내부에서 표현식 {}로 감싸서 삽입할 수 있다.

```python
data = ['별',2,'M','서울시 강서구','Y']
print(f"""이름 : {data[0]}
나이 : {data[1]}
성별 : {data[2]}
지역 : {data[3]}
중성화 여부 : {data[4]}
""")
```

예제 

구의 부피와 겉넓이

```python
r = int(input("반지름 넓이"))
pi = 3.141592
print("구의 부피 ={}".format(4/3*pi*r**3))
print("구의 겉넓이 ={}".format(4*pi*r**2))
```

피타고라스의 정리 밑변**2 + 높이**2 = 빗편**2

```python
c = float(input("밑변의 길이"))
d = float(input("높이의 길이"))
print("빗변의 길이는 {}".format((c**2 + d**2)**0.5)) 
```

불 자료형과 if 조건문

Boolean : True ,False

Boolean 비교연산자

| 연산자 | 설명 |
| --- | --- |
| == | 같다 |
| != | 다르다 |
| < | 크다 |
| > | 작다 |
| <= | 크거나 작다 |
| >= | 작거나 크다 |

Boolean 논리 연산자

| 연산자 | 의미 | 설명 |
| --- | --- | --- |
| not | 아니다 | 불을 반대로 전환합니다 |
| and | 그리고 | 피연산자 두 개가 모두 참일 때 True를 출력하며 그 외는 모두 False를 출력합니다. |
| or | 또는 | 피연자는 두 개 중에 하나만 참이라도 True를 출력하며 모두 거짓일때만 False를 출력합니다 |

if 조건문 : 조건의 따라 코드를 실행하거나 실행하지 않게 만드는 구문

조건 분기 : 조건을 기반으로 실행의 흐름을 변경하는 것

elif : 세 개 이상의 조건을 연결해서사용 if와 else문 사이에 입 

else : if 조건문 뒤에 사용하며 if 조건문의 조건이 거짓일 때 실행되는 부분

```python
# IF문 기본 사용
number = int(input("정수 입력 >"))

if number > 0:
    print("양수입니다.")
elif number <0 :
    print("음수입니다.")
else:
    print("0입니다.")
```

계절을 구분하기

```python
import datetime #날짜/시간과 관련된 기능을 가져온다.
now = datetime.datetime.now() # now에 날짜/시간을 구한다.
print("{}년{}월{}일{}시{}분{}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

if 3<=now.month <=5:
    print("이번 달은 {}월로 봄인다.".format(now.month))
elif 6<=now.month <=8:
    print("이번 달은 {}월로 여름인다.".format(now.month))
elif 9<=now.month <=11  :
    print("이번 달은 {}월로 가을인다.".format(now.month))
else:
    print("이번 달은 {}월로 겨울인다.".format(now.month))
```

홀수 짝수 구분하기

```python
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
    print("홀수입니다.
```

pass : 프로그래밍의 전체 골격을 잡아두고 내부에서 처리할 내용은 나중에 만들고자 할 때 사용한다.

IndentationError : if 조건문 사이에는 무조권 들여쓰기 4칸을 넣고 코드를 작성해야만 하는대 안했을 경우

raise NotlmplementedError : pass 잊어버리고 사용할 경우 아직 구현하지 않는 부분 이라는 오류

태어난 연도를 입력받아 띠를 출력하는 프로그램

조건 

입력받은 연도를 12로 나눈 나머지를 사용 나머지가 0,1,2,3,4,5,6,7,8,9,10,11 일때 12로 나눈 나머지가 각각 원숭이,닭,개,쥐,소,범,토끼,용,뱀,말,양띠 입니다.

```python
birth_year = int(input("태어난 해를 입력하세요"))

if birth_year%12==0:
    print("원숭이 띠")
elif birth_year%12==1:
    print("닭 띠")
elif birth_year%12==2:
    print("개 띠")
elif birth_year%12==3:
    print("돼지 띠")
elif birth_year%12==4:
    print("쥐 띠")
elif birth_year%12==5:
    print("소 띠")
elif birth_year%12==6:
    print("범 띠")
elif birth_year%12==7:
    print("토끼 띠")
elif birth_year%12==8:
    print("용 띠")
elif birth_year%12==9:
    print("뱀 띠")
elif birth_year%12==10:
    print("말 띠")
elif birth_year%12==11:
    print("양 띠")
```

간단한 대화형 프로그램

조건 안녕 또는 안녕하세요를 입력하면 안녕하세요 정도의 간단한 인사를 할수있게하고

지금 몇시야 또는 지금 몇시에요 처럼 시간을 물어보면 시간을 응답라고

준비되지 않는 문장을 출력시 그대로 출력

```python
import datetime #날짜/시간과 관련된 기능을 가져온다.
now = datetime.datetime.now() # now에 날짜/시간을 구한다.

hi = str(input("인사 : "))

if hi in "안녕하세요" or "안녕":
    print("안녕하세요")

time = str(input("시간 물어보기 : "))

if time in "지금 몇시야" or "지금 몇 시에요":
    print("{}시{}분{}초".format(now.hour,now.minute,now.second))

a = str(input("지정되지 않는 문자 : "))

if a == a:
    print(a)
```

나누어 떨어지는 숫자

숫자를 입력하면 그 숫자가 2,3,4,5로 나누어 떨어지는지 확인하고 출력하는 프로그램

```python
num = int(input("정수를 입력하세요 : "))

if num %2 == 0:
    print(num,"은 2로 나누어 떨어지는 숫자입니다.")
else:
    print(num,"은 2로 나누어 떨어지는 숫자가 아닙니다.")    
if num %3 == 0:
    print(num,"은 3로 나누어 떨어지는 숫자입니다.")
else:
    print(num,"은 3로 나누어 떨어지는 숫자가 아닙니다.")
if num %4 == 0:
    print(num,"은 4로 나누어 떨어지는 숫자입니다.")
else:
    print(num,"은 4로 나누어 떨어지는 숫자가 아닙니다.")
if num %5 == 0:
    print(num,"은 5로 나누어 떨어지는 숫자입니다.")
else:
    print(num,"은 5로 나누어 떨어지는 숫자가 아닙니다.")
```

리스트: 여러가지 자료를 저장할 수 있는 자료

요소 : 리스트 내부에 넣는 자료

index : 리스트 기호인 [] 대괄호에 들어간 숫자

리스트 활용

1. 대괄호 안에 음수를 넣어 뒤에서 부터 요소를 선택할수 있다
2. 리스트 접근 연산자는 이중으로 사용할수 있다.
3. 리스트안에서도 리스트를 사용할수 있다.

리스트에서 IndexError: 리스트의 길이를 넘은 인덱스로 인덱스 요소에 접근하려고 할 때 발생 하는 에러

리스트 연산

리스트 연결 + 반복* 길이 len

리스트에 요소 추가하기 

extend() : 매개변수로 라스트를 추가하는대 리스트뒤에 다양한 요소를 모두 추가한

append(요소) : 리스트 뒤에 요소를 추가

insert(위치,요소) : 리스트 중간에 요소를 추가

리스트 요소와 연산에 차이 

연산은 비파과적 이고 요소는 파괴적이다.

리스트 요소 제거하기

del 키워드 사용할경우 범위 지정해 리스트 요소를 함꺼번에 제거 가능

del 리스트명[인덱스]

리스트명.pop(인데스)

리스트.remove(값)

clear() : 모두제거하기

리스트 정렬하기

sort() : 리스트 요소를 정렬한다. 기본은 오름차순 정렬

range :  횟수만 지정하면 숫자가 0부터 시작하지만, 다음과 같이 시작하는 숫자와 끝나는 숫자를 지정해서 반복할 수도 있습니다.

**range(시작, 끝):**

리스트 내부에 있는지 확인하기

in/not in : 값 in 리스트

| 목록 | 배열 |
| --- | --- |
| 내장 데이터 구조 | 배열 또는 numpy를 사용하여 가져와야 합니다 |
| 대괄호로 묶음 | ,arry함수를 사용하여 묶어야 합니다 |
| 다른 유형의 요소로 포함 할수 있습니다. | 다른 형식의 요소를 포함할 수 없습니다. |
| 가변 크기 중첩 가능 | 중첩을 위해 동일한 크기의 배열이 필요합니다 |
| 직접 산술 연산을 적용할 수 없습니다. | 직접 산술 연산을 적용할 수 있습니다 |
| 더 많은 메모리를 소비합니다 | 비교적 적은 메모리를 소비합니다 |
| 명사적 루프를 만들지 않고 인쇄 할 수 있습니다, | 배열 요소를 인쇄하기 위해 명사적 루프를 만들어야 합니다. |

반복문

전개 연산자 : 리스트 내용을 전개해서 사용 할수 있다

*리스트

전개 연산자는 비파괴적으로 구현 할수 있다

딕셔너리와 반복문

딕셔너리 : 키를 기반으로 값을 저장하는 것

| 자료형 | 의미 | 가리키는 위치 | 선언 형식 |
| --- | --- | --- | --- |
| 리스트 | 인덱스를 기반으로 값을 저장 | 인덱스 | 변수 = [] |
| 딕셔너리 | 키를 기반으로 값을 저장 | 키 | 변수 = {} |

딕셔너리 예시

변수 =  {

키: 값,

키:값

}

| 구분 | 선언 형식 | 사용예 | 틀린예 |
| --- | --- | --- | --- |
| 리스트 | list_a = [] | list_a[1] |  |
| 딕셔너리 | dict_a = {} | dict_a[”name”] | dict_a{”name”} |

딕셔너리 사용 예제

```python
dictinary = {
    "name" : "7D 건조망고",
    "type" : "당절임" ,
    "ingredient" : ["망고","설탕","메타중아화안나트륨","치자황색소"],
    "origin" : "필리핀"

}   

print("name : ", dictinary["name"])
print("type : ", dictinary["type"])
print("ingredient : ", dictinary["ingredient"])
print("origin : ", dictinary["origin"])

dictinary["name"] = "8D 건조 망고"
print("name :", dictinary["name"])
```

NameError : 딕셔너리에 이름이 정의가 안되있을때 나오는 오류 ex name : "7D 건조망고" → "name" : "7D 건조망고"

KeyError : 딕셔너리에 존재하지 않는 키에 접근하면 KeyError 발생

딕셔너리에 값 추가하기 / 제거하기

딕셔너리[새로운 키] = 새로운 값

dictinary["price"] = 5000

딕셔너리에 요소 추가하기

딕셔너리에 내부에 키가 있는지 존재 확인

in 키워드

key = input(”찾으려는 키”)

**if key in dicttionary:**

print(”있다”)

else: 

print(”없다”)

for 반복문 : 딕셔너리와 함께 사용하기

for 키 변수 in 딕셔너리:

코드

whie 반복문

break : 반복문에서 벗어날때 사용한다

continue : 현재 반복을 생략하고 다음 반복으로 넘어갈때 사용한다.

# 4월 2주차 수업

이 문서는 수업에 대한 내용을 다룹니다.

## 2주차 일정

- 월요일: 외부 모듈
- 화요일:
- 수요일:  선형 리스트,
- 목요일:
- 금요일:

# 수업 2023.4.24

럄다 :  기능을 전달하는 코드 이런코드를 효율적으로 사용 

map(함수,리스트) : 리스트의 요소를 함수에 넣고 리턴된 값으로 새로운 리스트를 구성해 주는 함수

filter(함수, 리스트) : 리턴된 값이 True인 것으로 새로운 리스트를 구성해 주는 함수

```python
list_input_a = [1,2,3,4,5]

output_a = map(lambda x: x*x, list_input_a)
print("map 함수의 실행결과")
print("map(power, list_input_a):",output_a)
print("map(power, list_input_a):",list(output_a))
print()

output_b = filter(lambda x: x<3, list_input_a)
print("filter 함수의 실행결과")
print("filter(under3, list_input_a):",output_b)
print("filter(under3, list_input_a):",list(output_b))
print()
```

파일 열고 닫기

파일 객체 = open(문자열 : 파일경로 , 문자열 : 읽기 모드)

|  모드 | 설명 |
| --- | --- |
| w | wite 모드(새로 쓰기 모드) |
| a | append 모드 (뒤에서 이어서 쓰기 모드) |
| r | read 모드(읽기 모드) |

```python
file = open("basic.txt","w") #파일 열기 없으면 생성

file.write("Hello Python Programming...!") #basic.txt 파일에 해당 글을 적는다

file.close() # 종료한다.
```

with 키워드

코드가 길어지거나 많은 조건문과 반복문이 실행되면 열고 닫지 않는 실수가 발생 할 수 있다 이런 실수를 방지하기 위해 with 키워드 같은 형태의 구문을 사용한다

```python
with open("basic.txt","w") as file:
	#파일에 텍스트를 씁니다.
	file.write("Hello Python Programming...!")
```

정형데이터 :  0반 키 , 세금계산거 등 정형되어 있는 것 

비정형데이터 : 노래 사진 등 정형되지 않았다.

```python
import random 

hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt","w")as file: #파일 쓰기모드로 엽니다.
    for i in range(1000):
        #랜덤한 값으로 변수를 생성합니다.
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40,100)
        height = random.randrange(140,200)
        #텍스트를 씁니다.
        file.write("{}, {}, {} \n".format(name,weight,height))
        
        
with open("info.txt","r") as file:
    for line in file:
        #변수를 선언합니다.
        (name,weight,height) = line.strip().split(",")
        
        #데이터가 문제가 있는지 확인합니다.
        if (not name) or (not weight) or (not height):
            continue
    
        #결과를 계산합니다.
        bmi = int(weight) / ((int(height)/100)**2)
        result = ""
        if 25<= bmi:
            result ="과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"
        
        #출력합니다.    
        print('\n'.join([
            "이름 : {}",
            "몸무게 : {}",
            "키 : {}",
            "BMI : {}",
            "결과 : {}"
        ]).format(name,weight,height,bmi,result))
        print()
```

구문 오류와 예외

구문 오류  : 프로그램 실행전 발생하는 오류

런타임 오류, 예외 : 프로그램 실행 중에 발생하는 오류

try :

예외가 발생할 가능성이 있는코두

except: 

예외가 발생하였을때

```python
try:
    number_input_a = int(input("정수 입력"))
    
    print("원의 반지름 : " , number_input_a)
    print("원의 둘레 : ",2*3.14*number_input_a)
    print("원의 넓이",3.14*number_input_a*number_input_a)
except:
    print("숫자만 입력해주세요")
```

else : 예외가 발생하지 앟았을 때 실행할 코드

pass문 사용

```python
list_input_a = ["52","273","스파이","103"]

list_number = []
for item in list_input_a:
    try:
        float(item)
        list_number.append(item)
    except:
        print("에러가 발생했습니다.")
        pass
print("{} 내부에 있는 숫자는".format(list_input_a))
print("{}입니다.".format(list_number))
```

finally 구문: 예외 처리 구문에서 가장 마지막에 사용할 수 있는 구문 예외가 발생하든 발생하지 않든 무족건 실행할때 사용

예외 구문과 예외 객체

```python
#변수 선언
list_number = [52,273,32,72,100]

#try except 구문으로 예외를 처리합니다.
try:
    #숫자를 입력 받습니다.
    number_input = int(input("정수 입력 > "))
    #리스트의 요소를 출력합니다.
    print("{}번째 요소 : {}".format(number_input,list_number[number_input]))
    
except ValueError as exception:
        #valueError가 발생한 경우
        print("정수를 입력해 주세요!")
        print("exception :",exception)

except IndexError as exection:
        #Index Erro가 발생한 경우
        print("리스트의 인덱스를 벗어났어요")
        print("exception:",exception)

except Exception as exection:
    #이외의 에러가 발생한 경우
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print("exception",exception)
```

raise : pass의 반대 그냥 넘어가면 문제가 생기니 여기서 강제 종료시키자

raise 예외 객체

표준 모듈

모듈 : 코드를 분리하고 공유하는 기능

표준 모듈 : 파이썬에 기본적으로 내장된 모듈

외부 모듈 : 사람들이 만들어 공개한 모듈

일반적으로 모듈을 가져오는 import 구문은 코드 가장위에 작성

from : 모듈에는 많운 변수와 함수가  있는대 이때 그중에서 활용하고 싶은 기능 일부만 사용할때 사용한다.

from 모듈 이름 imporrt 가져오고 싶은 변수 또는 함수

as   : 모듈을 가져올 때 이름이 충돌하는 경우나 이름을 줄이고 싶은경우 as를 사용하여 대체한다.

import 모듈 as 사용하고싶은 식별자

ramdom 모듈 : 랜덤한 값을 생성할 때 사용하는 모듈

sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈

os 모듈 : 운영체제와 관련된 기능을 가지고 있는 모듈

datetime : 날짜 시간과 과련된 모듈로 날짜 형식을 만들 때 자주 사용되는 코드로 구성되어 있다.

time : 시간과 관련된 기능을 다룰 때 사용합니다.

urlib : url을 다루는 라이버러리 입니다.

정규 표현식

[https://docs.python.org/ko/3/howto/regex.html](https://docs.python.org/ko/3/howto/regex.html)

모듈 설치

pip install 모듈 이름

Beautiful Soup 모듈 : 웹 페이지 븐석 모듈

```python
#모듈을 읽어 드립니다
from urllib import request
from bs4 import BeautifulSoup

#urlopen() 함수로 기상청의 날씨를 읽습니다.
target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=109")

# Beautifulsoup을 사용해 전국 날씨를 읽습니다.
soup = BeautifulSoup(target,"html.parser")

#location 태그를 찾습니다.
for location in soup.select("location"):
    #내부의 city, wf , tmn, tmx 태크를 찾아 출력합니다.
    print("도시:",location.select_one("city").string)
    print("날씨:",location.select_one("wf").string)
    print("최저기온:",location.select_one("tmn").string)
    print("최고기온:",location.select_one("tmx").string)
    print()
```

Django : 웹 개발시 매우 다양한 웹 기능을 제공하는 웹 프레임워크

flask 모듈 : Django보단 작은 기능을 제공하는 웹 프레임워크

flask 모듈 

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return"<h1>Hello World!</h1>"
```

flask  실행시 cmd 창에서 flask run을 사용하여 실행한다.

라이브러리 : 정상적인 제어 하는 모듈

개발자가 모듈의 기능을 호출하는 형태

# 수업 2023.4.25

프레임워크 : 제어 역전이 발생하는 모듈

모듈이 개발자가 작성한 코드를 실행하는 형태

제어 역전 : 개발자가 모듈의 함수를 호출하는 것이 일반적인 제어 흐림이나 반대로 개발자가 만든 함수를 모듈이 실행하는 것

모듈 만들기

__name__ ==”__main__” : 현재 파일이 엔트리 포인트인지 확인함

패키지 : 모듈이 모인것

entry point : python 명령어를 사용해서 첫 진입파일을 엔트리 포인트 라고 한다

dir 파일을 보여줌

mkdir 폴더생성

rmdir 폴더삭제

pip show (설치된 모듈) : 모듈이 설치된 위치를 확인하 수 있습니다.

파이썬은 크게 두 가지 특징을 가지고 있다.

- main이 존재하지 않는다.
- 들여쓰기를 통해 코드 실행의 레벨을 결정한다.

현재 모듈의 이름을 담고있는 내장 변수이다. 

이 변수는 **직접 실행된 모듈의 경우 `__main__`이라는 값**
을 가지게 되며, **직접 실행되지 않은 import된 모듈은 모듈의 이름(파일명)**을 가지게 된다.

바이너리 데이터 : 텍스트 에디터로 열었을때 의미를 이해할 수 없는 데이터

| 비교 | 텍스트 데이터 | 바이너리 데이터 |
| --- | --- | --- |
| 구분방법 | 텍스트 데이터로 열었을 떄 읽을 수 있다 | 텍스트 데이터로 열어도 읽을 수 없습니다 |
| 장점 | 사람이 쉽게 읽을수 있다
텍스트 에디터로 쉽게 수정할 수 있다 | 용량이 적습니다 |
| 단점 | 용량이 큽니다 | 사람이 쉽게 읽을 수 없습니다
일반적으로 텍스트 에디터로 편집할 수 없습니다 |

클래스

객체 지향 프로그래밍 :

객체를 우선으로 생각해서 프로그래밍하는 것

클래스 기반의 객체지향 프로그래밍 

객체 : 여러 속성을 가질 수 있는 대상 

생성자 : 클래스 이름과 같은 함수 ,__init___

클래스 : 객체를 쉽고 편리하게 생성하기 위해 만들어진 구분

인스턴스 클래스를 기반으로 생성한 객체

메소드 클래스가 가진 함수

```python
#클래스 선언
class Student:
    def __init__(self,name,korean,math,english,science):#생성자
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
        
    def get_sum(self):
        return self.math+self.korean+self.english+self.science
    
    def get_average(self):
        return self.get_sum()/4
        
    def to_string(self):
        return "{}\t{}\t{}".format(self.name,self.get_sum(),self.get_average())
 #학생 리스트를 선언       
students = [
   Student(name="윤인성", korean=87, math=98, english=88, science=95),
   Student(name="연하진", korean=87, math=98, english=88, science=95),
   Student(name="구지연", korean=87, math=98, english=88, science=95),
   Student(name="나선주", korean=87, math=98, english=88, science=95), 
]

#학생을 한명씩 반복
print("이름", "총점", "평균",sep="\t")
for student in students:
    #출력
    print(student.to_string())
```

상속 : 클래스를 기반으로 그 속성과 기능을 물려받아 새로운 클래스를 만드는 것

isinstance(인스턴스,클래스) : 어떤 클래스로부터 만들어졌는지 확인하는 함수 제공

자료구조 : 컴퓨터 분야에서 효율적으로 접근하고 수정할 수 있도록 자료를 구성·관리·저장하는 것

알고리즘 : 컴퓨터 분야나 수학 등 관련 분야에서 어떤 문제를 해결하기 위해 정해진 일련의 단계적인 절차나 방법

자료구조의 개념

컴퓨터 프로그래밍 언어에서 효율적인 자료 형태

단순 자료구조 : 정수 실수 문자 문자열

선형 자료구조 : 리스트 스택 큐

비선형 자료구조 : 트리 그래프

파일 자료구조 : 순차파일 색인파일 직접파일

선형 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7282dafc-1fe0-4474-8d10-88c7e7cc9884/Untitled.png)

비선형 구조

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/51882756-4b09-4299-add5-01091d100769/Untitled.png)

파일 자료구조

파일 내용이 디스크에 저장되는 방식에 따라 순차 파일과 직접 파일로 구분

 순차 파일(Sequential File)
• 파일 내용을 논리적인 처리 순서에 따라 연속해서 저장하는 것
• 구조가 간단하기에 저장되는 공간 효율이 높지만, 다른 내용을 추가하거나 삭제할 경우에는 파일
내용을 재구성해야 하므로 상당히 시간이 오래 걸림

 직접 파일(Direct File)
• 파일 내용을 임의의 물리적 위치에 기록하는 방식으로 직접 접근 방식(Direct Access Method)

 알고리즘 표현법
 일반 언어 표현
• 일반적인 자연어를 사용해서 설명하듯이 알고리즘을 표현
• 일반 사람이 이해하기 쉽게 표현할 수 있으나, 최종적으로 코드로 변경하는 데는 한계가 있음
• 어떤 알고리즘을 사용해야 할지 아이디어가 떠오르지 않는 시점에서, 생각 범위를 넓히는 단계
정도에 사용하면 무난

 순서도를 이용한 표현
• 여러 종류의 상자와 상자를 이어 주는 화살표를 이용해서 명령 순서를 표현
• 간단한 알고리즘은 쉽게 표현할 수 있지만, 복잡한 알고리즘은 표현하기 어려운 경우가 많음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/23d38b4d-3bfd-4238-a7a1-deb006353595/Untitled.png)

 의사코드를 이용한 표현
• 프로그래밍 언어보다는 좀 더 인간의 언어에 가까운 형태
• 프로그램 코드와 일반 언어의 중간 형태
• 프로그램 코드를 직접 코딩하는 것보다 알고리즘을 좀 더 명확하게 정립하는 데 도움이 되고 코드에
설명을 달지 않아도 이해하는 데 무리 없음

![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/42dd4339-f800-4a76-aa11-05e0045d6c9b/Untitled.png)

 혼합 형태
• 간단한 알고리즘은 직접 코드로 작성
• 복잡한 알고리즘은 일반 언어, 의사코드, 순서도, 그림 등을 종합적으로 활용해서 표현

 알고리즘의 성능
 알고리즘 성능 측정
• 알고리즘을 소요 시간을 기준으로 알고리즘 성능을 분석 방법이 ‘시간 복잡도(Time Complexity)’

# 수업 2023.4.25

선형 리스트의 개념

데이터를 일정한 순서로 나열한 자료구조

순차 리스트라고도 함

선형 리스트는 입력 순서대로 저장하는 데이터에 적당

```python
def add_data(friend):
    
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend
    
def insert_data(position,friend):    
    if position < 0 or position > len(katok):    
        print("데이터를 삽입할 범위를 벗어났습니다.")
        return
    
    katok.append(None)
    kLen = len(katok)
    
    for i in range(kLen-1,position,-1):
        katok[i]= katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend

def correction_data(position,friend):    
    if position < 0 or position > len(katok):    
        print("데이터를 수정할 범위를 벗어났습니다.")
        return
    
    kLen = len(katok)
    
    for i in range(kLen-1,position-1):
        katok[i]= katok[i-1]
        katok[i-1] = None
        
    katok[position] = friend
    
def delete_data(position):
    if position < 0 or position > len(katok):  
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return
          
    kLen = len(katok)
    katok[position] = None
        
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None
            
    del(katok[kLen-1])

katok = []
select = -1

if __name__=="__main__":
    
    while (select != 5):
        
        select = int(input("선택하세요(1:추가,2:삽입,3:삭제,4:수정,5:종료)-->"))
        
        if(select == 1):
            data = input("추가할 데이터 -->")
            add_data(data)
            print(katok)
        elif (select == 2):
            pos = int(input("삽입할 위치 -->"))
            data = input("추가할 데이터 -->")
            insert_data(pos, data)
            print(katok)
        elif (select == 3):
            pos = int(input("삭제할 위치 -->"))
            delete_data(pos)
            print(katok)
            
        elif (select == 4):
            pos = int(input("수정할 위치 -->"))
            data = input("수정할 데이터 -->")
            correction_data(pos, data)
            print(katok)
                
        elif (select == 5):
            print(katok)
            exit()
        else :
            print("1~4 중 하나를 입력하세요")
            continue
```

단순 연결 리스트의 개념

노드들이 물리적으로 떨어진 곳에 위치

각 노드의 번지도 순차적이지 않음

화살표로 표시된 연결(링크,Link)을 따라가면 선형 리스트 순서와 같음

노드 구조

단순 연결 리스트는 다음 데이터를 가르키는 링크가 더 필요

노드는 데이터와 링크로 구성된 항목
