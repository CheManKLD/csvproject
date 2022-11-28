<h1 align="center">CSV item project</h1>
Тестовое задание.

## Технологии:
### Djando, PostgreSQL

## Требования:

<ul>
    <li>Создать проект на Django.</li>
    <li>Создать модель с полями охватывающими столбцы из CSV файла.</li>
    <li>Создать страницу с формой, в которую будет загружаться CSV файл.</li>
    <li>Создать View, которая будет парсить этот файл в созданную модель.</li>
    <li>Вывести на отдельную страницу список выгруженных данных.</li>
</ul>

<h2 align="center">Запуск приложения</h2>

1. Клонировать проект.
2. Создать файл `.env` в корневой папке следующего содержания:

```
DEBUG=1
SECRET_KEY=СЮДА_ВСТАВИТЬ_ВАШ_СЕКРЕТНЫЙ_DJANGO_КЛЮЧ
ALLOWED_HOSTS=localhost,127.0.0.1,[::1]
DATABASE_URL=psql://clients_user:password@localhost:5432/clients_db
```

3. Создать виртуальное окружение, активировать его и установить зависимости командой `pip install -r requirements.txt`.
4. Выполнить миграцию в базу данных командой `python manage.py migrate`.
5. Запустить приложение командой `python manage.py runserver` и следовать документации ниже.

<h2 align="center">Документация</h2>


### Доступные VIEW:
`https://chemanwebapp.pythonanywhere.com/` - Главная страница.

`https://chemanwebapp.pythonanywhere.com/uploadcsv` - Загрузка CSV файла для парсинга и записи данных о товарах 
в базу данных.

`https://chemanwebapp.pythonanywhere.com/items` - Список всех загруженных товаров с пагинацией.