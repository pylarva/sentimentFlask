#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint
from flask import render_template, template_rendered, request_started
from flask import request, Response
from flask import jsonify
# from ..db_helper import SQLHelper
from flask.signals import _signals
from ..models import Users
from ..models import Sentiment
import json
from ..models import db

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
@support_jsonp
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

        return jsonify({'status': 200, "data": [i.to_json() for i in ret], 'total_num': total_num,
                        'good_num': good_num, 'nature_num': nature_num, 'intens_num': intens_num})


@account.route('/login.html', methods=['GET', "POST"])
def login():
    # obj = SQLHelper()
    # result = obj.fetch_all('select * from mysql.user', [])
    # for item in result:
    #     print(item)
    return render_template('login.html')
