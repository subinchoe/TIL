# 2019.07.10.수

## 코딩 해보자!

- open () 여는 것

- w = write의 약자. 쓰겠다

- **폴더 위치 꼭 신경 쓰자!!**

- 컨트롤키+ 슬래시 = 주석넣기가 됨

- r 덮어쓰기, a 추가, w 쓰기

- **들여쓰기도 꼭,,,,**



#### 파일 만들기 및 내용 적기

```python
# f = open("student.txt","w")
# f.write("안녕하세요")
# f.close()

with open ("ssafy.txt", "w") as f:
    f.write("싸피 화이팅!!!")
```



#### 어제 환율 코딩한 것을 .txt로 저장하기

```python
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')

tr = soup.select('tbody > tr')

with open ("exchange.txt", "w") as f:
    for r in tr:
        f.write(r.select_one('.tit').text.strip() + ":" + r.select_one('.sale').text + "\n")

#with open ("exchange.txt", "w") as f:
    #for r in tr:
        #print(r.select_one('.tit').text.strip())
        #print(r.select_one('.sale').text)
        #f.write(r.select_one('.tit').text.strip())
        #f.write(r.select_one('.sale').text + "\n")
#선생님 방식

```



**import는 웬만하면 위에 쓰도록**



**모듈 이름과 똑같은 이름 쓰면 안돼용!!!!!!!**



#### 엑셀파일 만들기

```python
import csv

lunch = {
    "BBQ" : "123123",
    "중국집" : "789789",
    "한식" : "456456"
}

with open("lunch.csv", "w", encoding="utf-8", newline="") as f:
    csv_writer = csv.writer(f)

    for item in lunch.items():
        csv_writer.writerow(item)
```





#### 엑셀파일 만들기 응용

```python
import csv
import requests
from bs4 import BeautifulSoup
url = "https://finance.naver.com/marketindex/exchangeList.nhn"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
tr = soup.select('tbody > tr')

with open ("naver_exchange.csv", "w", encoding="utf=8", newline="") as f:
    csv_writer = csv.writer(f)
    for r in tr:
        print(r.select_one('.tit').text.strip())
        print(r.select_one('.sale').text)
        row = [r.select_one('.tit').text.strip(),r.select_one('.sale').text]
        csv_writer.writerow(row)
```



빗썸 어케해...ㅠ



## HTML&CSS

```python
<!DOCTYPE html>
<html>
    <head>
        <link rel="stylesheet" href="./intro.css">
    </head>
    <body>
        <h1 >HTML</h1>
        <h1 class="blue">CSS</h1>
        <h2 class="blue">HyperText Markup Language</h2>
        <a href="https://www.naver.com/">네이버</a>

        <!-- <태그이름 속성명 = "속성값" 속성명2 = "속성값2">내용</태그이름> -->

        <h3>우리가 공부한 것</h3>
        <ol>
            <li> <strong><i>파이썬</i></strong> </li>
            <li class="blue">HTML</li>
            <li id="git" class="blue">Git</li>
        </ol>
    </body>
</html>
#이것은 HTML!
```

```python
/* 여기는 css파일입니다!!! */
h1 {
background-color:red;
}
a {
color:brown; 
}
.blue {
background-color:blue;
}
#git {
background-color:black;
}
#이것은 CSS!
```



h1 으로 시작하는 것이 기본적임

h2 적고 탭하면 여는 태그 닫는 태그 자동으로 됨

**글자+탭키 : 자동으로 글자 완성됨**

a: 앵커? 링크

```python
<태그이름 속성명 = "속성값" 속성명2 = "속성값2">내용</태그이름> 
#속성명과 속성명2 사이의 띄어쓰기는 매우 중요함

```

- ol : ordered list?
- 알트키 + 키보드 위아래키는 옮기는 기능
- 속성 아무거나 넣을 수 있음 style
- css에서는 세미콜론(;) 으로 닫기
- .이 붙으면 class임(css에서!)
-    <link rel="stylesheet" href="">여는 태그는 있는데 닫는 태그는 없음. 왜냐하면 연결해주기 떄문이지 (내용이 안 들어가니깐)
- 반응형 웹 = toggle 뭐시기



### Resume의 내용 및 형식을 바꿔보자!!

#### 나의 결과물 : https://subinchoe.github.io





