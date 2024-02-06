# print(), input()

> cli에 출력하기, 입력하기

* print("안녕하세요"), input("숫자입력:")
* int(), str(), float(), bool()
* ⬜() [print해라 input해라 int화해라 str화해라]

# 변수

> 메모리에 저장하는 공간

> 2+3 =5
* 인간)연산+기억을 동시에 함
* 컴퓨터) 연산[CPU] / 기억[RAM]을 동시에 못함
* 변수 이름 문법
  * 영어,숫자,특수문자(_)만 가능
  * 숫자로 시작 안됨 e) 1a(X) a1(O)
  * 대소문자 구분함 A,a
  * 예약어[if, return, for 등]-이미 약속된 단어 -> 변수명 불가
  * 띄어쓰기 안됨
* 변수 이름 컨벤션(국룰-협업시)
  * 소문자로 시작
  * 두단어 합쳐질 때, snake이름, camel이름
    * mega_coffee :snake
    * megaCoffee :camel
  
# 타입

> 숫자(int,float), 문자(str), 불리언(bool), ...

* 숫자
  * int ex) a = 123
  * float ex) b = 1.23

* 문자
  * '', "", """""" ex) """""" (문단) ex) a = '123', b = '12.3', c = """파이썬 수업 언제끝남?"""
  
* 불리언
  * True, False

> 타입 변환(Type Casting) [타입()]

* int(), float ex) int("123") -> 123
* str() ex)str(123), str(True)
* bool() ex) bool(123)[True] bool(-1)[True] bool('ㅋㅋ')[True]
  * 빈 문자열"", 숫자 0만 False 나머지는 다 True
* list()

# 연산자(Operator)

> 사칙 연산, 대입 연산, 비교 연산, 논리 연산, in 연산자, ...

> 토큰: 연산해주는 작은 단위

### 사칙 연산

* +,-,*,/,%,//,**
* 숫자 타입에만 적용 cf) a = '1' + '1' :이건 사칙연산이 아님.

### 연결 연산자 & 반복 연산자
* +,*
* 문자 타입에만 적용

### 대입 연산자
* =, +=, *=, -=, /=

### 비교 연산자
* >, <, >=, <=, ==, !=,
* 결과가 무조건 bool 타입

### 논리 연산자
* and(all True), or(all False), not
* a = (5>3) and (3>1)   : 대우를 써서 코드를 깔끔하게

### 멤버쉽(In) 연산자
* 문자열 내에 특정 문자 확인
* a = "mega" in "megastudy" [True]

### 슬라이싱([start:end:step]) 연산자
* 문자열의 일부 추출
* "megastudy"[0:5] -> 'megas'
* "megastudy"[:3] -> 'meg'
* "megastudy"[::2] -> 'masuy' 그런가?
* "megastudy"[:5:2] -> 'mgs'

### 인덱싱([]) 연산자
* 문자열에서 특정 위치의 문자 가져오기
* "megastudy"[1] -> "e"