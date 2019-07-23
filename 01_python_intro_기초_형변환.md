# 복습

## 01. python

### 기초 형변환(Type conversion, Typecasting)

> 파이썬에서 데이터 타입은 서로 변환할 수 있음

#### 암시적 형변환(Implicit Type Conversion)

> 사용자가 의도하지 않았으나, 파이썬 내부에서 자동으로 형 변환을 하는 경우

- 아래의 상황에서만 가능

  - Bool

  - Numbers(int, float, complex)

    ```python
    # True는 1, False는 0이라구!!!!
    True + 3 
    
    >> 4
    ```

    ```python
    int_num = 3
    float_num = 3.14
    com_num = 3 + 5j
    
    type(int_num + float_num) >> float
    type(int_num + com_num) >> complex
    ```

#### 명시적 형변환(Explicit Type Conversion)

> 위의 상황을 제외하고는 모두 명시적으로 형 변환이 필요함

- string >> integer : 형식에 맞는 숫자만 가능

  ```python
  age = input()
  int(age) + 10
  
  만약 input에 10을 입력했다면
  >> 20
  ```

- integer >> string : 모두 가능

  ```python
  1 + '등' >> Error
  
  str(1) + '등' >> '1등'
  ```

> 암시적 형변환이 되는 모든 경우도 명시적으로 형변환이 가능함

- int( ) : string, float를 int로 변환

  ```python
  a = '3'
  int (a)
  
  >> 3
  ```

  > string은 숫자일 때만 형변환이 가능하다.

  ```python
  a = 'hi'
  int(a)
  
  >> Error
  ```

  > string 3.5를 int로 변환 못함 >> 3.5는 float야

  ```python
  a = '3.5'
  int(a)
  
  >> Error
  ```

- float( ) : string, int를 float로 변환

  ```python
  a = '3.5'
  float(a)
  
  >> 3.5
  ```

- str( ) : int, float, list, tuple, dictionary를 문자열로 변환

  ```python
  fruits = {'apple': '사과'}
  str(fruits)
  
  >> "{'apple': '사과'}"
  ```

  

