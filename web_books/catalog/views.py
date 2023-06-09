from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # Импорт всех моделей
from .forms import *  # Импорт всех форм
from django.views import generic  # Нужно для автоматического чтения модели
from django.contrib.auth.views import LoginView


# Главная страница
def index(request):
    # Получаем необходимые данные
    num_books = len(Book.objects.all())  # Количество книг
    num_instances = len(BookInstance.objects.all())  # Количество экземпляров
    num_instances_available = len(BookInstance.objects.filter(status__name="На складе"))
    num_authors = len(Author.objects.all())  # Количество авторов

    # --- Пример работы с сессиями (высчитывает количество посещений этого данного View) ---
    # Количество визитов (Получить значение сессии, если не существует то "0")
    num_visits = request.session.get("num_visits", 0)
    # Запись нового значения (Количество визитов) в сессию
    request.session["num_visits"] = int(num_visits) + 1

    # Передаем в шаблон
    context = {"num_books": num_books, "num_instances": num_instances, "num_visits": num_visits,
               "num_instances_available": num_instances_available, "num_authors": num_authors}
    return render(request, "index.html", context=context)


# Страница регистрации аккаунта
def registration(request):
    if request.method == "GET":
        # Создать форму
        form = Registration()
        # Генерация context
        context = {"form": form}
        # Показываем шаблон
        return render(request, "registration/registration.html", context=context)
    if request.method == "POST":
        # Получаем данные из формы
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        # Записываем данные в БД (нового пользователя)
        User.objects.create_user(username, email, password).save()
        # Генерация context
        context = {"username": username}
        # Показываем шаблон.
        return render(request, "registration/registration.html", context=context)


# Страница Входа в аккаунт (Переназначение)
class LoginUser(LoginView):
    form_class = Login
    template_name = "registration\login.html"



# Список всех книг (Автоматически генерируется при помощи ListView)
# Шаблон: "templates/catalog/book_list.html" (catalog - имя приложения)
# Переменная (шаблона/ключ): "book_list", такое название присваивается по умолчанию
class BookListView(generic.ListView):
    model = Book  # Модель читаемая для шаблона
    paginate_by = 2  # Сколько объектов будет передано в шаблон


# Конкретная книга (Автоматически генерируется при помощи DetailView)
# Шаблон: "templates/catalog/book_detail.html" (catalog - имя приложения)
# Переменная (шаблона/ключ): "book"
class BookDetailView(generic.DetailView):
    model = Book


# Список всех Авторов (Автоматически генерируется при помощи ListView)
# Шаблон: "templates/catalog/author_list.html" (catalog - имя приложения)
# Переменная (шаблона/ключ): "author_list"
class AuthorListView(generic.ListView):
    model = Author  # Модель читаемая для шаблона
    paginate_by = 3  # Сколько объектов будет передано в шаблон