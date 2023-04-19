# 수업

이 문서는 수업에 대한 내용을 다룹니다.

## 1주차 일정

- 월요일: OT
- 화요일: Python 자료형
- 수요일: Python 자료형 , if 조건문
- 목요일:
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

이번 주 수업에서는 인공지능과 머신러닝에 대한 다양한 주제를 다루었습니다. 특히, 자연어 처리와 컴퓨터 비전 분야에서의 딥러닝 기술의 중요성과 활용 방법에 대해 배웠습니다. 또한, AI 보안과 바이어스 감지 같은 실제 사례에 대해도 배웠습니다.

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
    print("홀수입니다.")
```
