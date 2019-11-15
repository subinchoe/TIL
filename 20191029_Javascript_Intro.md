# 20191029_Javascript_Intro

> 훨씬 편리하다!

`설정을 변경하자`

javascript는 2spaces를 사용하기 때문에 기존에 python할 때 썼던 4spaces에서 바꿔줄 것!

Beautify와 ESLint를 설치함.

## index.html

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
  <script src="./main.js"></script>
</body>
</html>

```

### main.js

```javascript
// console창 자체가 임시로 보여주기 때문에 새로고침 하는 순간 날아간다.

// reload 할 때마다 뜬다.
alert("hello world!!!")

// 여기는 주석입니다.

/* 
여기서부터
여기까지는 
주석입니다.
(여러 줄을 주석처리할 때)
*/

// document.write()은 문서에 나타낼 때 쓰는 것임!!!
// 폰트 크기가 적용되지 않음.
document.write('hello world')
// 폰트 크기가 적용됨.(h1태그)
document.write('<h1>hello world</h1>')

// ''안에 해당하는 태그들을 가져온다.
document.querySelector('h1')
// 가져온 태그의 내부 text를 바꿔준다.
document.querySelector('h1').innerText = "bye"

// 변수 생성할 때 var를 사용한다. 하지만 지금은 잘 쓰지 않는다. 문제점이 많기 때문!!
var name = "subin"
// 변수를 출력하고 싶을 때!! python에서는 print()를 썼지만, javascript에서는 console.log()를 쓴다.
console.log(name)

// 변수 b를 지정
var b = 30
// for () {}이 for문이야!!
// ()안에 조건을 적는 거고, b = 0부터, b < 10 까지이면 for문에서는 실제로 0~9까지 돈다.
// 조건 끼리 구분해주는 건 항상 세미콜론! C언어랑 비슷하다!
for (var b = 0 ; b < 10 ; b++) {
    console.log(b)
}
// var는 function scope래! 그래서 위에서 지정한 b = 30이라는 정보가 날아가고 for문 조건에 적은 var변수가 저장되는 거야!!!
// 마지막 b = 10을 출력해준다. 
console.log(b)

// 우리는 앞으로 문제가 많은 var 대신 let을 쓸 예정!
// let 키워드는 같은 이름의 변수를 한 번만 선언 가능! 할당은 여러 번 가능하다!!!
// let은 데이터 재할당이 가능하다.
let name = "subin"
document.write(name)

name="subinchoe"
document.write(name)
// 처음에 name에 subin을 할당했는데, name에 subinchoe를 다시 할당했더니,
// 재할당한 정보가 문서에 출력됐다.

// const는 데이터 재할당이 불가능하다.
// const 키워드는 같은 이름의 변수를 한 번만 선언 가능!
const loca = "GJ"
document.write(loca)

loca = "seoul"
document.write(loca)
// const는 재할당이 안되는데 같은 변수에 다른 정보를 재할당했더니 오류가 났다.

// 문자열을 합칠 거야!
const first_name = "subin"
const last_name = "choe"
const full_name = last_name + first_name
// h1태그도 스트링으로 묶어줘야 해!!
document.write('<h1>'+full_name+'</h1>')
// 백틱 사용하면 ${}를 사용할 수 있어. python에서 f스트링과 비슷하지!
document.write(`<h1>${full_name}</h1>`)
console.log(`<h1>${full_name}</h1>`)

// alert는 알림 창이고, prompt는 내가 입력한 정보를 전송해주는 알림 창!
const userName = prompt("hello, who are you") // hello, who are you라는 알림이 뜬다.
let message = `<h1>hello! ${userName}</h1>` // 각자 입력하고 싶은 내용을 입력한다.
document.write(message) // 

let message = 
// === 은 비교할 때 사용함
// == 은 비교할 때 사용함
if (userName === "subin") {
    message = `<h1>admin page</h1>`
} else if (userName === "happy") {
    message = `<h1>happy coding</h1>`
} else {
    message = `<h1>hello! ${userName}</h1>`
}
document.write(message)

// const user = "1"
// const num = 1
// // 안에 있는 값을 비교함.
// user == num
// // true
// user === num
// // false

const num1 = 0
const num2 = "0"
// 느슨한 같음(값을 비교)
console.log(num1==num2)
// 엄격한 같음(타입을 비교)
console.log(num1===num2)
```

## 00_variable.js

```javascript

```

## 01_operators.js

