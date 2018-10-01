#!/usr/bin/env python
# -*- coding:utf-8 -*-
from flask import Blueprint, render_template
from ..models import Users
from ..models import db

# flask-script 自定义flask运行命令插件
# flask-migrate 数据库管理插件

user = Blueprint('user', __name__)


@user.route('/user.html', methods=['GET', "POST"])
def users():
    # 添加用户
    # me = Users(username='xx', email='admin@ss.com')
    # db.session.add(me)
    # db.session.commit()
    # db.session.close()

    # 删除用户
    # db.session.delete(me)
    # db.session.commit()

    # 查询用户
    peter = Users.query.filter_by(username='lichengbing').first()
    print(peter.email)

    return render_template('user.html')