# 20191105_Javascript_review

#### var, let, const

> 밖에서 안을 참조하는 것은 가능하지만 반대는 노노

- var

```js
for (var a=0; a<5; a++){
    console.log(a) // 0부터 4까지 출력
}
console.log(a) // 5를 출력
```

```js
function testA(){
    for (var a=0; a<5; a++){
        console.log(a)
    }
    console.log(a)
}
testA()
console.log(a) // 여기서 오류가 난다. 왜냐면 var는 function scope거든!
```

```js
var a = 0
function testA(){
    for (var a=0; a<5; a++){
        console.log(a)
    }
    console.log(a)
}
testA()
console.log(a)
```



- let

  > 밑의 두 코드는 동일혀~

```js
for(let a=0; a<5; a++){
    console.log(a)
}
console.log(a)
```

혹은

```js
let a = 0
for(a=0; a<5; a++){
    console.log(a)
}
console.log(a)
```

```js
// 재할당이 가능함을 보여준다.
let user2 = {
        name: 'change',
        phone: 'iphone',
    }
    user2 = {}
    console.log(user2)
```



- const

  > const는 for문 불가능! 선언과 할당이 한 번뿐이라구!!
  >
  > object안의 데이터를 추가, 수정 및 삭제는 가능!! 그거슨 재할당이 아니야!

```js
// user.name은 object이므로 재할당이 아니야!
const user = {
    name: 'change',
    phone: 'iphone',
}
user.name = 'ochange'
console.log(user)
```

```js
const user = {
    name: 'change',
    phone: 'iphone',
}
user = {} // 요게 재할당!!! 그래서 오류가 나는겨!
console.log(user)
```

#### 자료형

```js
console.log(typeof '123') // string
console.log(typeof 123) // number
console.log(typeof true) // boolean
console.log(typeof null) // object
console.log(typeof undefined) // undefined
// 나눗셈을 잘못했을 때 많이 나타남(NaN)
console.log(typeof NaN) // number
console.log(typeof {}) // object
console.log(typeof function(){}) // function
// array인 줄 알았으나, object였다.
console.log(typeof []) // object
```

#### 조건 및 반복

> 문법은 파이썬이랑 비슷
>
> `==` : 느슨한 비교
>
> `===`: 엄격한 비교

#### 배열 - object

> 파이썬 처럼 음수 접근이 안 된다!

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray[3]) // 3
```

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.length) // 6
```

##### 원본이 바뀜

- reverse

  > reverse는 원본이 바뀐다.

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.reverse()) // [ 5, 4, 3, 2, 1, 0 ]
console.log(myArray) // [ 5, 4, 3, 2, 1, 0 ]
```

- push

  > push는 맨 뒤에 값을 넣어주고 새로운 배열의 길이를 반환한다.

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.push(6)) // 7
console.log(myArray.push(9)) // 8
console.log(myArray) // [0, 1, 2, 3, 4, 5, 6, 9]
```

- pop

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.pop()) // 5
console.log(myArray) // [ 0, 1, 2, 3, 4 ]
```

- unshift

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.unshift(-1)) // 7
console.log(myArray) // [-1, 0, 1, 2, 3, 4, 5]
```

- shift

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.shift()) // 0
console.log(myArray) // [ 1, 2, 3, 4, 5 ]
```

##### 원본 안 바뀜

- includes

  > 있니 없니? 0이 있니??? 100이 있니?

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.includes(0)) // true
console.log(myArray.includes(100)) // false
console.log(myArray) // [0, 1, 2, 3, 4, 5]
```

- indexOf

  >없으면 -1이 표현됨.

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.indexOf(0)) // 0
console.log(myArray.indexOf(100)) // -1
console.log(myArray) // [0, 1, 2, 3, 4, 5]
```

- join

  > 값들 사이에 '이거'를 넣어줌

```js
const myArray = [0, 1, 2, 3, 4, 5]
console.log(myArray.join('-')) // 0-1-2-3-4-5
console.log(myArray) // [0, 1, 2, 3, 4, 5]
```

#### Object

```js
const endGame = {
    title: '어벤져스: 엔드게임',      
        'my-lovers': [         
            {name: '아이언맨', actor: '로다주'},         
            {name: '헐크', actor: '마크 러팔로'}     
        ] 
    } 
console.log(endGame.title) // 어벤져스: 엔드게임
console.log(endGame['my-lovers'][1].actor) // 마크 러팔로
```

```js
const welcome = function(){
    console.log('책방에 오신걸 환영합니다.')
}
welcome() // 책방에 오신걸 환영합니다.
```

**함수도 변수가 된다!!!!!!!!!**

```js
const welcome = function(){
    console.log('책방에 오신걸 환영합니다.')
}
const comics = {    
    'DC': ['Aquaman', 'SHAZAM'],    
    'Marvel': ['Captain Marvel', 'Avengers'] 
} 
const magazines = null 
const bookShop = {  
    comics,  
    magazines, 
    greeting: welcome,
}
bookShop.greeting() // 책방에 오신걸 환영합니다.
console.log(bookShop)
//{
//  comics: {
//    DC: [ 'Aquaman', 'SHAZAM' ],
//    Marvel: [ 'Captain Marvel', 'Avengers' ]
//  },
//  magazines: null,
//  greeting: [Function: welcome]
//}
```

```js
const phone = {
    number: "010-0000-0000",
    name: 'subin',
    books: ['010-1234-5678', '010-9999-9999',],
    status: true,
    powerOff: function(){
        this.status = false
        console.log(`전원상태 ${this.status}`)
    },
    powerOn: function(){
        this.status = true
        console.log(`전원상태 ${this.status}`)
    },
    numberChange(newNum){
        this.number = newNum
    },
}
phone.powerOff()
console.log(phone.status) // false
phone.powerOn()
console.log(phone.status) // true
phone.numberChange('010-1231-2312')
console.log(phone.number) // 010-1231-2312
```

```js
const phone = {
    arrow: ()=>{
        
    },
    keyword: function(){
        
    }
}
// method 정의 시, this의 의미가 변질되므로 arrow function을 쓰지 않음.
phone.arrow() // 빈 object가 출력되는 이유 : arrow는 최상단을 찾는데 이 node환경에서는 최상단에 브라우저가 존재하지 않으므로
phone.keyword()
```



