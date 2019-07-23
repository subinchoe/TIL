# 복습

## 01. python

### 연산자

#### 산술 연산자

> 파이썬에서는 기본적인 사칙 연산이 가능

| 연산자 | 내용           |
| ------ | -------------- |
| +      | 덧셈           |
| -      | 뺄셈           |
| \*     | 곱셈           |
| /      | 나눗셈         |
| //     | 몫             |
| %      | 나머지(modulo) |
| \*\*   | 거듭제곱       |

- 나눗셈과 관련된 산술연산자를 활용해보자

  ```python
  print(5/2)
  print(5//2)
  print(5%2)
  
  >> 2.5
  >> 2
  >> 1
  ```

- divmod는 나눗셈과 관련된 함수

  ```python
  print(divmod(5,2))
  
  >> (2, 1)
  ```

- 양수, 음수 표현 가능

  ```python
  p_num = 4
  print(-p_num)
  n_num = -4
  print(-n_num)
  print(+n_num)
  
  >> -4
  >> 4
  >> -4
  ```

#### 비교 연산자

> 수학에서 배운 연산자와 동일하게 값을 비교할 수 있음

| 연산자 | 내용     |
| ------ | -------- |
| a > b  | 초과     |
| a < b  | 미만     |
| a >= b | 이상     |
| a <= b | 이하     |
| a == b | 같음     |
| a != b | 같지않음 |

- 숫자의 대소관계 비교

  ```python
  3 > 6
  
  >> False
  ```

- 같은 숫자인지 확인해보자

  ```python
  3 != 3
  
  >> False
  ```

- 다른 숫자인지 확인해보자

  ```python
  3.0 == 3
  
  >> True
  ```

- 문자열도 같은지 확인해보자

  ```python
  "hi" == "hello"
  
  >> False
  ```

#### 논리 연산자

| 연산자  | 내용                         |
| ------- | ---------------------------- |
| a and b | a와 b 모두 True시만 True     |
| a or b  | a 와 b 모두 False시만 False  |
| not a   | True -> False, False -> True |

> & 와 |은 파이썬에서 비트 연산자이다.

- and와 관련해서 모든 case를 출력

  ```python
  print(True and True)  >>  이것만 True고 나머지 다 False
  print(True and False)
  print(False and False)
  print(False and True)
  ```

- or과 관련해서 모든 case를 출력

  ```python
  print(True or True)
  print(True or False)
  print(False or False) >> 이것만 False고 나머지 다 True
  print(False or True)
  ```

- not을 활용

  ```python
  print(not True) >> False
  print(not False) >> True
  print(not "안녕하세요") >> False
  ```

- and는 a가 참이면 b를 리턴하고, 거짓이면 b를 리턴함 (0은 False값이잖앙!!!)

  ```python
  # and의 단축평가(short-circuit evaluation)
  print(3 and 0) >> 0
  print(5 and 3) >> 3
  print(0 and 3) >> 0
  print(0 and 0) >> 0
  ```

- or은 a가 참이면 a를 리턴하고, 거짓이면 b를 리턴함

  ```python
  # or의 단축평가(short-circuit evaluation)
  print(5 or 3) >> 5
  print(0 or 3) >> 3
  print(3 or 0) >> 3
  print(0 or 0) >> 0
  ```

#### 복합 연산자

> 복합 연산자는 연산과 대입이 함께 이루어짐
>
> 반복문을 통해서 개수를 카운트할 때 많이 사용됨

| 연산자    | 내용       |
| --------- | ---------- |
| a += b    | a = a + b  |
| a -= b    | a = a - b  |
| a \*= b   | a = a \* b |
| a /= b    | a = a / b  |
| a //= b   | a = a // b |
| a %= b    | a = a % b  |
| a \*\*= b | a = a ** b |

- ```python
  cnt = 0
  while cnt < 5:
      print("hello")
      cnt += 1
  # cnt = cnt + 1 이거는 위에 cnt += 1과 같음
  
  >> hello
  hello
  hello
  hello
  hello
  ```

#### 기타 연산자

- Concatenation

  - 숫자가 아닌 자료형은 + 연산자를 통해 합칠 수 있음 (연결의 의미)

    - 문자열끼리 합치자

      ```python
      print("hi" + "bye")
      
      >> hibye
      ```

    - list끼리 합치자

      ```python
      lotto = [1,2,3]
      number = [5,6,7]
      lotto + number
      
      >> [1, 2, 3, 5, 6, 7]
      ```

- Containment Test

  - in 연산자를 통해 속해있는지 여부를 확인할 수 있음

    - 문자열 안에 특정한 문자가 있니?

      ```python
      'z' in 'apple'
      
      >> False
      ```

    - list 안에 특정한 원소가 있니?

      ```python
      1 in [1, 2, 3]
      
      >> True
      ```

    - range 안에 특정한 원소가 있니?

      ```python
      30 in range(1, 46)
      
      >> True
      ```

- Identity

  - is 연산자를 통해 동일한 객체인지 확인할 수 있음

    - id가 같니?

      > 파이썬에서 -5부터 256까지의 id는 모두 동일함

      ```python
      a = 5
      b = 5
      print(a is b)
      
      >> True
      ```

      ```python
      a = 1000
      b = 1000
      print(a is b)
      
      >> False
      ```

- Indexing/Slicing

  - [ ]를 통한 값 접근 및 [ : ]을 통한 슬라이싱

    - 문자열을 인덱싱을 통해 값에 접근하자

      ```python
      "hello"[0]
      
      >> 'h'
      ```

#### 연산자 우선순위

> 0. (  )을 통한 grouping
> 1. Slicing
> 2. Indexing
> 3. 제곱연산자 \*\*
> 4. 단항연산자 +, - (음수/양수 부호)
> 5. 산술연산자 \*, /, %
> 6. 산술연산자 +, -
> 7. 비교연산자, in, is
> 8. not
> 9. and
> 10. or

- 우선순위 확인해보자

  ```python
  (-3) ** 4
  
  >> 81
  ```

  

