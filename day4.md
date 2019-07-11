# 2019.07.11.목

/는 루트, 최상단을 의미

### 페이지 만들기 (라우트 설정하기 - 라우팅)

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/hi")
def hi():
    return "안녕하세요!!!"
```

return 2개 쓰면 안됨

첫번째만 실행하고 중단되기 떄문



### 웹페이지 만들기  

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
    
@app.route("/hi")
def hi():
    return "안녕하세요!!!"

@app.route("/html_tag")
def html_tag():
    return "<h1>안녕하세요</h1>"

@app.route("/html_tags")
def html_tags():
    return """
    <h1>안녕하세요</h1>
    <h2>반갑습니다</h2>
    """

import datetime
@app.route("/dday")
def dday():
    today = datetime.datetime.now()
    endday= datetime.datetime(2019,11,29)
    d = endday-today
    return f"1학기 종료까지 {d.days}일 남음!!"

@app.route("/html_file")
def html_file():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```



### 동적인 웹페이지 만들기 (라우트를 변수화)

```python
@app.route("/greeting/<string:name>")
def greeting(name):                             -----> 이거
    return f"안녕하세요 {name}님!"
```



### 숫자 구하기 (라우트를 변수화)

```python
@app.route("/cube/<int:num>")
def cube(num):
    return f"{num}의 세제곱은 {num**3}입니다!"        # 나의방법

@app.route("/cube/<int:num>")
def cube(num):
    return f"{num}의 세제곱은 {num**3}입니다!"        #선생님방법
```



### 숫자 구하기 (라우트를 변수화 & html페이지를 만들면서 해보기)

```python
@app.route("/cube_html/<int:num>")
def cube_html(num):
    cube_num = num**3
    return render_template("cube.html", num_html=num, cube_num_html=cube_num)
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <strong>{{num_html}}</strong>  의 세제곱은 <i>{{cube_num_html}}</i> 입니다.
</body>
</html>
```

html에서 {{}} 중괄호를 두개 연속으로 사용하면 파이썬 문법을 그대로 가져와 사용할 수 있다.

! render_template을 사용하니 원래 html에서 없는 문법이었으나 사용이 가능해짐. 그러나 주석에 {{}}를 사용한다면 이것도 읽힌다! 그렇다면 어떻게 해야할까? => {* {{}} *}???????





### 이미지를 활용하여 랜덤으로 점심 추천하기

```python
import random
@app.route("/lunch")
def lunch():
    menu = {
        "짜장면":"http://pds1.egloos.com/pds/200812/25/19/b0063319_4953836d99965.jpg",
        "짬뽕":"https://www.simbata.co.kr/img_src/s600/1231/12310391.jpg",
        "스파게티":"https://www.tefal.co.kr/medias/?context=bWFzdGVyfHJvb3R8MjUyMTF8aW1hZ2UvanBlZ3xoMmYvaGRlLzkzMzg2Mzc5MTAwNDYuanBnfDQ4MzFlN2NlZjMwOTIxNmJmNDE3NjBiZjU0NzA3Mzk5ZDE2YmIzZDk4NTUyOWUzNGM4MmZiN2UwODA1YmY1MGE",
    }
    menu_list = list(menu.keys())  # ["짜장면", "짬뽕","스파게티"]
    pick = random.choice(menu_list)
    img = menu[pick]
    
    return render_template("lunch.html", pick=pick, img=img)

```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h3>오늘의 점심은 {{pick}} 어떠세요???</h3>
    <img src="{{img}}" alt="">
</body>
</html>
```





### html안에서도 if문을 사용하여 나타낼 수 있다. (로그인 관련 버튼들,,)

```python
@app.route('/greeting_html/<string:name>')
def greeting_html(name):
    return render_template("greeting.html", name=name)

```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {% if name == "수빈" %}
        <p style="color:violet">{{name}}</p> 아 안녕!!
    {% else %}
        <p style="color:skyblue">{{name}}</p> 님 안녕하세요!!!
    {% endif %}
</body>
</html>
```





### 영화 리스트들을 세로로 나열하여 보여주기

```python
@app.route('/movies')
def movies():
    movie_list = ['스파이더맨','토이스토리','알라딘','존윅']
    return render_template("movies.html", movie_list = movie_list)
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <ol>
        {% for movie in movie_list %}
            <li>{{movie}}</li>
        {% endfor %}
    </ol>
    
</body>
</html>
```



폴더 옮기는 방법이랑, 폴더명 바꾸는 거!!!! 이따 물어보기





주소창에서 url보면     ? 뒤에 &로 구분이 되어있고, 딕셔너리 형태임.  ?     =      &     =       &      =       &

매개변수들 = arguments



### 페이크 창

```python
@app.route("/naver")
def naver():
    return render_template("naver.html")

```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>여기는 네이버 페이크 창입니다.</h1>

    <form action="https://search.naver.com/search.naver">
        <input type="text" name="query">
        <input type="submit" name="hihi">
    </form>
