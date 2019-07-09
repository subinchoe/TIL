# 2019.07.08.월
## 파이썬의 3형식
1. 저장
2. 조건(if)
3. 반복(while)

## startcamp-day1

### 4차 산업혁명
> 한잔 두잔 들어가는 술잔 

#### 소프트웨어의 발전

- 그딴 거 없다 열심히 코딩하자
- 열심히 파이썬 공부하기

1. 첫번째
2. 두번째

	1. 2-1번째

### 파이썬 기본 문법
#### if문(조건문)

```python
if(True):
		print("if문 안쪽입니다.")
```

#### 내장함수
`print()`는 파이썬이 가지고 있는 내장함수이다.



## 오늘 배웠던 내용
- `은 code block의 기능을 가지고 있음.

- 꼭 기억하기
  - 대/소문자
  - 띄어쓰기
  - 스펠링
  
- 리스트는 []

- 딕셔너리는 {}
  
  - "키" : "밸류"
  
- while은 조건을 달성하면 탈출! *<u>종료조건 필수</u>*

- for는 데이터를 끝까지 다 돌면 탈출! *<u>종료조건 불필요</u>* **(while 보다는 for)**

- for i in list

  ```python
  greeting = "hello"
  
  for i in range(15):
    print(i)
    print(greeting)
  #hello를 15번 연속으로 나타내기!!!!
  ```

  

- 리스트나 딕셔너리가 여러 가지 숫자나 문자열들의 배열들은 복수형으로 나타내기
- for는 리스트의 숫자 또는 문자열을 하나씩 수행하기 때문에 단수형으로 나타내기
- 요청(**클라이언트**) ↔ 응답(**서버**)
- 도움이 되는 사이트 : 자소설닷컴
- range(1,46) = 1이상 46미만

```python
import random
numbers = list(range(1,46))

pick = random.sample(numbers,6)
print(sorted(pick))
#제발 로또 돼라! 로또 번호 추천하는 코드
```

- **import는 서랍에서 꺼내기 역할?????** 잘 이해가 안 됨. 센세요!

  > 이것은 무엇일꼬? 

```python
import datetime

today = datetime.datetime.now()

print (today.strftime("%Y.%m.%d"))
#오늘 며칠이야?(년.월.일)
```

```python
import random

# 원하는 식당과 전화번호를 {}안에 넣어주세요
phonebook = { 
  "국민떡볶이" : "062-999-9999",
  "버거킹" : "062-888-8888",
  "공차" : "062-777-7777"
}
choice = random.choice(list(phonebook.keys()))
print(f"{choice} : {phonebook[choice]}")
#오늘 뭐 먹지? 배달 음식 랜덤 추천!
```

```python
import requests
from bs4 import BeautifulSoup

url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageSize=10&pageNo=1&startPage=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.6'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
dong = soup('item')[7]
location = dong.stationName.text
time = dong.dataTime.text
dust = int(dong.pm10Value.text)
# 아래의 코드가 잘 실행되는지 보려면 dust = 80 처럼 값을 직접 정해서 넣어보기
print(f"{time} 기준 {location}의 미세먼지 농도는 {dust}입니다.")

# 아래에 코드를 작성해주세요

if dust>150:
    print("매우나쁨")
elif 80<dust<=150:
    print("나쁨")
elif 30<dust<=80:
    print("보통")
else:
    print("좋음")

# 위 방법도 됨. 좀 더 개발자스럽게 꾸며본다면,
# if dust > 150:
#     print("매우 나쁨")
# elif dust > 80 and dust <= 150:
#     print("나쁨")
# elif 30 < dust <= 80:
#     print("보통")
# else:
#     print("좋음")

print(url)
#미세먼지 시러시러잉! 공공데이터포털에서 tpi를 알 수 있대!! 좀 어렵다ㅠ
```

아!!!! 갑자기 생각난건데 7월 31일까지 학사시스템인가 진로뭐시기 올리랬는데,,ㅠ 까먹지 말자