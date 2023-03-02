"""
This will access the employees.csv file data and store to list format
"""


import csv

from typing import List, Dict
from pprint import pprint


class HandleCSV:
    """ Data accessing class to get data from given path file"""

    filename = "D:\\Python Developer class\\Assignments\\employees.csv"

    @classmethod
    def read_entire_csv(cls) -> List:
        """ Returns a list object containing employees details"""

        data = []
        with open(cls.filename, "r") as foo:
            reader = csv.DictReader(foo)

            for lines in reader:
                data.append(lines)
        return data

    @classmethod
    def read_csv_line_by_line(cls) -> Dict:
        """ Generator function: generate data from given file line by line"""
        with open(cls.filename) as bar:
            yield bar.readline()


if __name__ == "__main__":

    task1 = HandleCSV()
    pprint(task1.read_entire_csv())
