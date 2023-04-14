from django.contrib import admin
from django.urls import path
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),  # Главная страница
    path('books/', views.BookListView.as_view(), name="books"),  # Все книги
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book"),  # Конкретная книга
    path('authors/', views.index, name="authors"),  # Все авторы
]
