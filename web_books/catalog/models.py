from django.db import models
from django.contrib.auth.models import User  # Импортируем встроенную модель "Пользователи"

'''  --- ШПАРГАЛКА Варианты параметров доступных в полях моделей: ---
null - Разрешить хранить это поле пустым в БД (True)
blank - Разрешить формам Django игнорировать это поле (True) + Разрешить хранить это поле пустым в БД
default - Значение по умолчанию для поля
primary_key - Первичный ключ для поля (уникальное)
choices - Предоставление выбора из вариантов значение (не используем)
on_delete - Разные сценарии при удалении главной сущности (обязательно для ForeignKey) (CASCADE, PROTECT, SET_NULL, SET_DEFAULT, DO_NOTHING)

help_text - ... При заполнении(добавлении) модели из админки (Подсказка снизу под полем)
verbose_name - ... При заполнении(добавлении) модели из админки (Текстовая метка поля)
'''

# Commands for migrations (моя запись):
# python manage.py makemigrations
# python manage.py migrate
# python manage.py sqlmigrate dj_app 0001


# 1. Модель Жанры (Genre)
# Поля: name(Жанр)
class Genre(models.Model):
    name = models.CharField(max_length=200, help_text="Введите жанр книги", verbose_name="Жанр Книги")

    # При просмотре всей модели из админки (поле которое будет отображаться в таблице)
    def __str__(self):
        return self.name

    # Настройки перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Жанр"  # Название модели в ед.числе
        verbose_name_plural = "Жанры"  # Название модели в мнж.числе
        ordering = ["name"]  # Сортировка по полю


# 2. Модель Авторы (Author)
# Поля: first_name(Имя), last_name(Фамилия), date_of_birth(Дата рождения), date_of_death(Дата смерти)
class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(blank=True, null=True, help_text="Введите дату рождения", verbose_name="Дата рождения")
    date_of_death = models.DateField(blank=True, null=True, help_text="Введите дату смерти", verbose_name="Дата смерти")

    # При просмотре всей модели из админки (поле которое будет отображаться в таблице)
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Автора"  # Название модели в ед. числе
        verbose_name_plural = "Авторы"  # Название модели в мн. числе
        ordering = ["-last_name"]  # Сортировка по полю (если с "-" то в обратном порядке)


# 3. Модель Язык (Language)
# Поля: name(Язык)
class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги")

    # При просмотре всей модели из админки (поле которое будет отображаться в таблице)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Язык"  # Название модели в ед.числе
        verbose_name_plural = "Языки"  # Название модели в мнж.числе
        ordering = ["name"]  # Сортировка по полю (если с "-" то в обратном порядке)


# 4. Модель Книг (Book)
# Поля (связи): author(Автор-ManyToManyField), genre(Жанр-ForeignKey), language(Язык-ForeignKey)
# Поля: title(Название), summary(Описание), isbn(Код книги)
class Book(models.Model):
    author = models.ManyToManyField(Author, help_text="Выберите автора книги", verbose_name="Автор книги")
    genre = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE, help_text="Выберите жанр книги", verbose_name="Жанр книги")
    language = models.ForeignKey(Language, null=True, on_delete=models.CASCADE, help_text="Выберите язык книги", verbose_name="Язык книги")
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    summary = models.TextField(max_length=1000, help_text="Введите описание книги", verbose_name="Описание книги")
    isbn = models.CharField(max_length=200, help_text="Должно содержать 13 символов", verbose_name="ISBN книги")

    # [ВНУТРЕННИЙ МЕТОД] Получить авторов книги (Метод показа [всех авторов] одной из книг)
    def get_authors(self):
        # 1 способ (сделать список из авторов)
        # lst_authors = [a.last_name for a in self.author.all()]
        # 2 способ (сделать список из авторов)
        lst_authors = []
        for author in self.author.all():  # Пробегаю по всем авторам
            lst_authors.append(author.last_name)
        return ", ".join(lst_authors)

    # [ВНУТРЕННИЙ МЕТОД] Возвращающий ссылку на книгу
    def get_absolute_url(self):
        return "/book/{}".format(self.pk)  # self.pk тоже самое что self.id, но id зарезервирован

    # Подписать столбик
    get_authors.short_description = "Авторы"

    # При просмотре всей модели из админки (поле которое будет отображаться в таблице)
    def __str__(self):
        return self.title

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Книгу"  # Название модели в ед.числе
        verbose_name_plural = "Книги"  # Название модели в мнж.числе
        ordering = ["title"]  # Сортировка по полю (если с "-" то в обратном порядке)


# 5. Модель Состояние (Status)
# Поля: name(Состояние)
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги", verbose_name="Статус экземпляра книги")

    # При просмотре всей модели из админки (поле которое будет отображаться в таблице)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Статус"  # Название модели в ед.числе
        verbose_name_plural = "Статусы"  # Название модели в мнж.числе
        ordering = ["name"]  # Сортировка по полю (если с "-" то в обратном порядке)


# 6. Модель Экземпляр (BookInstance)
# Поля (связи): book(Книга-ForeignKey), status(Статус-ForeignKey), borrower(Заказчик-ForeignKey)
# Поля: due_back(Дата возврата), imprint(Издательство), inv_nom(Инвентарный номер)
class BookInstance(models.Model):
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE, help_text="Выберите книгу", verbose_name="Книга")
    status = models.ForeignKey(Status, null=True, on_delete=models.CASCADE, help_text="Изменить состояние экземпляра", verbose_name="Статус экземпляра книги")
    due_back = models.DateField(blank=True, null=True, help_text="Введите конец срока статуса", verbose_name="Дата окончания статуса")
    imprint = models.CharField(max_length=200, help_text="Введите издательство и год выпуска", verbose_name="Издательство")
    inv_nom = models.CharField(max_length=20, null=True, help_text="Введите инвентарный номер экземпляра", verbose_name="Инвентарный номер")
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="Выберите заказчика книги", verbose_name="Заказчик")

    # [ВНУТРЕННИЙ МЕТОД] Проверяющий [не просрочен ли срок возврата] и [не является ли поле пустым]
    pass

    # При просмотре всей модели из админки (поле которое будет отображаться в таблице)
    def __str__(self):
        return "№{} {} ({})".format(self.inv_nom, self.book, self.status)

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Экземпляр"  # Название модели в ед.числе
        verbose_name_plural = "Экземпляры"  # Название модели в мнж.числе
        ordering = ["inv_nom"]  # Сортировка по полю (если с "-" то в обратном порядке)