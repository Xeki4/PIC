from django.shortcuts import render
from .models import Article
from django.http import Http404
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout


def article_list(request):
    posts = Article.objects.all().order_by('-created_date')  # Все статьи, сортировка по дате
    return render(request, 'archive.html', {'posts': posts})

def get_article(request, article_id):
    try:
        post = Article.objects.get(id=article_id)
        return render(request, 'article.html', {"post": post})
    except Article.DoesNotExist:
        raise Http404
    
def create_post(request):
    if not request.user.is_anonymous:
        if request.method == "POST":
            # обработать данные формы, если метод POST
            form = {
                'text': request.POST["text"], 'title': request.POST["title"]
            }
            # в словаре form будет храниться информация, введенная пользователем
            if form["text"] and form["title"]:
                # проверка на уникальность названия
                if Article.objects.filter(title=form["title"]).exists():
                    form['errors'] = u"Статья с таким названием уже существует"
                    return render(request, 'create_post.html', {'form': form})
                
                # если поля заполнены без ошибок и название уникально
                article = Article.objects.create(text=form["text"], title=form["title"], author=request.user)
                return redirect('get_article', article_id=article.id)
            else:
                # если введенные данные некорректны
                form['errors'] = u"Не все поля заполнены"
                return render(request, 'create_post.html', {'form': form})
        else:
            # просто вернуть страницу с формой, если метод GET
            return render(request, 'create_post.html', {})
    else:
        raise Http404

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            error = "Пароли не совпадают"
            return render(request, "register.html", {"error": error})

        if User.objects.filter(username=username).exists():
            error = "Пользователь с таким именем уже существует"
            return render(request, "register.html", {"error": error})

        user = User.objects.create_user(username=username, password=password)
        user.save()

        # Автоматический вход после регистрации
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect("archive")  # замените на нужную страницу

    return render(request, "register.html")

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('archive')  # главная или другая страница
        else:
            error = "Неверные имя пользователя или пароль"
            return render(request, 'login.html', {'error': error})
    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('archive')  # главная страница


