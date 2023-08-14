from pprint import pprint
from typing import List
import requests


class HeadHunterParser:
    """

    """
    base_url: str = 'https://api.hh.ru/'

    def get_employers(self) -> List[dict]:
        response = requests.get(self.base_url + 'employers',
                                {'per_page': 10, 'area': 113, 'only_with_vacancies': True}).json()
        return response['items']

    def get_vacancies(self) -> List[dict]:
        vacancies = []
        for vac_id in [int(elem['id']) for elem in self.get_employers()]:
            response = requests.get(self.base_url + 'vacancies', {'employer_id': vac_id}).json()['items']
            vacancies.extend(response)
        return vacancies


if __name__ == '__main__':
    hh_parser = HeadHunterParser()
    pprint(hh_parser.get_employers())
    pprint(hh_parser.get_vacancies())