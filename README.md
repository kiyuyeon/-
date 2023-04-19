# 수업

이 문서는 수업에 대한 내용을 다룹니다.

## 1주차 일정

- 월요일: OT
- 화요일: Python 자료형
- 수요일:
- 목요일:
- 금요일:

# 수업 2023.4.17

컴퓨터 비전 자연어 처리 (딥러닝) 이유 : 딥러닝은 가르치는  수업재료를 준다

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

cd .. 

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

format : 문자열을 가지고 있는 함
