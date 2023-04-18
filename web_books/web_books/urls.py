from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    # Админка и Аккаунты
    path('admin/', admin.site.urls),
    path('accounts/', include("django.contrib.auth.urls")),  # Маршрут для работы с аккаунтами
    path('accounts/registration', views.registration, name="registration"),  # Маршрут для регистрации

    path('', views.index, name="index"),  # Главная страница
    path('books/', views.BookListView.as_view(), name="books"),  # Все книги, по умолчанию (/books/?page=2)
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book"),  # Конкретная книга
    path('authors/', views.AuthorListView.as_view(), name="authors"),  # Все авторы
]
