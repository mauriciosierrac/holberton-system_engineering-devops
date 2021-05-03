#!/usr/bin/python3
import requests
from sys import argv
import csv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + 'users/{}'.format(int(argv[1]))).json()
    todos = requests.get(url + 'todos?userId={}'.format(int(argv[1]))).json()

    with open('USER_ID.csv', 'w') as file:
        res = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos:
            res.writerow([task.get('userId'), user.get('username'),
                          task.get('completed'), task.get('title')])
