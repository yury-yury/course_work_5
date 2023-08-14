from db.db_manager import DBManager
from views.display_with_pandas import DisplayWithPandas


def main() -> None:
    """

    """
    db = DBManager()
    view = DisplayWithPandas()

    while True:
        command = input(
            "1 - Cписок всех компаний и количество вакансий у каждой компании;\n"
            "2 - Cписок всех вакансий с указанием названия компании, названия вакансии и зарплаты и "
                    "ссылки на вакансию;\n"
            "3 - Cредняя зарплата по вакансиям;\n"
            "4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям;\n"
            "5 - Список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”;\n"
            "exit - для выхода.\n")

        if command.lower() == 'exit':
            db.after_working()
            return

        elif command == '1':
            data: list = db.get_companies_and_vacancies_count()
            view.display_companies(data)

        elif command == '2':
            data: list = db.get_all_vacancies()
            view.display_vacancies(data)

        elif command == '3':
            data: list = db.get_avg_salary()
            view.display_avg_salary(data)

        elif command == '4':
            data: list = db.get_vacancies_with_higher_salary()
            view.display_vacancies(data)

        elif command == '5':
            keyword = input('Введите слово: \n')
            data: list = db.get_vacancies_with_keyword(keyword.title())
            view.display_vacancies(data)

        else:
            print(f'{command} не является корректной командой,\nпоробуйте еще раз.')


if __name__ == '__main__':
    main()
