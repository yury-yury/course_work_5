import os
from dotenv import load_dotenv
import psycopg2

from hh_parser.hh_parser import HeadHunterParser


load_dotenv()


class DBManager:
    def __init__(self):
        print('Инициализируется база данных')
        try:
            self.create_database()
        except psycopg2.errors.DuplicateDatabase:
            print("БД уже существует")
        else:
            print("БД создана")
        self.connect = psycopg2.connect(host=os.environ.get("DB_HOST"),
                                        database=os.environ.get("DB_NAME"),
                                        user=os.environ.get("DB_USER"),
                                        password=os.environ.get("DB_PASSWORD"))
        self.cursor = self.connect.cursor()
        print('Инициализируются таблицы базы данных')
        self.create_table()
        print('Заполняются данные')
        self.fill_table()


    def create_database(self) -> None:
        """Создает базу данных в PG"""
        conn = psycopg2.connect(host=os.environ.get("DB_HOST"),
                                database="postgres",
                                user=os.environ.get("DB_USER"),
                                password=os.environ.get("DB_PASSWORD"))
        conn.autocommit = True
        cur = conn.cursor()
        cur.execute(f"""CREATE DATABASE {os.environ.get("DB_NAME")}""")
        conn.close()

    def create_table(self) -> None:
        """Создает таблицы с работодателями и вакансиями"""
        self.connect.autocommit = True
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS employers(
                                company_id int PRIMARY KEY,
                                company_name varchar(150) 
                            )""")
        self.cursor.execute(f"""CREATE TABLE IF NOT EXISTS vacancies(
                                vacancy_id int PRIMARY KEY,
                                vacancy_name varchar,
                                url varchar,
                                salary_from int,
                                salary_to int,
                                company_id int REFERENCES employers(company_id)
                            )""")
        print('Таблицы инициализированы.')

    def fill_table(self) -> None:
        """Заносит информацию в таблицы"""
        self.connect.autocommit = True
        hh = HeadHunterParser()

        employers = hh.get_employers()

        for item in employers:
            employers_id = item['id']
            company_name = item['name']
            self.cursor.execute(f"""INSERT INTO employers (company_id, company_name) VALUES ('{employers_id}', '{company_name}') 
                                    ON CONFLICT (company_id) DO NOTHING""")

        vacancies = hh.get_vacancies()
        for vacancy in vacancies:
            vacancy_id = vacancy['id']
            vacancy_name = vacancy['name']
            url = vacancy['alternate_url']
            if vacancy['salary'] is not None:
                salary_from = vacancy['salary']['from'] if vacancy['salary']['from'] is not None else 'NULL'
                salary_to = vacancy['salary']['to'] if vacancy['salary']['to'] is not None else 'NULL'
            else:
                salary_from = 'NULL'
                salary_to = 'NULL'
            company_id = vacancy['employer']['id']
            self.cursor.execute(f"""INSERT INTO vacancies (vacancy_id, vacancy_name, url, salary_from, salary_to, company_id) 
                    VALUES ({vacancy_id}, '{vacancy_name}', '{url}', {salary_from}, {salary_to}, {company_id})
                    ON CONFLICT (vacancy_id) DO NOTHING""")
        print('Данные заполнены.')

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        self.cursor.execute(f"""SELECT company_name, COUNT(vacancy_name) as count_vacancies
                                FROM vacancies
                                INNER JOIN employers ON vacancies.company_id = employers.company_id
                                GROUP BY company_name""")
        return self.cursor.fetchall()

    def get_all_vacancies(self):
        """Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на
            вакансию"""
        self.cursor.execute(f"""SELECT company_name, vacancy_name, salary_from, salary_to, url FROM vacancies
INNER JOIN employers ON vacancies.company_id = employers.company_id""")
        return self.cursor.fetchall()

    def get_avg_salary(self):
        """Получает среднюю зарплату по вакансиям"""
        self.cursor.execute(f"""SELECT AVG(salary_from) as avg_salary
                           FROM vacancies""")
        return self.cursor.fetchall()

    def get_vacancies_with_higher_salary(self):
        """Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям"""
        self.cursor.execute(f"""SELECT company_name, vacancy_name, salary_from, salary_to, url FROM vacancies
                                    INNER JOIN employers ON vacancies.company_id = employers.company_id 
                                    WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)""")
        return self.cursor.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например
            “python”"""
        self.cursor.execute(f"""SELECT company_name, vacancy_name, salary_from, salary_to, url 
                        FROM vacancies INNER JOIN employers ON vacancies.company_id = employers.company_id 
                        WHERE vacancy_name LIKE '%{keyword}%' OR vacancy_name LIKE '%{keyword.lower()}%'""")
        return self.cursor.fetchall()

    def after_working(self):
        self.connect.close()


if __name__ == '__main__':
    db = DBManager()
    # db.get_companies_and_vacancies_count()
    # db.get_all_vacancies()
    # db.get_avg_salary()
    print(db.get_vacancies_with_higher_salary())
    # db.get_vacancies_with_keyword('разработчик')
