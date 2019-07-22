# 복습

## 01. python

### 변수 및 자료형

> **dust = 60**을 해석하면?
>
> 상자를 떠올려라!!
>
> dust는 60이다 (X)
>
> dust에 60을 저장한다(O)

- 변수는 = 을 통해 할당된다.

- 자료형 확인은 type()

- 변수의 메모리 주소 확인은 id()

  ```python
  name = 'subin'
  print(name)
  
  type(name)
  
  id(name)
  ```

- 같은 값을 동시에 할당 가능

- 다른 값을 동시에 할당 가능

- 서로 값을 바꾸는 것 가능

  ```python
  x = y = 100
  print(x, y)
  
  x, y = 1, 2
  print(x, y)
  
  print(x, y)
  x, y = y, x
  print(x, y)
  ```

#### 수치형(Numbers)

##### int(정수)

- 모든 정수는 int로 표현

- 진수

  - 10진수 :  0d
  - 8진수 : 0o
  - 2진수 : 0b
  - 16진수 : 0x

  ```python
  binary_number = 0b10
  octal_number = 0o10
  decimal_number = 10
  hex_number = 0x10
  
  print(f"""
  2진수 : {binary_number}
  8진수 : {octal_number}
  10진수 : {decimal_number}
  16진수 : {hex_number}
  """)
  ```

- 오버플로우 

  > 표현할 수 있는 수의 범위를 벗어나면 기대한 값이 출력되지 않는 현상

  > 파이썬에서는 메모리를 유동적으로 사용 가능하기 때문에 정수 자료형에서 오버플로우 현상이 발생하지 않음

##### float(부동소수점, 실수)

- 실수는 float로 표현됨

- 항상 같은 값으로 일치되지 않음

  - 컴퓨터가 2진수를 통해 숫자를 표현하는 과정에서 생기는 오류

  - 실수의 경우 실제로 값을 처리하기 위해서는 조심할 필요가 있음

  - 값이 같은지 비교하는 과정에서 문제 발생
  
    ```python
    5.1 - 3.11 == 1.99
    
    >> False
    ```
    
  - 해결 방법
  
    ```python
    a = 5.1 - 3.11
    b = 1.99
    
    abs(a-b) <= 1e-10
    
    >> True
    ```
  
    > sys 모듈을 통해 처리하는 방법
  
    ```python
    import sys
    abs(a-b) <= sys.float_info.epsilon
    
    >> True
    ```
  
    > math 모듈을 통해 처리하는 방법 (기억해!!)
  
    ```python
    import math
    math.isclose(a,b)
    
    >> True
    ```

- 반올림 하는 법

  > round함수는 반올림 함수임
  >
  > , 뒤 숫자는 그 자리까지 반올림 하라는 표시

  ```python
  round(5.1 - 3.11, 2)
  
  >> 1.99
  ```

##### complex(복소수)

- 복소수는 허수부를 j로 표현함

  ```python
  a = 3 -4j
  type(a)
  
  >> complex
  ```

- 복소수와 관련된 메소드를 확인해보자

  - 허수부
  - 실수부
  - 켤레복소수

  ```python
  print(a.imag)
  print(a.real)
  print(a.conjugate())
  
  >> -4.0
  >> 3.0
  >> (3+4j)
  ```

#### Bool

- 비교/논리 연산을 수행하는 등 여러 방면에서 활용됨

- True 와 False

  ```python
  print(type(True))
  type(False)
  
  >> <class 'bool'>
  >> bool
  ```

- False로 변환되는 예

  > 0,   0.0,   ( ),   [ ],   { },   '  ',   None

- 형변환에서 추가적으로 다루는 내용

  ```python
  print(bool(0))
  print(bool(1))
  print(bool(None))
  print(bool([]))
  print(bool({}))
  print(bool([1, 2, 3]))
  print(bool("asdf"))
  print(bool(""))
  
  >> False
  >> True
  >> False
  >> False
  >> False
  >> True
  >> True
  >> False
  ```

#### None

- 값이 없음을 표현하기 위해 존재

  ```python
  type(None)
  
  >>> NoneType
  ```

  > 변수에 저장해서 확인해보자. None은 변수 자체가 없음

  ```python
  a = None
  print(a)
  
  >> None
  ```

#### 문자형(String)

##### 기본 활용법

> 문자열은 '  '나 "  "를 활용하여 표현 가능하며, 문자열을 묶을 때 동일한 문장부호를 사용해야 함
>
> 하나의 문장부호를 선택해 유지하는 것을 권함 (나는 ' ' pick!)

- 사용자에게 받은 입력(input( ))은 기본적으로 str임

  ```python
  age = input()
  print(age)
  print(type(age))
  ```

- 문자열 안에 문장부호(' ', " ")가 활용될 경우

  - 이스케이프 문자(\\)를 같이 사용해 해결하는 방법

    ```python
    print("엄마가 말했다. \"창희야 밥 먹어라!!!!!\"")
    ```

  - 서로 다른 문장부호를 통해 해결하는 방법

    ```python
    print('엄마가 말했다. "창희야 밥 먹어라!!!!!" ')
    ```

- 여러 줄에 걸쳐있는 문장일 경우, 반드시 """  """를 사용

  ```python
  print("""
  첫 번째 문장
  두 번째 문장
  끝나는 문장
  """)
  ```

  > string interpolation도 가능

  ```python
  a = "안녕하세요"
  print(f"""
  {a}
  반갑습니다.
  """)
  ```

##### 이스케이프 문자열

> 문자열을 활용하는 경우 \를 사용

| 예약문자 |   내용(의미)    |
| :------: | :-------------: |
|    \n    |     줄바꿈      |
|    \t    |       탭        |
|    \r    |   캐리지리턴    |
|    \0    |    널(Null)     |
|   `\\`   |       `\`       |
|    \'    | 단일인용부호(') |
|    \"    | 이중인용부호(") |

- 이스케이프 문자열을 조합하여 프린트해보자

  > 크롤링하거나 데이터 정제(?)할 때 많이 쓰게될 것

  ```python
  print("안녕하세요 \n그리고 \t 반갑습니다")
  print("1234567\rabcd")
  print("1$는 1200\\입니다.")
  
  >> 안녕하세요 
     그리고 	   반갑습니다
  >> abcd567
  >> 1$는 1200\입니다.
  ```

- end 옵션을 사용해보자

  > 기본적으로 \n 상태인데 \t를 넣어줌으로써 한 줄로 작성됨

  ```python
  print("내용을 출력해보자", end = "\t")
  print("옆으로 붙어라")
  
  >> 내용을 출력해보자	옆으로 붙어라
  ```

  > end 옵션은 이스케이프 문자열이 아닌 다른 것도 가능함

  ```python
  print("다른 것도 가능합니다", end = "!")
  print("이것도", end = "?????")
  print("기본으로 print는 개행을 한다")
  
  >> 다른 것도 가능합니다!이것도?????기본으로 print는 개행을 한다
  ```

##### String interpolation

> %-formatting
>
> str.format()
>
> f-strings

- name 변수에 이름을 입력한 후 세 가지 방법을 활용해 출력해보자

  ```python
  name = "subin"
  ```

  > %-formatting

  ```python
  "반갑습니다 %s" % name
  
  >> '반갑습니다 subin'
  ```

  > str.format()

  ```python
  "반갑습니다. {} {}".format(name, name)
  
  >> '반갑습니다. subin subin'
  ```

  > f-strings

  ```python
  f'반갑습니다 {name}'
  
  >> '반갑습니다 subin'
  ```

- f-string에서는 형식 지정 가능

  > datetime 모듈로 오늘을 표현해보자

  ```python
  import datetime
  today = datetime.datetime.now()
  print(today)
  f'오늘은 {today:%Y}년 {today:%m}월 {today:%d}일 입니다.'
  
  >> 2019-07-18 18:40:19.015452
  >> '오늘은 2019년 07월 18일 입니다.'
  ```

- 연산과 출력 형식 지정 가능

  > 연산과 숫자 출력형식을 지정해보자

  ```python
  pi = 3.141592
  f'원주율은 {pi:.3}입니다. 반지름이 2일 때 원의 넓이는 {pi*2*2}입니다.'
  
  >> '원주율은 3.14입니다. 반지름이 2일 때 원의 넓이는 12.566368입니다.'
  ```

