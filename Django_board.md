# Django_board

1. 새 폴더 만들기

   > `03_board` 만들기

2. 새 폴더 들어가기

   > 우 클릭 후 `open with code` 클릭

3. 터미널 창에서 `python -m venv venv`를 입력한다.

4. `F1` 키를 누르고 `select interpreter`를 클릭 후 `venv`를 클릭한다.

5. `vscode`에서 터미널 창을 켜고 `pip install django`를 실행한다.

6. 터미널 창에 있는 휴지통을 누른 후 다시 터미널을 켠다.

7. `django-admin startproject board .`이라는 폴더를 만들어준다.

8. `django-admin startapp todos`라는 폴더를 만들어준다.

9. `.gitignore`파일을 만들고, `gitignore.io`에 들어가 `python`, `windows`, `visual studio code` 등 필요한 것들을 검색하여 `enter`누르고 들어가서 모두 긁어와 파일에 붙여넣기 해준다.

## CRUD

- Create

- Read

- Update

- Delete

  > CRUD를 이용하여 프로젝트를 완성해보자!

## board

### > settings.py

```python
INSTALLED_APPS = [
    'todos',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- `'todos',`를 추가해주었다.

### > urls.py

> urls.py 중에서 상위에 있는 파일이다.

```python
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('todos/', include('todos.urls'))
]
```

- `path('todos/', include('todos.urls'))`에서 `include()`는 `todos.urls`에게 책임을 전가하기 위해 쓴 것이고, 그러기 위해서는 `from django.urls import path, include`처럼 `include`를 가져와야 함.

## todos

### > urls.py

> `urls.py (board)`에게 책임을 넘겨받은 아이!

```python
from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new),
]
```

### > views.py

```python
from django.shortcuts import render

# Create your views here.
def new(request):
    return render(request, 'new.html')

```

### > templates 

#### > base.html

```html
<!DOCTYPE html>
<html lang="en">
  <!-- 이 페이지가 기본값 언어로 en을 가지고 있다. -->
<head>
  <meta charset="UTF-8">
    <!-- 인코딩 설정해주는 곳 -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <!-- viewport는 divice의 width를 viewport라는 이름으로 부르겠다. -->
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <!-- 신경 안 써두 돼용 -->
  <title>Subin</title>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">To do</a>
    <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
      <div class="navbar-nav">
        <a class="nav-item nav-link active" href="/todos/">All<span class="sr-only">(current)</span></a>
        <a class="nav-item nav-link" href="/todos/new/">New</a>
      </div>
    </div>
  </nav>
  <div class="container">
    {% block body %}
  
    {% endblock%}
  </div>  
  <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
  <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js" integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM" crossorigin="anonymous"></script>
</body>
</html>
```

### > templates

#### > new.html

```html
{% extends 'base.html' %}
{% block body %}
  <form action="/todos/create/" class="m-5">
    <!-- 과목평가니깐 잘 봐, mt my mx m -->
    <div class="form-group">
      <label for="title">To do</label>
      <input type="text" class="form-control" id="title" name="title" placeholder="to do">
    </div>
    <div class="form-group">
      <label for="content">Content</label>
      <input type="text" class="form-control" id="content" name="content" placeholder="content">
    </div>
    <div class="form-group">
      <label for="due-date">Due date</label>
      <input type="date" class="form-control" id="due-date" name="due-date" placeholder="due-date">
    </div>  
    <button type="submit" class="btn btn-primary">Submit</button>
  </form>
{% endblock %}
<!-- new는 보여주는거 create는 만드는거 -->
```

### > urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),
]
```

### > models.py

```python
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 50)
    content = models.CharField(max_length = 200)
    due_date = models.DateField()
```

### > migrate시켜주기.

```python
python manage.py makemigrations
python manage.py migrate
```

### > views.py

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date) 아래 터미널 창에 잘 나오는 지 확인용
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date) 위 방법과 같음.
    return render(request, 'create.html')
```

### > templates 

#### > create.html

```html
{% extends 'base.html' %}
{% block body %}
  <h1>글 작성 완료</h1>
{% endblock %}
```

### > urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),
    # read
    path('', views.index),
]
```

