# Dictionary 에서 데이터 빼오기

```python
ssafy = {
    "location": ["서울", "대전", "구미", "광주"],
    "language": {
        "python": {
            "python standard library": ["os", "random", "webbrowser"],
            "frameworks": {
                "flask": "micro",
                "django": "full-functioning"
            },
            "data_science": ["numpy", "pandas", "scipy", "sklearn"],
            "scraping": ["requests", "bs4"],
        },
        "web" : ["HTML", "CSS"]
    },
    "classes": {
        "gj":  {
            "lecturer": "change",
            "manager": "pro-gj",
            "class president": "박선용",
            "groups": {
                "A": ["김선만", "박승재", "공현아", "박선용", "최화경", "정윤선"],
                "B": ["김상돈", "박정우", "김기범", "남선웅", "정진주"],
                "C": ["박승규", "김혁준", "김승연", "김규리", "최수빈"],
                "D": ["고재형", "고태환", "양선", "윤준석", "윤서영"],
                "E": ["정은지", "양예은", "정명한", "창호연", "최동호"]
            }
        },
        "gm": {
            "lecturer": "justin",
            "manager": "pro-gm"
        }
    }
}

```

- 난이도* 

  1. 지역(location)은 몇개 있나요? : list length

  출력예시) 4

  ```python
  print(len(ssafy['location']))  #만약 'locationnnnn'이라는 값을 넣었을 때 keyerror가 난다.
  # print(ssafy.get('location')) 이게 더 좋은 방법. 오류가 나지 않고 none이라는 값을 뽑아주므로 if문 쓸 때 False를 뽑을 수 있음.
  ```

- 난이도** 

  2. python standard library에 'requests'가 있나요? : 접근 및 list in

  출력예시) False

  ```python
  print('requests' in ssafy['language']['python']['python standard library'])
  #print('requests' in ssafy.get('language').get('python').get('python standard library'))
  ```

- 난이도** 

  3. gj반의 반장의 이름을 출력하세요. : depth 있는 접근

  출력예시) 박선용

  ```python
  print(ssafy['classes']['gj']['class president'])
  #print(ssafy.get('classes').get('gj').get('class president'))
  ```

- 난이도*** 

  4. ssafy에서 배우는 언어들을 출력하세요. : dictionary.keys() 반복

  출력 예시) python web

  ```python
  for i in ssafy['language'].keys():
      print(i)
  # language = ssafy.get('language')
  # print(language) 이건 데이터가 잘 나왔는지 확인용
  # for i in language.keys():
  # print(i)
  ```

- 난이도*** 

  5. ssafy gm반의 강사와 매니저의 이름을 출력하세요. dictionary.values() 반복 

  출력 예시) justin pro-gm

  ```python
  for i in ssafy['classes']['gm'].values():
      print(i)
      
  # gm = ssafy.get('classes').get('gm')
  # print(gm)
  # for i in gm.values():
  # print(gm)
  ```

- 난이도***** 

  6. framework들의 이름과 설명을 다음과 같이 출력하세요. : dictionary 반복 및 string interpolation

  출력 예시) flask는 micro이다. django는 full-functioning이다.

  ```python
  for key, value in ssafy['language']['python']['frameworks'].items():
      print(f'{key}는 {value}이다.')
      
  # frameworks = ssafy.get('language').get('python').get('frameworks')
  # for key, value in frameworks.items():
  # print(frameworks)
  ```

- 난이도***** 

  7. 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요. : depth 있는 접근 + list 가지고 와서 random.

  출력예시) 오늘의 당번은 정은지

  ```python
  import random   
  # => not defined가 오류로 나온다면 정의되지 않았다는 것이므로 서랍에서 꺼내주자!!!
  a = ssafy['classes']['gj']['groups']['E']
  print(a)
  b = random.choice(a)
  # random.뒤에는 무수히 많은 것들을 달 수 있어!
  # 그 중에서도 하나를 선택한다면 choice고, 몇 개를 선택하고 싶다면 sample!(이건 중복 안됑)
  print(b)
  
  # e = ssafy.get('classes')('gj')('groups')('E')
  # print(e)
  #import random
  #today = random.choice(e)
  #print(today)
  ```

  