</body>
</html>
```

form 많이 사용할 것이다.

action이랑 같이 잘 이용함.

?전 까지는 실제 주소 창임



### HTML input Tag

```python
#example
<form action="/action_page.php">
  First name: <input type="text" name="fname"><br>
  Last name: <input type="text" name="lname"><br>
  <input type="submit" value="Submit">
</form>
```

#### Attributes

type :  Specifies the type <input> element to display

​			button
​			checkbox
​			color
​			date 
​			datetime-local 
​			email 
​			file
​			hidden
​			image
​			month 
​			number 
​			password
​			radio
​			range 
​			reset
​			search
​			submit
​			tel
​			text
​			time 
​			url
​			week



#### 입력한 내용을 아스키코드로 바꿔주기

```python
@app.route('/text')
def text():
    return render_template("text.html")

import requests

@app.route('/result')
def result():
    raw_text = request.args.get('raw')
    url = "http://artii.herokuapp.com/make?text="
    res = requests.get(url+raw_text).text
    return render_template("result.html", res=res)

```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>입력한 글자를 아스키 코드로 바꿔줍니다.</h1>
    <form action="/result">
        <input type="text" name="raw">
        <input type="submit" value="변경">

    </form>
</body>
</html>
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=<device-width>, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>짜란~ 결과는 다음과 같습니다.</h1>
    <pre>{{res}}</pre>
</body>
</html>
```

###### 결과

```
   _____       ____  _       
  / ____|     |  _ \(_)      
 | (___  _   _| |_) |_ _ __  
  \___ \| | | |  _ <| | '_ \ 
  ____) | |_| | |_) | | | | |
 |_____/ \__,_|____/|_|_| |_|
```



#### 랜덤게임

아니...어케 만들어,,



```python
@app.route("/von")
def von():
    return render_template("von.html")

import random
@app.route("/vong")
def vong():
    menu = {
        "짜장면":"http://pds1.egloos.com/pds/200812/25/19/b0063319_4953836d99965.jpg",
        "짬뽕":"https://www.simbata.co.kr/img_src/s600/1231/12310391.jpg",
        "스파게티":"https://www.tefal.co.kr/medias/?context=bWFzdGVyfHJvb3R8MjUyMTF8aW1hZ2UvanBlZ3xoMmYvaGRlLzkzMzg2Mzc5MTAwNDYuanBnfDQ4MzFlN2NlZjMwOTIxNmJmNDE3NjBiZjU0NzA3Mzk5ZDE2YmIzZDk4NTUyOWUzNGM4MmZiN2UwODA1YmY1MGE",
    }
    # 여기서 이미지를 가져올 때 http로 시작해야 돼! 그리고 이미지 주소 복사를 눌러주라구!
    menu_list = list(menu.keys())  # ["짜장면", "짬뽕","스파게티"]
    pick = random.choice(menu_list)
    img = menu[pick]
    return render_template("vong.html", pick=pick, img=img)
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h1>이름을 입력해주세요</h1>
    <form action="/vong">
        <input type="text" name="test">
        <input type="submit">
    </form>
</body>
</html>
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <h3>당신과 어울리는 음식은 {{pick}} 입니다.</h3>
    <img src="{{img}}" alt="">

</body>
</html>
```



#### 로또번호와 내 번호가 일치하는지 알아보기

```python
@app.route("/lotto")
def lotto():
    return render_template("lotto.html")

@app.route("/lotto_result")
def lotto_result():
    # 사용자가 입력한 정보를 가져오기
    numbers = request.args.get('numbers').split()
    user_numbers = []
    for n in numbers:
        user_numbers.append(int(n))

    # 로또 홈페이지에서 정보를 가져오기
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    lotto_numbers = res.json()

    winning_numbers = []
    for i in range(1,7):
        winning_numbers.append(lotto_numbers[f'drwtNo{i}'])
    bonus_number = lotto_numbers['bnusNo']

    result = "1등"

    matched = len(set(user_numbers) & set (winning_numbers))
    if matched == 6:
        result = "1등"
    elif matched == 5:
        result = "3등"
    elif matched == 4:
        result = "4등"
    elif matched == 3:
        result = "5등"
    else:
        result = "꽝"
        
    return render_template("lotto_result.html", u=user_numbers, w=winning_numbers, r=result, b=bonus_number)

# 아니 로또 2등 어떻게 하는겨
로또 2등은 
	elif matched == 5: 
        if bonus_number in user_numbers : 
            result = "2등"
        else :
            result = "3등"
            
이렇게!
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    <form action = "/lotto_result">
        <input type="text" name="numbers">
        <input type="submit">
    </form>
</body>
</html>
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>
<body>
    {{u}}
    {{w}}
    {{b}}
    {{r}}
</body>
</html>
```







교집합은 &로