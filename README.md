# test_task
Проект: "test_task" - README.md

# Описание проекта

Проект "test_task" это веб-приложение для создания статей и комментарий к статьям. Он разработан с использованием фреймворка Django и включает в себя следующие функциональные возможности:

- Регистрация и аутентификация пользователей.
- Создание статей, редактирование и удаление статей с  проверкой авторства.
- Добавление комментариев к статьям.
- Возможность прикреплять изображения и текстовые файлы к статьям.
- Защита от спама с использованием CAPTCHA.

# Структура проекта

Проект имеет следующую структуру каталогов и файлов:

```
comments/
|-- migrations/
|   |-- __init__.py
|-- templatetags/
|   |-- __init__.py
|   |-- comments_tags.py
|   |-- custom_filters.py
|-- __init__.py
|-- admin.py
|-- apps.py
|-- filters.py
|-- forms.py
|-- models.py
|-- serializers.py
|-- tests.py
|-- urls.py
|-- utils.py
|-- views.py
config/
|-- __init__.py
|-- asgi.py
|-- settings.py
|-- urls.py
|-- wsgi.py
media/
|-- avatars/
|   |-- No_image.png
|-- uploads/
|   |-- img/
|   |-- text/
static/
|-- commands/
|   |-- css/
|   |   |-- style.css
|   |-- img/
|   |   |-- favicon.ico
|   |   |-- logo.jpg
|   |   |-- No_image.png
|   |-- js/
|   |   |-- app.js
|   |   |-- main.js
|   |-- pdf/
|   |   |-- task.pdf
templates/
|-- comments/
|   |-- detail_page.html
|   |-- edit_page.html
|   |-- home.html
|   |-- login_page.html
|   |-- register_page.html
|   |-- task.html
|-- base.html
.gitignore
manage.py
README.md
requirements.txt
```

# Основные компоненты проекта

1. **Модели (models.py)**:
   - `CustomUser`: Расширенная модель пользователя .
   - `Post`: Статьи с заголовком, текстом и возможностью прикреплять изображения или текстовые файлы.
   - `Commentary`: Комментарии к статьям и комментариям.

2. **Формы (forms.py)**:
   - `AuthUserForm`: Форма аутентификации пользователя.
   - `CommentaryForm`: Форма создания комментария.
   - `CommentaryWithCaptchaForm`: Форма наследуется от `CommentaryForm` и добавляет CAPTCHA.
   - `RegisterUserForm`: Форма регистрации новых пользователей.
   - `PostForm`: Форма создания и редактирования статей.

3. **Представления (views.py)**:
   - `HomeListView`: Представление для отображения списка статей на домашней странице.
   - `ProjectLoginView` и `ProjectLogoutView`: Представления для входа и выхода из системы.
   - `PostCreateView`, `PostUpdateView`, `PostDeleteView`: Представления для создания, редактирования и удаления статей.
   - `DetailListView`: Представление для отображения деталей статьи и комментариев к ней.
   - `RegisterUserView`: Представление для регистрации новых пользователей.

4. **URL-паттерны (urls.py)**:
   - Определяют маршруты для обработки запросов и их связь с представлениями.

5. **Статические файлы (static/)**:
   - CSS-файлы, изображения и JavaScript-файлы для стилизации и функциональности веб-приложения.

6. **Медиафайлы (media/)**:
   - Изображения для аватаров пользователей и загружаемые файлы к статьям.

7. **Шаблоны (templates/)**:
   - HTML-шаблоны для отображения страниц приложения.

8. **Миграции базы данных (migrations/)**:
   - Миграции Django для создания и обновления схемы базы данных.

9. **Кастомные теги и фильтры (templatetags/)**:
   - Пользовательские теги и фильтры для шаблонов Django.

# Требования к окружению

- Python 3.10
- Django 4.2.5
- Библиотеки: Pillow, django-captcha, django-filter, djangorestframework (по необходимости)

# Установка и настройка проекта "test_task"
**Шаг 1: Подготовка окружения**

Установка Python: Если у вас еще нет Python, скачайте его с [официального сайта Python](https://www.python.org/downloads/) и выполните установку. При установке убедитесь, что у вас установлена опция "Add Python to PATH".

Создайте деректорию вашего проекта и клонируйте в нее этот репозиторий (https://github.com/soosanin2/test_task_2.git)

Создание виртуальной среды: Рекомендуется создать виртуальное окружение для изоляции зависимостей проекта. Откройте командную строку и выполните следующие команды:


 -  Установите virtualenv глобально с использованием pip: (если у Вас virtualenv еще не установлен)

`pip install virtualenv`

- Убедитесь что вы находитесь в корневой папке "test_task" в ней должен находиться файл "manage.py". Создайте виртуальную среду

`python -m venv venv`

-  Активируйте виртуальную среду

Для Windows

`venv\Scripts\activate`

Для Linux/Mac

`source <ваша_виртуальная_среда>/bin/activate`


После выполнения этих команд ваше виртуальное окружение будет активировано.

**Шаг 2: Установка зависимостей** 

Установка зависимостей проекта: Убедитесь в наличии `requirements.txt`
 и выполните следующую команду:

`pip install -r requirements.txt`

Это установит все необходимые библиотеки и пакеты для вашего проекта.

**Шаг 3: Применение миграций и создание суперпользователя**

Создайте и применение миграций базы данных: Выполните следующие команды, чтобы создать базу данных и применить миграции:

`python manage.py makemigrations`

`python manage.py migrate`

Создание суперпользователя: Для управления админ-панелью Django, создайте суперпользователя, следуя инструкциям:

`python manage.py createsuperuser`

Вы должны будете ввести имя пользователя, адрес электронной почты и пароль для суперпользователя.

**Шаг 4: Запуск сервера:**

Теперь можно запустить сервер разработки Django с помощью команды:


`python manage.py runserver`

После выполнения этой команды, сервер будет доступен по адресу http://localhost:8000 в вашем веб-браузере.

**Шаг 5: Использование проекта**

Регистрация и вход: Перейдите по адресу http://localhost:8000 в вашем браузере. Вы увидите домашнюю страницу проекта. Для доступа к админ-панели перейдите по адресу http://localhost:8000/admin/ и войдите, используя учетные данные суперпользователя, созданные на предыдущем шаге.


# Дополнительная информация
В проекте присутствуют закоментированые части кода, что в дальнейшем поможет адаптировать проект к работе с фреймворками для создания пользовательских интерфейсов.
Проект "test_task" разрабатывается на основе фреймворка Django и использует стандартные инструменты для разработки веб-приложений. 

Создан был в рамках тестового задания, и не является мануалом. Предшествующая версия проекта доступна по ссылке https://github.com/soosanin2/Test_task.git

Используйте данный проект на свой страх и риск, за возможные последствия автор не несет ответственности.
