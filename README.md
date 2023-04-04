### **“Техническое задание на разработку формы вопросов на День директора”**
```
Требования:
- использовать Django
- для оформления темплейтов использовать bootstrap.min.css

Cистема должна состоять из двух форм:
1) Форма подачи вопроса
2) Таблица поданных вопросов

Требования к форме подачи вопросов:
1) Поля ‘Выберите ваш дивизион’ Выпадающий список: Топливный, Машиностроение, ЯОК, Энергетический.
2) Выберите ваше предприятие ‘Выпадающий спиок предприятий, формируется в зависимости от выбранного дивизиона. Названия предприятий любые’.
3) Названия предприятия ‘если в списке не нужного предприятия, то предоставить пользователю возможность заполнить данное поле’.
4) Приложение должно работать в локальной сети без доступа к интернету
```
**Образец:**
<form>

  <label for="list">Выберите ваш дивизион*</label>
  <select id="list" name="list">
    <option value="1">Энергетический</option>
    <option value="2">ЯОК</option>
  </select>

 <label for="list">Выберите ваше предприятие*</label>
  <select id="list" name="list">
    <option value="1">ЯОК 1</option>
    <option value="2">ЯОК 2</option>
  </select>  
  
  <label for="name">Название предприятия*:</label>
  <input type="text" id="name" name="name" required>
  
  <label for="email">Электронная почта, на которую необходимо отправить ответ (можно не корпоративную):</label>
  <input type="email" id="email" name="email" required>

  <label for="message">Задайте ваш вопрос ген. директору Госкорпорации "Росатом" А.Е. Лихачеву:</label>
  <textarea id="message" name="message" rows="5" required></textarea>
  <input type="submit" value="Завершить запрос">
</form>

### **Требования к форме ‘таблица вопросов’**
```
Форма должная состоять из 2х таблиц: вопросы и статистика поданных вопросов
```
<table>
  <thead>
    <tr>
      <td scope="col"></td>
      <td scope="col">Дата время </td>
      <td scope="col">Предприятие</td>
      <td scope="col">Вопрос</td>
	  <td scope="col">E-mail</td>
    </tr>
  </thead>
  <tbody>
    <tr>
         <td>1</td><td></td><td></td><td></td>
      <th></th>     
   
  </tbody>
</table>

<table>
  <thead>
    <tr>
      <td scope="col"></td>
      <td scope="col">Дивизион</td>
      <td scope="col">Предприятие</td>
      <td scope="col">Количество поданных вопросов</td>
    </tr>
  </thead>
  <tbody>
    <tr>
         <td>1</td><td></td><td></td><td></td>
  </tbody>
</table>


### **Стек:**
![python version](https://img.shields.io/badge/Python-3.10-green)  
![django version](https://img.shields.io/badge/Django-4.17-blue)


### **Дополнительные библиотеки:**
[![django-extensions](https://img.shields.io/badge/django--extensions-3.2.1-purple)](https://github.com/django-extensions/django-extensions)  
[![django-smart-selects](https://img.shields.io/badge/django--smart--selects-1.6.0-yellow)](https://github.com/jazzband/django-smart-selects)


### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/artyom-vah/tree_menu.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
``` 
```
source venv/Scripts/activate
```

3. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```

4. В папке с файлом manage.py выполните миграции:
```
python manage.py migrate
```

5. Создайте суперюзера, зайдите в админку
```
python manage.py createsuperuser
```

6. В папке с файлом manage.py запустите сервер, выполнив команду:
```
python manage.py runserver
```

7. Перейдите в админку и добавьте дивизионы, предприятия и вопросы(также можете их добавить через основную форму подачи вопроса http://127.0.0.1:8000/)
```
http://127.0.0.1:8000/admin/
```

**Пример готового проекта**

***Админка:***
![Admin 1](https://raw.githubusercontent.com/artyom-vah/question_list/main/screens/admin_1.jpg)
![Admin 2](https://raw.githubusercontent.com/artyom-vah/question_list/main/screens/admin_2.jpg)
![Admin 3](https://raw.githubusercontent.com/artyom-vah/question_list/main/screens/admin_3.jpg)
***Вывод в браузер:***
![brows_1](https://raw.githubusercontent.com/artyom-vah/question_list/main/screens/brows_1.jpg)
![brows_2](https://raw.githubusercontent.com/artyom-vah/question_list/main/screens/brows_2.jpg)



