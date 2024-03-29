# 복습

## 01. python

### Sequence (Ordered)

> 시퀀스는 데이터의 순서대로 나열된 형식을 나타냄
>
> **주의!! 순서대로 나열된 것이 오름차순이나 내림차순으로 정렬되었다는 의미가 아님**

> 파이썬에서 기본적인 시퀀스 타입
>
> 1. 리스트(list)
> 2. 튜플(tuple)
> 3. 레인지(range)
> 4. 문자열(string)
> 5. 바이너리(binary) : 따로 다루지는 않습니다.

#### list

> 시퀀스에서 유일하게 ==수정 가능==한 아이!!
>
> 리스트는 대괄호 [ ]를 통해 만들 수 있음
>
> 값에 대한 접근은 list[i]를 통해 함

- 빈 리스트를 만들고 어떤 타입인지 보자!

  ```python
  l = [ ]
  ll = list()
  print(type(l))
  print(type(ll))
  
  >> <class 'list'>
  >> <class 'list'>
  ```

- 원소를 포함한 리스트 만들자

  ```python
  location = ['서울', '대전', '광주', '구미']
  location = [
      '서울',
      '대전',
      '광주',
      '구미'
  ]
  
  location[0]
  
  >> '서울'
  ```

#### tuple

> list와 유사하지만, ( )로 묶어서 표현함
>
> 수정 불가능(immutable)하고, 읽기만 가능
>
> 직접 사용보다는 파이썬 내부에서 사용함

- tuple을 만들고 어떤 타입인지 보자

  ```python
  t = (1, 2)
  print(type(t))
  
  t = 1, 2
  print(type(t))
  
  >> <class 'tuple'>
  >> <class 'tuple'>
  ```

- 파이썬 내부에서는 다음과 같이 활용됨

  ``` python
  x, y = 1, 2 >> 실제로는 tuple로 처리되는 거임 x, y = (1, 2)
  print(x)
  print(y)
  
  >> 1
  >> 2
  
  # 변수의 값을 swap할 때도!!!
  x, y = (y, x)
  print(x)
  print(y)
  
  >> 2
  >> 1
  ```

- 수정 불가능함을 보여주는 예

  ```python
  a = (1, 2, 3)
  print(a[1]) >> 2
  
  b = [1, 2, 3]
  b[1] = 5
  print(b) >> [1, 5, 3](list니까 수정이 가능하다)
  
  a[1] = 5
  print(a) >> Error(tuple은 수정이 불가능해서 오류난거야)
  ```

#### range()

> range는 숫자의 시퀀스를 나타내기 위해 사용됨

- 기본형  range(n)

  > 0부터 n-1까지 값을 가짐

  ```python
  list(range(5))
  
  >> [0, 1, 2, 3, 4]
  ```

- 범위 지정  range(n, m)

  > n부터 m-1까지 값을 가짐

  ```python
  list(range(4, 9))
  
  >> [4, 5, 6, 7, 8]
  ```

- 범위 및 스텝 지정  range(n, m, s) 

  > n부터 m-1까지 +s만큼 증가한다 (s는 step을 의미)

  ```python
  list(range(0, -10, -1))
  
  >> [0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
  ```

#### 시퀀스에서 활용할 수 있는 연산자/함수

| operation  | 설명                              |
| ---------- | --------------------------------- |
| x in s     | containment test                  |
| x not in s | containment test                  |
| s1 + s2    | concatenation                     |
| s * n      | n번만큼 반복하여 더하기(= 곱하기) |
| s[i]       | indexing                          |
| s[i:j]     | slicing                           |
| s[i:j:k]   | k간격으로 slicing                 |
| len(s)     | 길이                              |
| min(s)     | 최솟값                            |
| max(s)     | 최댓값                            |
| s.count(x) | x의 개수                          |

- containment test

  ```python
  a = 'string'
  print('i' in a)
  
  l = [1, 2, 3]
  print(5 not in l)
  
  >> True
  >> True
  ```

- concatenation

  ```python
  print('hello' + 'bye')
  print([1, 2, 3] + [1, 2, 3])
  
  >> hellobye
  >> [1, 2, 3, 1, 2, 3]
  ```

- n번만큼 반복하여 더하기

  ```python
  l = [0] * 6
  print(l)
  
  a = "hi" * 10
  print(a)
  
  >> [0, 0, 0, 0, 0, 0]
  >> hihihihihihihihihihi
  ```

- indexing & slicing

  ```python
  location = ['서울', '대전', '광주', '구미']
  location[1]
  
  >> '대전'
  
  location[2 : 4] # 2 이상 4 미만
  
  >> ['광주', '구미']
  ```

- k 간격으로 slicing

  ```python
  numbers = list(range(31))
  print(numbers[0::3])
  
  >> [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
  ```

- 길이

  ```python
  len(numbers)
  
  >> 31
  # 이건 위의 range(31) 때문에 이런 결과가 나온거야!
  # slicing을 했지만 print로 감싸줬기 때문에 출력만 한 거고, 출력된 값이 저장된 형태는 아니라는거지!!
  ```

- 최댓값, 최솟값

  ```python
  min(numbers)
  max(numbers)
  
  >> 0
  >> 30
  ```

- 특정한 것의 개수를 확인

  ```python
  numbers = [1, 2, 3, 3, 5]
  numbers.count(3)
  
  >> 2
  # 이게 range야? 라고 생각했지만 numbers라는 list를 순서대로 세고 있으니까 맞아!
  ```

### Unordered

> set과 dictionary는 기본적으로 수정 가능하며, ==순서==가 없음

#### set

> 수학에서의 집합과 동일하게 처리됨
>
> { }를 통해 만들며, 순서가 없고 중복된 값이 없음

| 연산자/함수       | 설명   |
| ----------------- | ------ |
| a - b             | 차집합 |
| a \| b            | 합집합 |
| a & b             | 교집합 |
| a.difference(b)   | 차집합 |
| a.union(b)        | 합집합 |
| a.intersection(b) | 교집합 |

- 연산자들을 활용해보자

  ```python
  a = {1, 2, 3}
  b = {3, 6, 9}
  print(a - b)
  print(a | b)
  print(a & b)
  
  >> {1, 2}
  >> {1, 2, 3, 6, 9}
  >> {3}
  ```

- set은 중복이 존재하지 않는다구

  ```python
  a = {1, 1, 1}
  print(a)
  
  >> {1}
  ```

- set을 활용해 list의 중복된 값 없애기

  ```python
  l = [1, 2, 3, 1, 2, 3, 1, 2, 3]
  my_list = set(l)
  print(my_list)
  
  >> {1, 2, 3}
  
  # 다시 리스트로 바꿔보자
  print(list(my_list))
  
  >> [1, 2, 3]
  ```

#### dictionary



### 정리

#### 데이터 타입

