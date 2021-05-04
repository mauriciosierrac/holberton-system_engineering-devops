#!/usr/bin/python3
'''this app consume a URL API for Json Placeholder'''

import json
import requests
from sys import argv

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'

    user = requests.get(url + 'users/{}'.format(int(argv[1]))).json()
    todos = requests.get(url + 'todos?userId={}'.format(int(argv[1]))).json()

    data = []
    for task in todos:
        task_dic = {}
        task_dic['task'] = task.get('title')
        task_dic['completed'] = task.get('completed')
        task_dic['username'] = user.get('username')
        data.append(task_dic)

    json_file = {}
    json_file[argv[1]] = data

    with open('{}.json'.format(argv[1]), 'w') as file:
        json.dump(json_file, file)
