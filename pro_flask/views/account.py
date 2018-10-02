#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template, template_rendered, request_started
from flask import request, Response
from flask import jsonify
# from ..db_helper import SQLHelper
from flask.signals import _signals
from flask import make_response
from ..models import Users
from ..models import Sentiment
import json
from ..models import db
from ..utils.s_client import send_message

account = Blueprint('account', __name__)



# 信号
def print_template_rendered(sender, template, context, **extra):
    print(sender)
    print('Using template: %s with context: %s' % (template.name, context))
    print(request.url)


def print_request_started(sender, **extra):
    print('Request request_started start..')
    print(request.url)


# 注册信号
# template_rendered.connect(print_template_rendered)
# request_started.connect(print_request_started)

from functools import wraps
from flask import current_app


def support_jsonp(f):
    """Wraps JSONified output for JSONP"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            content = str(callback) + '(' + str(f().data, encoding="utf-8") + ')'
            return current_app.response_class(content, mimetype='application/json')
        else:
            return f(*args, **kwargs)
    return decorated_function


@account.route('/index/', methods=['GET', "POST"])
# @support_jsonp
def home():

    if request.method == 'GET':
        ret = Sentiment.query.all()
        # 样本总数
        total_num = Sentiment.query.count()
        # 善言正语数
        good_num = Sentiment.query.filter_by(rank=1).count()
        # 中性宽容
        nature_num = Sentiment.query.filter_by(rank=2).count()
        # 强烈谴责
        intens_num = Sentiment.query.filter_by(rank=3).count()

        sample_info = request.args.get('sample_info')
        if sample_info:
            machine_server = send_message(msg=sample_info, ip='127.0.0.1', port=9997)
            if not machine_server:
                machine_server = '语法分析错误, 请尝试使用其他中文语句重试...'
            print(machine_server)

            resp = jsonify({'machine_server': machine_server})
            resp.headers['Access-Control-Allow-Origin'] = '*'

            return resp

        # response = make_response(jsonify({'status': 200, "data": [i.to_json() for i in ret], 'total_num': total_num,
        #                                  'good_num': good_num, 'nature_num': nature_num, 'intens_num': intens_num}))

        # response = make_response(jsonify({'status': 200}))
        # response.headers['Access-Control-Allow-Origin'] = '*'
        # response.headers['Access-Control-Allow-Methods'] = 'POST'
        # response.headers['Access-Control-Allow-Headers'] = 'x-requested-with,content-type'
        #
        # return Response

        #  测试数据
        total_num = 4000
        good_num = 588
        nature_num = 3118
        intens_num = 294

        resp = jsonify({'status': 200, "data": [i.to_json() for i in ret], 'total_num': total_num,
                        'good_num': good_num, 'nature_num': nature_num, 'intens_num': intens_num})
        resp.headers['Access-Control-Allow-Origin'] = '*'
        return resp


@account.route('/login.html', methods=['GET', "POST"])
def login():
    # obj = SQLHelper()
    # result = obj.fetch_all('select * from mysql.user', [])
    # for item in result:
    #     print(item)
    return render_template('login.html')
