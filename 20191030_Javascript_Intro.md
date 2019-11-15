# 20191030_Javascript_Intro

## 06_array_method.js

- `arr.forEach(callback[, thisArg]);`

  > 대괄호는 옵션이므로 신경 안 써도 됨.
  >
  > 배열을 반복할 때는 `forEach`나 `for of`가 편함.

```javascript
// colors 선언
let colors = ['red', 'green', 'blue']

for (let color of colors) {
    console.log(color)
}
// 출력
red
green
blue

colors.forEach(function(color) {
    console.log(color)
})
// 출력
red
green
blue

colors.forEach(function(color, idx, array){
    console.log(color, idx, array)
})
// 출력
red 0 [ 'red', 'green', 'blue' ]
green 1 [ 'red', 'green', 'blue' ]
blue 2 [ 'red', 'green', 'blue' ]

// function() {} >> function()=>{}
// 1단계 화살표 함수
colors.forEach((color, idx, array) => {console.log(color)})
// 2단계 소괄호 생략
colors.forEach(color, idx, array => {console.log(color)})
// 3단계 중괄호 생략
colors.forEach((color, idx, array) => console.log(color))

```

```javascript
// 문제 1
function handlePosts(){
    const posts = [
        {id: 50, title: "javascript"},
        {id: 100, title: "python"},
        {id: 123, title: "css"},
    ]
    for (let i = 0 ; i < posts.length ; i++) {
        console.log(posts[i])
        console.log(posts[i].id)
        console.log(posts[i].title)
    }
}
handlePosts()

// 출력
{ id: 50, title: 'javascript' }
50
javascript
{ id: 100, title: 'python' }
100
python
{ id: 123, title: 'css' }
123
css


// 내가 쓴 코드 (for문 있는 곳에 만들어줘야지.....)
posts.forEach(handlePosts(posts[i], (posts[i].id, posts[i].title)){
    console.log(posts[i].id, posts[i].title)
})

// 정답
function handlePosts(){
    const posts = [
        {id: 50, title: "javascript"},
        {id: 100, title: "python"},
        {id: 123, title: "css"},
    ]
    posts.forEach((post)=>{
        console.log(post)
        console.log(post.id)
        console.log(post.title)
    })
}
handlePosts()

// 문제 2
const images = [
    {height: 10, width: 20},
    {height: 14, width: 25},
    {height: 50, width: 15},
]
const areas = []

// 정답 (function 부터 callback이라 부른다.)
images.forEach(function(image){
    areas.push(image.height * image.width)
})

console.log(areas)
// 출력
// [200, 350, 750]
```

- `arr.map(callback(currentValue[, index[, array]])[, thisArg])`

  > python에서와 같은 역할을 함.

```javascript
const numbers = [1, 2, 3, 4, 5]
const doubleNumbers = []

// forEach 썼을 때
// numbers.forEach(function(number){
//     doubleNumbers.push(number*2)
// })

const double = numbers.map(function(number){
    return number * 2
})
console.log(double)
// 출력
[ 2, 4, 6, 8, 10 ]

// 바로 위와 같은 코드
const double = numbers.map(number =>number * 2)
console.log(double)

const images = [
    {height: 10, width: 20},
    {height: 14, width: 25},
    {height: 50, width: 15},
]

// map을 사용하여 넓이 배열 만들기
const areas = images.map(function(image){
    return image.height * image.width
})
console.log(areas)
```

- `arr.filter(callback(element[, index[, array]])[, thisArg])`

  > python의 filter와 같은 역할

```javascript
// filter
// 예시 1
const numbers = [1, 2, 3, 4, 5]

const evenNumber = numbers.filter(function(number){
    return number % 2 === 0
})
console.log(evenNumber)

// 예시 2
const products = [
    {name: 'cucumber', type: 'vegetable'},
    {name: 'banana', type: 'fruit'},
    {name: 'carrot', type: 'vegetable'},
    {name: 'apple', type: 'fruit'},
]

// 내 풀이
const a = products.filter(function(product){
    return product.type === "fruit"
})
console.log(a)

// 선생님 풀이
const fruit = products.filter((product) => {
    return product.type === "fruit"
})
console.log(fruit)

// 출력
[ { name: 'banana', type: 'fruit' }, { name: 'apple', type: 'fruit' } ]
```

