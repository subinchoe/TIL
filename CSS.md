# CSS

> HTML에서 구조화를 이루지 못했다면 CSS를 아무리 잘해도 소용이 없다!
>
> `ex` 
>
> ​	h1 {
>
> ​	color: blue;
>
> ​	fontsize: 10;
>
> ​	}
>
> ​	h1은 selector, color는 property, blue는 값

## CSS 활용하기

### 00_intro.html & 00_intro.css

#### 내부 스타일 시트 (Internal CSS)

- Inline

  - Inline은 지양하자. 앞으로 쓰일 일이 거의 없을 걸

    > Inline은 새로운 줄을 만들지 않고 필요한 너비만 차지하는 별로 좋지 않은 요소
    >
    > `ex` < h1 style="color:red;">CSS intro< /h1>
    >
    > h1 태그에 꾸미고 싶은 요소들을 다 집어넣으니 얼마나 불편하니!!!!

  ```html
  <!DOCTYPE html>
  <html lang="en">    
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
  </head>  
  <body>
      <h1 style="color:red;">CSS intro</h1>
  </body>  
  </html>
  ```

- Embbeding

  - 앞으로 쓰일 일이 좀 있을 걸

    > `ex` body에 h2 태그를 열고 내용을 적었다면, 위의 head에서 style이라 쓰고 h2에 적용시키고 싶은 요소들을 중괄호로 열어 적는다.

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <style>
          h2 {
              color: blue;
              font-size: 100px;
          }
      </style>
  </head>
  <body>
      <h2>CSS is awesome</h2>
  </body>
  </html>
  ```

  <br>

#### 외부 스타일 시트 (External CSS)

- Link file (외부 참조)

  - 앞으로 쓰일 일이 좀 많을 걸
  
  ```html
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <link rel="stylesheet" href="00_intro.css">
  </head>
  <body>
      <p>Lorem ipsum dolor sit amet.</p>
</body>
  ```
  
  ```css
  p {
      color: green;
}
  ```
  
  > html에서 css를 불러와야함
  >
  > < head >의 맨 마지막 부분에서 링크를 불러오자!

> **lorem 5은 의미없는 단어 5개를 쭉 나열해줌.**

- css_value

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <link rel="stylesheet" href="01_css_val.css">
  </head>
  <body>
      <p id="hello">안녕하세요</p>
      <p id="welcome">반갑습니다</p>
      <p id="lunch">점심시간입니다</p>
      <p di="snack">오늘 간식은 도시락</p>
      <div>
          <h1>배고파</h1>
      </div>
  
      <h1 id="menu">오늘의 메뉴</h1>
  </body>
  </html>
  ```

  ```css
  /* 이건 바로 CSS의 주석! */
  /* px 사용*/
  #hello {
      font-size: 50px;
  }
  /* % 사용*/
  #welcome {
      font-size: 50%;
  }
  /* em은 기본 크기에서 배수로 늘려주는 것 */
  #lunch {
      font-size: 10em;
  }
  /* div는 부모 */
  div {
      width: 50%;
  }
  /* h1은 자식, 부모의 width를 상속 받아서 결국 50% * 50% = 25%가 된다. */
  h1 {
      width: 50%;
  }
  /* rem은 뭐양 */
  #snack {
      font-size: 0.5rem;
  }
  /* viewport 단위!! */
  #menu {
      background-color: red;
      width: 50vw;
      height: 50vh;
  }
  ```

  > #붙이면 id값을 찾아줌
  >
  > ex ) #hello >> id="hello"
  >
  > .붙이면 class값 찾아줌

- box!

  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta http-equiv="X-UA-Compatible" content="ie=edge">
      <title>Document</title>
      <link rel="stylesheet" href="02_box.css">
  </head>
  <body>
      <div class="margin border"></div>
      <div class="margin padding"></div>
      <div class="margin border"></div>
      <div class="margin padding"></div>
      <div class="margin-1"></div>
      <div class="margin-2"></div>
      <div class="margin-3"></div>
      <div class="margin-4"></div>
  
  </body>
  </html>
  ```

  ```css
  div {
      width: 100px;
      height:100px;
      background-color: rgba(180, 100, 200, 50);
  }
  
  .margin {
      margin-top: 10px;
      margin-bottom: 10px;
      margin-left: 10px;
      margin-right: 10px;
  }
  
  .padding {
      padding-top: 20px;
      padding-bottom : 10px;
  }
  
  .border {
      border-width: 2px;
      border-color: blueviolet;
      border-style: dotted;
      /* 위에 세 개를 축약한 것 */
      border: 3px blueviolet dotted;
  }
  /* 상하좌우 모두 10 */
  .margin-1 {
      margin: 10px;
      }
  /* 상하 10 좌우 20 */
  .margin-2 {
      margin: 10px 20px;
  }
  /* 상 10 좌우 20 하 30 */
  .margin-3 {
      margin: 10px 20px 30px;
  }
  /* 상 10 우 20 하 30 좌 40 */
  .margin-4 {
      margin: 10px 20px 30px 40px;
  }
  ```

  