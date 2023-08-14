CREATE DATABASE {os.environ.get("DB_NAME")}

CREATE TABLE IF NOT EXISTS employers(company_id int PRIMARY KEY, company_name varchar(150))

CREATE TABLE IF NOT EXISTS vacancies(   vacancy_id int PRIMARY KEY,
                                        vacancy_name varchar,
                                        url varchar,
                                        salary_from int,
                                        salary_to int,
                                        company_id int REFERENCES employers(company_id))

INSERT INTO employers (company_id, company_name) VALUES ('{employers_id}', '{company_name}')
                                    ON CONFLICT (company_id) DO NOTHING

INSERT INTO vacancies (vacancy_id, vacancy_name, url, salary_from, salary_to, company_id)
                    VALUES ({vacancy_id}, '{vacancy_name}', '{url}', {salary_from}, {salary_to}, {company_id})
                    ON CONFLICT (vacancy_id) DO NOTHING

SELECT company_name, COUNT(vacancy_name) as count_vacancies
                                FROM vacancies
                                INNER JOIN employers ON vacancies.company_id = employers.company_id
                                GROUP BY company_name

SELECT company_name, vacancy_name, salary_from, salary_to, url FROM vacancies
INNER JOIN employers ON vacancies.company_id = employers.company_id

SELECT AVG(salary_from) as avg_salary
                           FROM vacancies

SELECT company_name, vacancy_name, salary_from, salary_to, url FROM vacancies
                                    INNER JOIN employers ON vacancies.company_id = employers.company_id
                                    WHERE salary_from > (SELECT AVG(salary_from) FROM vacancies)

SELECT company_name, vacancy_name, salary_from, salary_to, url
                        FROM vacancies INNER JOIN employers ON vacancies.company_id = employers.company_id
                        WHERE vacancy_name LIKE '%{keyword}%' OR vacancy_name LIKE '%{keyword.lower()}%'