### > admin.py

```python
from django.contrib import admin
from .models import Todo
# Register your models here.
admin.site.register(Todo)
```

### > admin 계정 만들기 (id : subin, pw : subin)

```python
python manage.py createsuperuser
```

### > views.py

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date) 아래 터미널 창에 잘 나오는 지 확인용
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date) 위 방법과 같음.
    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)
```

### > templates 

#### > index.html

```html
{% extends 'base.html' %}
{% block body %}
  <table class="table table-dark mt-3">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Title</th>
        <th scope="col">DueDate</th>
        <th scope="col">Buttons</th>
      </tr>
    </thead>
    <tbody>
      {% for todo in todos %}
        <tr>
          <th scope="row">{{todo.id}}</th>
          <td>{{todo.title}}</td>
          <td>{{todo.due_date}}</td>
          <td>
            <a href="/todos/{{todo.id}}/" class="btn btn-primary">more</a>
          </td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

### > urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),
    # read
    path('', views.index),
    path('<int:todo_id>/', views.detail),
]
```

### > views.py

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date) 아래 터미널 창에 잘 나오는 지 확인용
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date) 위 방법과 같음.
    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)
```

### > templates 

#### > detail.html

```html
{% extends 'base.html' %}
{% block body %}
  <div class="jumbotron my-3">
    <h1 class="display-4">{{todo.title}}</h1>
    <p class="lead">{{todo.content}}</p>	
    <hr class="my-4">
    <p>{{todo.due_date}}</p>
    <a class="btn btn-info btn-lg" href="#" role="button">다시쓰기</a>
    <a class="btn btn-danger btn-lg" href="#" role="button">다해땅!</a>
  </div>
{% endblock %}
```

### > urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),
    # read
    path('', views.index),
    path('<int:todo_id>/', views.detail),
    # update
    # delete
    path('<int:todo_id>/delete/', views.delete),
]
```

### > views.py

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date) 아래 터미널 창에 잘 나오는 지 확인용
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date) 위 방법과 같음.
    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return render(request, 'delete.html')
```

### > templates

#### > detail.html

```html
{% extends 'base.html' %}
{% block body %}
  <div class="jumbotron my-3">
    <h1 class="display-4">{{todo.title}}</h1>
    <p class="lead">{{todo.content}}</p>
    <hr class="my-4">
    <p>{{todo.due_date}}</p>
    <a class="btn btn-info btn-lg" href="#" role="button">다시쓰기</a>
    <a class="btn btn-danger btn-lg" href="/todos/{{todo.id}}/delete/" role="button">다해땅!</a>
  </div>
{% endblock %}
```

### > templates

#### > delete.html

```html
{% extends 'base.html' %}
{% block body %}
  <h1>글이 삭제되었습니다.</h1>
{% endblock %}
```

### > templates

#### > index.html

```html
{% extends 'base.html' %}
{% block body %}
  <table class="table table-dark mt-3">
    <thead>
      <tr>
        <th scope="col">#</th>
        <th scope="col">Title</th>
        <th scope="col">DueDate</th>
        <th scope="col">Buttons</th>
      </tr>
    </thead>
    <tbody>
      {% for todo in todos %}
        <tr>
          <th scope="row">{{todo.id}}</th>
          <td>{{todo.title}}</td>
          <td>{{todo.due_date}}</td>
          <td>
            <a href="/todos/{{todo.id}}/" class="btn btn-primary">more</a>
          </td>
        </tr>
      {% empty %}
        <tr>
          <th>#</th>
          <td>할 일이 없엉,,ㅠ</td>
          <td>-</td>
          <td>-</td>
        </tr>
      {% endfor %}
    </tbody>
  </table>
{% endblock %}
```

### > urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),
    # read
    path('', views.index),
    path('<int:todo_id>/', views.detail),
    # update
    path('<int:todo_id>/edit/', views.edit),
    # delete
    path('<int:todo_id>/delete/', views.delete),
]
```

### > views.py

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date) 아래 터미널 창에 잘 나오는 지 확인용
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date) 위 방법과 같음.
    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return render(request, 'delete.html')

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'edit.html', context)
```

