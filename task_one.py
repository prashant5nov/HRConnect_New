"""
----------------------
PROBLEM STATEMENT
----------------------

Write a program to get details of employees who's salary is > 9000.

"""
# developer 1


from pprint import pprint
from typing import List

from my_utils.csvfile import HandleCSV



def get_details() -> List:

    reader = HandleCSV.read_entire_csv()

    getdata = []
    for data in reader:
        if int(data.get("SALARY")) > 9000:
            getdata.append({"Name": data.get('FIRST_NAME') + " " + data.get('LAST_NAME'), "Email": data.get('EMAIL'),
                            "Phone Number": (data.get("PHONE_NUMBER").replace(".", ""))})
    return getdata
    # for finaldata in getdata:
    #     return (finaldata)


if __name__ == "__main__":

    pprint(get_details())
