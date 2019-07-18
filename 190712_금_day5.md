# 2019.07.12.금

## 텔레그램 봇 만들기

### 아래의 기능을 가진 봇을 만들다

- 점심 메뉴 랜덤 추천
- 로또 번호 랜덤 추천
- 오늘 날짜
- 영화 장르 랜덤 추천
- 놀이공원 랜덤 추천
- 제주도 여행지 랜덤 추천
- 번역

```python
# app.py

from flask import Flask, request, render_template
from decouple import config
import requests
import random
import datetime

app = Flask(__name__)

api_url = "https://api.telegram.org"
token = config("TELEGRAM_TOKEN")
chat_id = config("CHAT_ID")
naver_id = config("NAVER_ID")
naver_secret = config("NAVER_SECRET")

@app.route("/write")
def write():
    return render_template("write.html")

@app.route("/send")
def send():
    msg = request.args.get('msg')
    url = f"{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={msg}"
    res = requests.get(url)
    return render_template("send.html")

@app.route(f"/{token}", methods=['POST'])
def telegram():
    print(request.get_json())
    data = request.get_json()
    user_id = data.get('message').get('from').get('id')
    user_msg = data.get('message').get('text')

    if data.get('message').get('photo') is None:

        if user_msg == "점심":
            menu_list = ["삼계탕", "철판낙지볶음밥", "물냉면"]
            result = random.choice(menu_list)
        elif user_msg == "로또":
            numbers = list(range(1,46))
            result = sorted(random.sample(numbers, 6))
            #sorted는 오름차순으로 정렬해주는 함수
        elif user_msg == "날짜":
            today = datetime.datetime.now()
            result = today.strftime("%Y.%m.%d")
        elif user_msg == "영화":
            movie_list = ["로맨스","코미디","액션","누와르","스릴러","미스터리","모험","공포","전쟁","드라마","가족","애니","범죄","재난","SF","스포츠","뮤지컬"]
            result = random.choice(movie_list)
        elif user_msg == "놀이공원":
            amusementpark_list = ["에버랜드","롯데월드","패밀리랜드","경주월드","대전오월드","대구이월드","서울랜드"]
            result = random.choice(amusementpark_list)
        elif user_msg == "제주도여행":
            travel_list = ["성산일출봉","섭지코지","협재해수욕장","중문색달해변","정방폭포","오설록티뮤지엄"]
            result = random.choice(travel_list)
        elif user_msg[0:2] == "번역":
            # 번역 안녕하세요 저는 누구입니다.
            raw_text = user_msg[3:]
            papago_url = "https://openapi.naver.com/v1/papago/n2mt"
            data = {
                "source":"ko",
                "target":"en",
                "text":raw_text
            }
            header = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
            res = requests.post(papago_url,data=data, headers=header)
            translate_res = res.json()
            translate_result = translate_res.get('message').get('result').get('translatedText')
            result = translate_result
        else:
            result = user_msg
    else:
        # 사용자가 보낸 사진을 찾는 과정
        result = "찬희"
        file_id = data.get('message').get('photo')[-1].get('file_id')
        file_url = f"{api_url}/bot{token}/getFile?file_id={file_id}"
        file_res = requests.get(file_url)
        file_path = file_res.json().get('result').get('file_path')
        file = f"{api_url}/file/bot{token}/{file_path}"
        # print(file)
        # 사용자가 보낸 사진을 클로버로 전송
        res = requests.get(file, stream=True)
        clova_url = "https://openapi.naver.com/v1/vision/celebrity"
        header = {
                'X-Naver-Client-Id':naver_id,
                'X-Naver-Client-Secret':naver_secret
            }
        
        clova_res = requests.post(clova_url, headers=header,files={'image':res.raw.read()})
        
        if clova_res.json().get('info').get("faceCount"):
            # 누구랑 닮았는지 출력
            celebrity = clova_res.json().get('faces')[0].get('celebrity')
            name = celebrity.get('value')
            confidence = celebrity.get('confidence')
            result = f"{name}일 확률이 {confidence*100}입니다."
        else:
            # 사람이 없음
            result = "사람이 없습니다."


    res_url = f"{api_url}/bot{token}/sendMessage?chat_id={user_id}&text={result}"
    requests.get(res_url)

    return '',200

if __name__ == "__main__":
    app.run(debug=True)
```

- sorted는 오름차순으로 정렬해주는 함수
- 내가 받은 api토큰과 아이디를 어떻게 숨길 수 있을까??? 답은 .env !!
- gitignore를 통해 github에 올릴 때 중요 정보가 표시 되지 않게 해줌
- gitignore에서 python, visual studio code, windows 를 선택 후 정보를 모두 긁어와 .gitignore에 저장하기

```python
#test.py

import requests
from decouple import config
token = config("TELEGRAM_TOKEN")
url = f"https://api.telegram.org/bot{token}/"
user_id = config("CHAT_ID")

# send_url = f"{url}sendMessage?chat_id={user_id}&text=호이호이"
# requests.get(send_url)

ngrok_url = "https://subinchoe.pythonanywhere.com"
# 이 url을 통해 평생 나의 봇을 이용할 수 있음!!!!!!!!
webhook_url = f"{url}setWebhook?url={ngrok_url}/{token}"
print(webhook_url)
```

- 이 url을 통해 평생 나의 봇을 통한 서비스를 이용할 수 있음!!!!!!!!

### 이건 뭐였지,,,

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
    <form action="/send">
        <input type="text" name="msg">
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
    <h1>성공적으로 메시지가 전달되었습니다.</h1>
</body>
</html>
```



