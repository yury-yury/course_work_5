import pandas

from views.abstract_display_results import DisplayResult


class DisplayWithPandas(DisplayResult):
    """
    The DisplayWithPandas class inherits from the abstract DisplayResult class from
    the views.abstract_display_results module. Designed to display the results in a comfortable way using
    the capabilities of the pandas library. Contains settings for using a third-party library, and also overrides
    the methods of the base class.
    """
    pandas.set_option('display.max_row', None)
    pandas.set_option('display.max_columns', None)
    pandas.options.display.expand_frame_repr = False

    def display_companies(self, data: list) -> None:
        """
        The display_companies function overrides the method of the abstract base class.
        Accepts a list of companies as an argument.
        Outputs the results in a convenient form using the tools of the pandas library.
        """
        print(pandas.DataFrame(data, columns=['Название компании', 'Число вакансий']))
        print('-' * 120)

    def display_vacancies(self, data: list) -> None:
        """
        The display_vacancies function overrides the method of the abstract base class.
        Accepts a list of vacancies as an argument.
        Outputs the results in a convenient form using the tools of the pandas library.
        """
        print(pandas.DataFrame(data, columns=['Название компании', 'Название вакансии', 'Зарплата от',
                                              'Зарплата до', 'URL вакансии']))
        print('-' * 120)

    def display_avg_salary(self, data: list) -> None:
        """
        The display_avg_salary function overrides the method of the abstract base class.
        Accepts a list of average salary as an argument.
        Outputs the results in a convenient form using the tools of the pandas library.
        """
        print(pandas.DataFrame(data, columns=['Средняя зарплата']))
        print('-' * 50)
