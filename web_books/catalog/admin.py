from django.contrib import admin
from .models import *


# Регистрация и настройка модели Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (При отображении модели)
    list_display = ["__str__", 'date_of_birth', 'date_of_death']


# Регистрация и настройка модели Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (При отображении модели)
    list_display = ["__str__", 'genre', 'language', 'get_authors']
    # Добавление окошка ФИЛЬТРА (По перечисленным полям)
    list_filter = ["genre", "author"]
    # Порядок вывода ПОЛЕЙ (При заполнении модели)
    fieldsets = (("Основное", {"fields": ("title", "author")}),
                 ("Дополнительно", {"fields": ("genre", "language", "summary", "isbn")}))

    # Объявление ВНУТРЕННЕЙ модели "BookInstance" (дополнительная к основной)
    class BookInstanceInline(admin.TabularInline):
        model = BookInstance

    # Дополняем ОСНОВНУЮ "Book" модель дополнительной (ВНУТРЕННЕЙ) "BookInstanceInline"
    inlines = [BookInstanceInline]


# Регистрация и настройка модели BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (При отображении модели)
    list_display = ["__str__", 'borrower', 'due_back']
    # Добавление окошка ФИЛЬТРА (По перечисленным полям)
    list_filter = ["status"]
    # Порядок вывода ПОЛЕЙ (При заполнении модели)
    fieldsets = (("Экземпляр книги", {"fields": ("book", "imprint", "inv_nom")}),
                 ("Статус окончания и заказы", {"fields": ("borrower", "status", "due_back")}))


# Регистрация и настройка модели Genre
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    # Объявление ВНУТРЕННЕЙ модели "Book" (дополнительная к основной)
    class BookInline(admin.TabularInline):
        model = Book

    # Дополняем ОСНОВНУЮ "Book" модель дополнительной (ВНУТРЕННЕЙ) "BookInstanceInline"
    inlines = [BookInline]


# Регистрация и настройка модели Language
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


# Регистрация и настройка модели Status
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass