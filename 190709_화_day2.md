# 2019.07.09.화

### CLI

- git bash : 터미널 프로그램, CLI
- 명령줄 인터페이스 - CLI

- GIT BASH 명령어 기초
  - ls :  현재 디렉토리의 위치
    - 하얀색은 파일
    - ~ 은 홈 폴더 (나는 c드라이브 안에 사용자 안에 student)
  - lpwd : 
  - cd : change directory  (cd TLI를 입력하면 TLI폴더로 이동하게 됨.)
  - mkdir : 새로운 디렉토리 생성
  - ..의 의미 : 상위 폴더로 이동 (cd ..은 상위 폴더로 이동!!)
  - .으로 시작하는 폴더는 숨김 폴더임
  - rm : 파일 또는 폴더 지우기
  - mv : 파일을 옮기자! 파일 이름을 수정하자!

##### **Visual Studio Code 실행할 때 <u>저장</u> 필수!**

- 텍스트 코드는 <>     <u>요기</u>     <> 열린 꺽쇠 닫는 꺽쇠 사이에 있는 값 (요기)

- CLI 환경에서는 내가 어디 있는지 알아야함
- 다른 폴더로 들어가려면 cd 폴더이름을 입력해야함
- os는 오버라이팅시스템(운영체제) 



### import os

- r은 raw. 날 것이라는 의미로 이스케이프의 기능 없이 폴더 나누는 기능으로만 쓰는거야를 나타낼 때 씀.

- +는 연결하는 것의 의미



### 환율

```python
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

tr = soup.select('tbody > tr')
for r in tr:
    print(r.select_one('.tit').text.strip())
    print(r.select_one('.sale').text)

# tr = soup.select('tbody > tr') 이거랑 밑에 두 개랑 같음
# tbody = soup.select_one('tbody')
# tr = tbody.select('tr')
```

- requests라는 것을 import를 통해 꺼낸다.
- bs4를 통해 BeautifulSoup을 꺼낸다.
- BeautifulSoup은 text를 더 예쁘게 정리하는 용도임. (물론 우리 눈에서는 보이지 않으나 파이썬을 통해서는 예쁘게 보임)
- parser란 compiler의 일부로 컴파일러나 인터프리터에서 원시 프로그램을 읽어 들여 그 문장의 구조를 알아내는 parsing(구문 분석)을 행하는 프로그램임
- tr = soup.select('tbody > tr')에서 tbody가 tr보다 상위에 있다는 표시. tbody를 먼저 가져오고 tr을 select로 전부 다 가져와!
- 여기서 r은 row의 의미로 행이라는 의미를 가지고 있다.
- for문을 사용하여 문장 하나하나를 돌리고 있다.
- strip은 문자열 함수로 문자열 양쪽 끝을 자르는 역할이며, 제거할 문자를 인자로 전달함 (디폴트는 공백)



### 파일 이름 바꾸기

```python
import os

os.chdir(r"C:\Users\student\startcamp\students")
for filename in os.listdir("."):
    os.rename(filename, filename.replace("SAMSUNG_","SSAFY_"))
```

- chdir은 change directory이다!



### 가짜 이름 만들기

```python
from faker import Faker
import os
f = Faker('ko_KR')
for i in range(100):
    filename = f"{i}_{f.name()}.txt"
    cmd = f"touch {filename}"
    os.system(cmd)
```





### git bash를 통하여 github에 올려보자!

- 현재 자신이 올리고자 하는 폴더의 위치에 있는지 확인해보기
- master라는 표시가 있는 폴더만 github에 올릴 수 있음!!
- 파일 하나를 올리려고 하는데 어떻게 하지??
  1. git add .
  2. git commit -m "하고 싶은 말" 여기서 m이란 message의 약어!
  3. git push origin master
  4. 협업하고 있는 중이라면 git pull origin master를 입력하여 수정된 내용들을 검토해보자!



# 번외

## Typora 사용법

### 1. 제목

\#의 개수에 따라 다양한 크기의 제목을 설정 할 수 있다. (단축키: ctrl + 숫자 1~6)

 

### 2. 코드

\~~~ 혹은 ```을 입력하면 코드블록 기능을 쓸 수 있다.

\```입력 후 글자를 쓰면 그 코드블록의 제목이 된다. java, c, python등의 언어를 입력하면 그 언어에 맞게 코드블록의 내용이 하이라이팅 돼서 나온다.

단순히 강조하고 싶을때는 `강조할 단어`를 쓰면 된다.

```
public static void main(String[] args)
{
    System.out.println("Hello, Typora!");
}
```

 

### 3. 수평선

---를 입력하면 수평선을 넣을 수 있다. 좋다



### 4. 스크롤 이동

화면 왼쪽 아래에 있는 동그라미 표시를 누르면 사이드바가 뜬다. (사이드바의 내용은 변경 가능)

개략으로 해 두면 제목들이 표시되는데, 이 제목들을 클릭하면 제목간 빠른 이동이 가능하다.



### 5. 하이라이팅 표시

** , __ : 진하게.      ** **진하게** **

*, __ : 기울이기.      _ *기울이기* _

*** , ___:       진하게+ 기울이기.

== : 형광펜(환경설정 필요). ==

형광펜

==