from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # Импорт всех моделей
from django.views import generic  # Нужно для автоматического чтения модели


# Главная страница
def index(request):
    # Получаем необходимые данные
    num_books = len(Book.objects.all())  # Количество книг
    num_instances = len(BookInstance.objects.all())  # Количество экземпляров
    num_instances_available = len(BookInstance.objects.filter(status__name="На складе"))
    num_authors = len(Author.objects.all())  # Количество авторов
    # Передаем в шаблон
    context = {"num_books": num_books, "num_instances": num_instances, "num_instances_available": num_instances_available, "num_authors": num_authors}
    return render(request, "index.html", context=context)


# Список всех книг (Автоматически генерируется при помощи ListView)
# Шаблон: "templates/catalog/book_list.html" (catalog - имя приложения)
# Переменная (шаблона/ключ): "book_list"
class BookListView(generic.ListView):
    model = Book  # Модель читаемая для шаблона
    # paginate_by = 3  # Сколько объектов будет передано в шаблон


# Конкретная книга (Автоматически генерируется при помощи DetailView)
# Шаблон: "templates/catalog/book_detail.html" (catalog - имя приложения)
# Переменная (шаблона/ключ): "book"
class BookDetailView(generic.DetailView):
    model = Book