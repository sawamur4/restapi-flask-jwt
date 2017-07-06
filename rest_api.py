# -*- coding: utf-8 -*-
import requests
import json

from flask import Flask, jsonify, request
from flask_restful import Api
from flask_jwt import JWT, jwt_required, current_identity
from user import UserModel

from security import authenticate, identity

from facebookads.api import FacebookAdsApi
from facebookads.objects import AdUser


__author__ = 'junior'

my_app_id = '438875109829513'
my_app_secret = 'd65cc258aeb9a25b1178bd933e0e4cf7'
my_access_token = 'EAAGPJ5MFq4kBAB1tvZBgZBQmyuYs1rJO4Q8vFCtiFV8TxcoREg82FlRNVMtV9bNgkiVpNfxwGYf2LQB6uatc3n4NWtmyG5ENQCgY3uaWV7KgSshbSJHjIrSdk5mDFZAfd4BvqeviBHFSnfJqiAkaDdviZBKZAvqBZBNF5FNmlwbV1ZB1B7pdo4VZC8bZA7JUPIk4aZCcEZAJ9QCkYniZARX301py'
FacebookAdsApi.init(my_app_id, my_app_secret, my_access_token, api_version="v2.9")

app = Flask(__name__)
app.config['MONGOALCHEMY_DATABASE'] = 'login'
app.config['MONGOALCHEMY_SERVER_AUTH'] = False
app.secret_key = 'ver'
api = Api(app)


jwt = JWT(app, authenticate, identity)  # /auth


@app.route('/login', methods=['POST'])
def login():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password :
        user = UserModel.find_by_username(username)
        if user:
            # auth_url = "http://127.0.0.1:5000/auth"
            # data_body = {"username": username, "password": password}
            # # headers = {'Content-Type': 'application/json'}
            # r = requests.post(auth_url, json=data_body)
            # # print response.status_code
            # # return response.json()
            # return json.dumps(r.json(), indent=4)
            return "Login Success"
        else:
            return "Error Username Not found in DB"
    else:
        return "Error Param"


@app.route('/daftar')
def daftar():
    username = request.args.get("username")
    password = request.args.get("password")
    if username and password :
        user = UserModel.find_by_username(username)
        if user:
            return "Error Username : {} Already Exist".format(username)
        else:
            users = UserModel(id=username ,username=username, password=password)
            users.save_to_db()

        return "Success Insert Username : {}".format(username)
    else:
        return "Error Param"


@app.route('/user')
@jwt_required()
def user():
    me = AdUser(fbid='me')
    my_account = me.get_ad_account()
    # print
    return "{}".format(my_account)


if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)