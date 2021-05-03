#!/usr/bin/python3
''' this application export to csv file'''

import csv
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + 'users/{}'.format(int(argv[1]))).json()
    todos = requests.get(url + 'todos?userId={}'.format(int(argv[1]))).json()

    with open('{}.csv'.format(argv[1]), 'w') as file:
        res = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos:
            res.writerow([task.get('userId'), user.get('username'),
                          task.get('completed'), task.get('title')])
