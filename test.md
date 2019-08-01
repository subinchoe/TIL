### 1. built-in-function

abs() : 절대값

list() : 리스트

map() : 뭐지

### 2. 시퀀스 자료형 특징

list같은 자료형 타입

데이터가 연속적으로 나열

in연산자를 통해 특정 값이 있는 지 알 수 있음

정렬된 것이 아님.

### 3. [-2] [-2]

james의 e

### 4. population증가

p3를 출력했으므로 3

### 5. 오류 발생

my_complex = 3+4j

my_complex.real()

왜?

### 6. 출력

def func(c,b,a):

​	return(a*b+c)

print(func(2,5,4)) => 22 

### 7. dict라고 써야한댕...

a = {}

type(a)

<class 'dict'>.....

### 8. 함수 설명

return이 없으면 none을 선언하기 때문에 

같은 이름의 함수가 두 개면 나중께 선언됨

### 9. numbers = 

[0,0,0,0,0]

[0]*5

[]; numbers.append(0*5) 는 틀림

[0 for i in range(5)]

### 10. result = 4+true+false+5 = 10

### 11. s = 'hello my name is ssafy'

s가 2번 출력되는 거!

### 12. dict알아보기

d1 = {'d':dict()} =>  {'d' : {}}

d2 = dict(d={}) =>  {'d' : {}}

id는 서로 다름

d1이랑 d2는 같음(True임)

len(d1)=1, len(d2)=1

### 13. fruits={'apple':'사과', 'banana':'바나나'}

b=fruits.get('cherry')

b는 None이다.

에러가 나지 않는다구!~!!!!!!!!

### 14. func의 값은 무얼까?

def func(c="5", *args):

​	a,c,b = args

​	return a+b+c

print(func('3','4','1','2'))



나는 314라고 생각했어

근데 c에 3이 먼저 들어가고 나머지 4,1,2가 args에 들어가는거야

def fund(c='3', ('4','1','2'))

c='3'

a,c,b = (4,1,2)

그래서 421............

### 15. class문제다!!!

name = 'hong'

class Person:

​	name='choi'

​	def greeting(self):

​		print(name)

p1=Person()

p1.name = 'kim'

p1.greeting()



정답은 hong 이라고??????????????????????????????????

### 16.  my_int =3 정수형인지 확인해보자

isinstance(int, my_int) : 얘가 왼쪽에 있는 게 오른쪽의 인스턴스니? >>순서가 잘못됨

my_int ==3: 이건 값을 확인하는거라서,,

isinstance(my_int, 3) : 값을 비교하기 때문에 아님

type(my_int)==int 정답

### 17. 또 클래스야

class Person:

def __ init  __(self,name,age):

self.name=name



p3 = Person(age=3, name='kang')이 정답

### 18. word = 'python'

indexing = word[3:8]

print(indexing)



정답은 hon

### 19. my_sum, result변수에 들어있는 값 구하기

def my_sum(a,b):

​	c = a+b

​	print(c)

result = my_sum (5,8)

정답은 None

### 20. idx%2일 때

홀수에 있는 것만 대문자로 띄어쓰기도 포함

string = 'I am hungry'

### 21.딕셔너리

d = {'a':1, 'b':2}

a1 = d.update(c=3)

a2 = a1

와우,,, a1은 아무런 데이터도 없어, len(a1)=2.. none이라구,,

a1과 a2가 같은 딕셔너리? 하... 값이 아예 없어

코드 에러 발생 안 해

보기 중에 답이 없다 가 정답

### 22. 와 숫자더하기다

def func(a=1,b=2,c=3,*args, **kwargs)

def func(9,4,2,(3,1,7),(d:3,e:6))

a+b+c+d+e

print(func(9,4,2,3,1,7,d=3,e=6))

80이래..

### 23. fib호출하기

1은 3번, 0은 2번 출력됨

### 24. scope!!

답은 11이래.

### 25. 































