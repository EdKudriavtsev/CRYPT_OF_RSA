# CRYPT_OF_RSA

### Цель
Сервис, который позволяет экспериментировать с основным алгоритмом асимметричного шифрования.

### Технологический стек:
- Python 3.8
- Django 4.0+
- SQLite 3.22+

### Инструкция по настройке проекта для запуска:
1. Скачать zip-архив проекта(Вкладка "code")
2. Распаковать архив в папку
3. Запустить файл startapp.bat

### Инструкция по настройке проекта для доработки:
1. Склонировать проект
2. Открыть проект в PyCharm с наcтройками по умолчанию
3. Создать виртуальное окружение (через settings -> project "RSA_CRYPT" -> project interpreter)
4. Открыть терминал в PyCharm, проверить, что виртуальное окружение активировано.
5. Обновить pip:
   ```bash
   pip install --upgrade pip
   ```
6. Установить в виртуальное окружение необходимые пакеты: 
   ```bash
   pip install -r requirements.txt
   ```

7. Синхронизировать структуру базы данных с моделями: 
   ```bash
   python manage.py migrate
   ```

8. Создать суперпользователя
   ```bash
   python manage.py shell -c "from django.contrib.auth import get_user_model; get_user_model().objects.create_superuser('vasya', '1@abc.net', 'promprog')"
   ```

9. Создать конфигурацию запуска в PyCharm (файл `manage.py`, опция `runserver`)
