
## Установка

Клонируйте репозиторий:

   ```bash
   git clone https://github.com/UladzimirAliakseichyk/alpha_bank_task.git
```
Перейдите в каталог
alpha_bank_task

```bash 
cd alpha_bank_task

```
Выпоните команду Docker

```bash 
docker-compose build
```
Для запуска приложения выпоните поманду
```bash 
docker-compose up
```


Приложение будет доступно по адресу:

http://127.0.0.1:8000/docs

## Функциональность приложения

**/predict/**

Позволяет получить топ 3 товара из базы данных для конкретного пользователя.

Чтобы получить свои топ 3  товаров необходимо пройти авторизацию.

Введите в поле авторизации:

username: **test_user**

password: **password**

**/auth/**

Есть возможность зарегистрировать нового пользователя с помощью этого эндпоинта.
Выберите username
и password.

Новый пользователь после авторизации получит другие топ 3 в **/predict/**.
