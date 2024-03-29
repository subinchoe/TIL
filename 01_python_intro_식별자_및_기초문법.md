# 복습

## 01. python

### 식별자 및 기초 문법

- 변수, 함수, 모듈, 클래스 등을 식별할 때 사용

  - 식별자의 이름은 영문 알파벳, _, 숫자로 구성
  - 대소문자 구별
  - 예약어 사용 불가능 `(ex)` True, False, and, or, not, pass, return, if, elif, etc.
  - 내장함수나 모듈등의 이름으로도 만들면 안 됨.

- 식별자 확인 방법

  ```python
  import keyword
  print(keyword.kwlist)
  
  ## kwlist는 keyword를 list로 나타내는 것.
  ```

- 식별자 오류

  ```python
  str = "hi"
  str(5)
  
  TypeError: 'str' object is not callable
  
  ## ---->는 어느 줄에 오류가 있는지 알려줌.
  ## str = 'hi'에서 str이라는 함수를 변수 이름으로 지정을 해줌으로써
  ## 이 함수의 기능이 사라져 str(5)에서 오류가 나게 됨.
  ```

- docstring
  - """으로 표현
  - 여러 줄의 주석 작성 가능
  - 함수나 클래스 선언 후 해당 설명 위해 활용
  - .__doc__는 docstring을 읽는 기능을 함

- print

  - 한줄로 이어 쓰지 않음 

    ```python
    print('hello')print('hihi')
    ```

  - 해결 방안

    ```python
    print('hello')
    print('hihi')
    ```

    ```python
    print('hello');print('hihi')
    
    ## 이 방법보다는 첫 번째 방법이 훨 낫다.
    ```

  - \ (역슬래시) 이용

    - 참고 : [  ] {  } (  ) 는 \ 없이도 여러 줄 작성 가능

    ```python
    print("
    asdf")
    
    ## 스트링으로 감싸지지 않아서 검은색 글씨로 뜨는거야!
          
    print("\
    asdf")
         
    ## 역슬래시를 씀으로 인해 완성됐어!! 그치만 이 방법도 불편하겠지?
    ```