- `arr.reduce(callback[, initialValue])`

  > 각각의 요소에 대한 연산을 해서 리턴하는 함수.

```javascript
// reduce
const scores = [100, 80, 88, 92, 95, 70]

// 여기서는 인자가 두 개이니까 소괄호 생략 안 됨.
// 0은 초기값이고, reduce는 초기값이 필수이다. reduce의 두 번째 인자로 들어가야 하므로 중괄호 뒤에 콤마 찍고 0으로 초기화 해줌.
const total = scores.reduce((total, score)=>{
    return total += score
}, 0)
console.log(total)
// 소괄호는 생략 못 하지만 중괄호는 생략 가능
const total = scores.reduce((total, score) => total += score, 0)
```

- `arr.find(callback[, thisArg])`

  > ddd

```javascript
// find
const users = [
    {name: 'change', location: 'gj'},
    {name: 'justin', location: 'gj'},
    {name: 'tak', location: 'dj'},
    {name: 'junho', location: 'dj'},
    {name: 'neo', location: 'so'},
]

// name이 neo인 사람을 찾아라.
const name = users.find(function(user) {
    return user.name === "neo"
})
console.log(name)
// 출력
{ name: 'neo', location: 'so' }

// location이 dj인 사람을 찾아라.
const location = users.find(function(user) {
    return user.location === "dj"
})
console.log(location)
// 출력
{ name: 'tak', location: 'dj' }

// find는 값을 단 하나만 찾아온다. 처음부터 순서대로 찾는데 위에 해당되는 것이 있으면 그것을 리턴하고 끝난다.
```

## 07_event.html

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
  <div id="my"></div>
  <button id="this-button">CLICK</button>

  <script>
    // 1. 무엇을 => id가 this-button을
    const btn = document.querySelector("#this-button")
    console.log(btn)
    // 2. 언제 => 클릭하면
      // keydown은 click 및 여러 개로 바꿀 수 있음.
      // https://developer.mozilla.org/ko/docs/Web/Events 이곳을 참조
    btn.addEventListener('keydown', function(event){
      // 3. 어떻게 => id가 my인 div에 hello를 넣기
      console.log(event)
      const div = document.querySelector("#my")
      div.innerHTML = "<h1>HELLO</h1>"
    })
  </script>
</body>
</html>
```

## 08_dino.html

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <title>Document</title>
    <style>
      .bg {
        background-color: #f7f7f7;
        display: flex;
        justify-content: center;
        align-items: center;
        min-height: 90vh;
      }
    </style>
  </head>
  <body>
    <div class="bg">
      <img
        id="dino"
        width="100px"
        height="100px"
        src="https://is4-ssl.mzstatic.com/image/thumb/Purple118/v4/88/e5/36/88e536d4-8a08-7c3b-ad29-c4e5dabc9f45/AppIcon-1x_U007emarketing-sRGB-85-220-0-6.png/246x0w.jpg"
        alt="dino"
      />
    </div>

    <script>
      // 1. 무엇을
      const dino = document.querySelector('#dino')
      // 2. 언제
      dino.addEventListener('click', function(){
        // 3. 어떻게
        console.log("아야!!")
      })

      // 1. 무엇을
      // 2. 언제
      document.addEventListener('keydown', (e)=>{
        // 3. 어떻게
        if (e.code === "ArrowLeft") {
          console.log("왼쪽")
          dino.style.marginRight = "50px"
        } else if (e.code === "ArrowRight") {
          console.log("오른쪽")
          dino.style.marginLeft = "50px"
        } else if (e.code === "ArrowUp") {
          console.log("위쪽")
          dino.style.marginBottom = "50px"
        } else if (e.code === "ArrowDown") {
          console.log("아래쪽")
          dino.style.marginTop = "50px"
        } else {
          console.log("다른 키를 눌렀어")
        }
      })

    </script>
  </body>
</html>
```

```javascript
// console창에 입력한 것들.

> const bg = document.querySelector('.bg')

> bg.firstElementChild
// bg가 가지고 있는 첫 번째 원소를 가져옴.
```

