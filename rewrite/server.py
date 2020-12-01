#!/usr/bin/python
import json
import logging
from datetime import datetime
import os
import requests
from os import path
from User import User
from Group import Group
from MyUtils import MyUtils
from FSDB import FSDB
from flask import Flask, request, abort, make_response, jsonify

#loggin pre init
log = logging.getLogger("pySCIM")
log.addHandler(logging.StreamHandler())

#global variables
time_stamp = datetime.now().strftime("%y%m%d%H%M%S")
db = None

# -File logging init
def init_logging(log_file_str, verbose_int, file_logging_int):
    """
    init logging

    Parameters:
    log_file_str (STRING): log_file path
    verbose_int (INTEGER): verbosity level
    file_logging_int (int): if this is not 0, turn of file logging
    """
    log.handlers = []

    # create formatter
    formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s', '%m/%d/%Y_%H:%M:%S')

    # if both file and verbosity is missing, set logging "off"
    if len(log_file_str) <= 1 and verbose_int <= 0:
        log.setLevel(logging.CRITICAL)
    elif verbose_int > 0:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.WARNING)

    # create console handler and set level to debug
    # console logger is always created because otherwise logger crashes whole app.
    ch = logging.StreamHandler()
    ch.setLevel(logging.CRITICAL)
    if verbose_int > 0:
        if verbose_int <= 1:
            pass
        elif verbose_int <= 2:
            ch.setLevel(logging.ERROR)
        elif verbose_int <= 3:
            ch.setLevel(logging.WARNING)
        elif verbose_int <= 4:
            ch.setLevel(logging.INFO)
        if verbose_int >= 5:
            ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    log.addHandler(ch)

    if len(log_file_str) > 1 and file_logging_int == 0:
        fh = logging.FileHandler(log_file_str)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        log.addHandler(fh)
    log.info('init(): done, logging starts')


app = Flask(__name__)

users = [
    {
        'id': 1,
        'name': u'Bob',
        'email': u'bob@gmaile.com',
        'phone': '12345689'
    },
    {
        'id': 2,
        'name': u'Ross',
        'email': u'ross@gmaile.com',
        'phone': '789455689'
    }
]

# Get all the users
@app.route('/v2/Users', methods=['GET'])
def get_users():
    return json.dumps({'user': users})

# get users using user id.
@app.route('/v2/Users/<int:user_id>', methods=['GET'])
def get_user_withId(user_id):
    task = [user for user in users if user['id'] == user_id]
    if len(task) == 0:
        abort(404)
    return json.dumps({'user': task[0]})

#----------------------------------------------------


@app.route('/api/users/create_users', methods=['POST'])
def create_task():
    if not request.json or not 'id' in request.json:
        abort(400)
    else:
        url = 'http://localhost:5000/api/users/create_users'
        user = {
            'id': users[-1]['id'] + 1,
            'name': request.json['name'],
            'email': request.json['email'],
            'phone': '123456'
        }
        headers = {"Content-Type: application/json"}
        users.append(user)
        print(users)
        r = requests.post(url, data=json.dumps(user), headers=headers)
        # print(r.content)
        print(r.status_code)
    return ({'user': users}), 201


@app.errorhandler(404)
def not_found(error):
    return make_response(json.dumps({'error': 'Data Not found'}), 404)


@app.route('/api/update_user/<int:user_id>', methods=['PUT'])
def update_task(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    user[0]['name'] = request.json.get('name', user[0]['name'])
    user[0]['email'] = request.json.get('email', user[0]['email'])
    user[0]['phone'] = request.json.get('phone', user[0]['phone'])
    return json.dumps({'user': user[0]})


@app.route('/api/delete_user/<int:user_id>', methods=['DELETE'])
def delete_task(user_id):
    user = [user for user in users if user['id'] == user_id]
    if len(user) == 0:
        abort(404)
    user.remove(user[0])
    return json.dumps({'result': True})


# @app.route('/api/create_users', methods=['POST'])
# def create_user():
#     if not request.json or not 'id' in request.json:
#         abort(400)
#     task = {
#         'id': users[-1]['id'] + 1,
#         'name': request.json['name'],
#         'email': request.json('email'),
#         'phone': request.json('phone#')
#     }
#     print(type(task))
#     users.append(task)
#     print(users)
#     #return json.dumps({task}), 201


if __name__ == '__main__':
    """
    """
    #varibales
    program_folder_str = str(os.environ['HOME']) + '/' + str("pySCIM")
    logs_folder_str = program_folder_str + '/' + str("logs")

    utils = MyUtils(log)

    if not utils.folder_exist(logs_folder_str):
        log.info("hello(): log folder" + str(logs_folder_str) + " Doesn't Exist. Creating new folder")
        os.makedirs(logs_folder_str)

    init_logging(logs_folder_str + '/' + str(time_stamp) + '_log.txt', 6, 0)
    utils.setMyUtilsLogger(log)
    db = FSDB(program_folder_str,log,utils)

    log.critical("main(): starting server")
    app.run(debug=True)