### > templates

#### > detail.html

```html
{% extends 'base.html' %}
{% block body %}
  <div class="jumbotron my-3">
    <h1 class="display-4">{{todo.title}}</h1>
    <p class="lead">{{todo.content}}</p>
    <hr class="my-4">
    <p>{{todo.due_date}}</p>
    <a class="btn btn-info btn-lg" href="/todos/{{todo.id}}/edit/" role="button">수정수정</a>
    <a class="btn btn-danger btn-lg" href="/todos/{{todo.id}}/delete/" role="button">다해땅!</a>
  </div>
{% endblock %}
```

### > templates

#### > edit.html

```html
{% extends 'base.html' %}
{% block body %}
  <form action="/todos/{{todo.id}}/update/" class="m-5">
    <!-- 과목평가니깐 잘 봐, mt my mx m -->
    <div class="form-group">
      <label for="title">To do</label>
      <input type="text" class="form-control" id="title" name="title" value="{{todo.title}}">
    </div>
    <div class="form-group">
      <label for="content">Content</label>
      <input type="text" class="form-control" id="content" name="content" placeholder="{{todo.content}}">
    </div>
    <div class="form-group">
      <label for="due-date">Content</label>
      <input type="date" class="form-control" id="due-date" name="due-date" value="{{todo.due_date|date:'Y-m-d'}}">
    </div>  
    <input type="submit" class="btn btn-outline-success" value="수정완료!">
  </form>
{% endblock %}
```

### > urls.py

```python
from django.urls import path
from . import views

urlpatterns = [
    # create
    path('new/', views.new),
    path('create/', views.create),
    # read
    path('', views.index),
    path('<int:todo_id>/', views.detail),
    # update
    path('<int:todo_id>/edit/', views.edit),
    path('<int:todo_id>/update/', views.update),
    # delete
    path('<int:todo_id>/delete/', views.delete),
]
```

### > views.py

```python
from django.shortcuts import render
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date) 아래 터미널 창에 잘 나오는 지 확인용
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date) 위 방법과 같음.
    return render(request, 'create.html')

def index(request):
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return render(request, 'delete.html')

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'edit.html', context)

def update(request, todo_id):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
	
    todo = Todo.objects.get(id=todo_id)
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    return render(request, 'update.html')
```

### > templates

#### > update.html

```html
{% extends 'base.html' %}
{% block body %}
  <h1>수정이 완료되었습니다.</h1>
{% endblock %}
```

### > views.py

```python
from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')
    # print(title, content, due_date) 아래 터미널 창에 잘 나오는 지 확인용
    todo = Todo()
    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()

    # todo = Todo(title=title, content=content, due_date=due_date) 위 방법과 같음.
    # return render(request, 'create.html')
    return redirect('/todos/')

def index(request):
    todos = Todo.objects.order_by('due_date').all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context)

def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'detail.html', context)

def delete(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect('/todos/')

def edit(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    context = {
        'todo': todo,
    }
    return render(request, 'edit.html', context)

def update(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    title = request.GET.get('title')
    content = request.GET.get('content')
    due_date = request.GET.get('due-date')

    todo.title = title
    todo.content = content
    todo.due_date = due_date
    todo.save()
    # return render(request, 'update.html')
    return redirect(f'/todos/{todo_id}/')
    # 중괄호 안에 todo.id를 넣어도 상관없대.
```

- return render(request, 'detail.html')로 가면 안 돼?

  > 안 되는건 아닌데 그러기 위해서는 변수나 이런 것들을 추가해줘야하는 불편함이 있으니까 그냥 redirect를 쓰는게 맘 편해.

- python manage.py makemigrations 번역본 만들어주는 것

  python manage.py migrate 까지 실행해야함.

- models class전까지 commit

  models class하고 commit

  todos/migrations/0001_initial.py는 자동으로 생성되니까 따로 commit은 안하겠음

