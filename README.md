
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

Позволяет получить топ-3 товара из базы данных для конкретного пользователя.

Чтобы получить свои топ-3  товаров необходимо пройти аутентификацию.

Введите в поле аутентификации:

username: **test_user**

password: **password**

**/auth/**

Есть возможность зарегистрировать нового пользователя с помощью этого эндпоинта.
Ведите новые username
и password и зарегистрируйте нового пользователя.

Новый пользователь после аутентификации получит другие топ-3 рекомендованных товаров в **/predict/**.
