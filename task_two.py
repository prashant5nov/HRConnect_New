"""
----------------------
PROBLEM STATEMENT
----------------------

Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.

"""

from datetime import datetime
from typing import Dict
from pprint import pprint

from my_utils.csvfile import HandleCSV


def get_details() -> Dict:
    """ Returns dict object data containing 'HIRE DATE' and 'NAME' from given csv file"""

    reader = HandleCSV.read_entire_csv()
    getdata = {}
    for data in reader:
        if 30 < int(data.get("DEPARTMENT_ID")) < 110 and int(data.get("SALARY")) > 4200:
            date = datetime.strptime(data['HIRE_DATE'], "%d-%b-%y")
            fdate = date.strftime("%Y-%d-%m")
            getdata.setdefault(fdate, []).extend([data.get('FIRST_NAME') + " " + data.get('LAST_NAME')])
    return getdata


if __name__ == "__main__":

    pprint(get_details())
