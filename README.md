Курсовая 5. Работа с базами данных

В рамках проекта данные о компаниях и вакансиях получаются с сайта hh.ru, 
и загружаются в спроектированные таблицы в БД PostgreSQL.

Запуск проекта
    

    До начала работы программы необходимо создать файл .env в который прописать значение следующих переменных: 
    DB_HOST, DB_PORT, DB_NAME, DB_USER, DB_PASSWORD
    для создания и подключения к БД Postgres.

    Необходимо произвести инсталяцию дополнительных модулей используемых программой в процессе функционирования
    используя следующую команду введенную в терминале:

        $ pip install -r requirements.txt

    Точка входа в проект находиться в файле main.py. Необходимо запустить файл на выполнение, 
    например командой в терминале
        
        $ python3 main.py
    
    Далее выбрать из меню вызываемую функцию, которая выведет в консоль результат.

Класс HeadHunter

Класс HeadHunter, находящийся в файле hh_parser.py, берет данные о работодателях и их вакансиях с сайта hh.ru. Для этого используется публичный API hh.ru и библиотека requests. Имеет следующие методы:

    get_employers():Берет список компаний с публичного API.
    get_vacancies():Берет список вакансий с публичного API.

Класс DBManager

Класс DBManager , находящийся в файле db_manager.pyотвечает за подключение к БД Postgres, создание таблиц и занесения в них информации с сайта hh.ru.использует библиотеку psycopg2 для работы с БД. Имеет следующие методы:
Основные методы

    create_database():Подключается и создает базу данных в Postgres.
    create_tables():Создает таблицы с работодателями и вакансиями.
    insert_data():Создает таблицы с работодателями и вакансиями.

Методы для работы с пользователем

    get_companies_and_vacancies_count(): получает список всех компаний и количество вакансий у каждой компании.
    get_all_vacancies(): получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.
    get_avg_salary(): получает среднюю зарплату по вакансиям.
    get_vacancies_with_higher_salary(): получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.
    get_vacancies_with_keyword(): получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.

Файл queries.sql

Файл queries.sql хранит SQL-запросы для портала