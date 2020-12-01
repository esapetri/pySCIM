import json
from flask import Flask, request, abort, make_response, jsonify
import requests

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
@app.route('/api/get_users', methods=['GET'])
def get_users():
    return json.dumps({'user': users})


# get users using user id.
@app.route('/api/get_users/<int:user_id>', methods=['GET'])
def get_user_withId(user_id):
    task = [user for user in users if user['id'] == user_id]
    if len(task) == 0:
        abort(404)
    return json.dumps({'user': task[0]})


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
    app.run(debug=True)
