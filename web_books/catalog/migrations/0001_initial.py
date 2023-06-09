# Generated by Django 4.1.5 on 2023-04-10 13:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(help_text='Введите имя автора', max_length=100, verbose_name='Имя автора')),
                ('last_name', models.CharField(help_text='Введите фамилию автора', max_length=100, verbose_name='Фамилия автора')),
                ('date_of_birth', models.DateField(blank=True, help_text='Введите дату рождения', null=True, verbose_name='Дата рождения')),
                ('date_of_death', models.DateField(blank=True, help_text='Введите дату смерти', null=True, verbose_name='Дата смерти')),
            ],
            options={
                'verbose_name': 'Автора',
                'verbose_name_plural': 'Авторы',
                'ordering': ['-last_name'],
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Название книги')),
                ('summary', models.TextField(help_text='Введите описание книги', max_length=1000, verbose_name='Описание книги')),
                ('isbn', models.CharField(help_text='Должно содержать 13 символов', max_length=200, verbose_name='ISBN книги')),
                ('author', models.ManyToManyField(help_text='Выберите автора книги', to='catalog.author', verbose_name='Автор книги')),
            ],
            options={
                'verbose_name': 'Книгу',
                'verbose_name_plural': 'Книги',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите жанр книги', max_length=200, verbose_name='Жанр Книги')),
            ],
            options={
                'verbose_name': 'Жанр',
                'verbose_name_plural': 'Жанры',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите статус экземпляра книги', max_length=20, verbose_name='Статус экземпляра книги')),
            ],
            options={
                'verbose_name': 'Статус',
                'verbose_name_plural': 'Статусы',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='BookInstance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('due_back', models.DateField(blank=True, help_text='Введите конец срока статуса', null=True, verbose_name='Дата окончания статуса')),
                ('imprint', models.CharField(help_text='Введите издательство и год выпуска', max_length=200, verbose_name='Издательство')),
                ('inv_nom', models.CharField(help_text='Введите инвентарный номер экземпляра', max_length=20, null=True, verbose_name='Инвентарный номер')),
                ('book', models.ForeignKey(help_text='Выберите книгу', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Книга')),
                ('borrower', models.ForeignKey(blank=True, help_text='Выберите заказчика книги', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Заказчик')),
                ('status', models.ForeignKey(help_text='Изменить состояние экземпляра', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.status', verbose_name='Статус экземпляра книги')),
            ],
            options={
                'verbose_name': 'Экземпляр',
                'verbose_name_plural': 'Экземпляры',
                'ordering': ['inv_nom'],
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text='Выберите жанр книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
        migrations.AddField(
            model_name='book',
            name='language',
            field=models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Язык книги'),
        ),
    ]
