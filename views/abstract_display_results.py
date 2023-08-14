from abc import ABCMeta, abstractmethod


class DisplayResult(metaclass=ABCMeta):
    """
    The DisplayResult class is inherited from the abs module and is an abstract class designed to output results.
    Contains mandatory methods that must be overridden in child classes.
    """
    @abstractmethod
    def display_companies(self, data: list) -> None:
        """
        The display_companies function defines an abstract method of an abstract class designed to output
        the result of a request for a list of companies. Takes a list of data as an argument.
        Must be redefined in the inherited class.
        """
        pass

    @abstractmethod
    def display_vacancies(self, data: list) -> None:
        """
        The display_vacancies function defines an abstract method of an abstract class designed to output
        the result of a vacancies list query. Takes a list of data as an argument.
        Must be redefined in the inherited class.
        """
        pass

    @abstractmethod
    def display_avg_salary(self, data: list) -> None:
        """
        The display_avg_salary function defines an abstract method of an abstract class designed to output
        the result of a request for an average salary for available vacancies. Takes a list of data as an argument.
        Must be redefined in the inherited class.
        """
        pass

