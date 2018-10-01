# !/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用flask-sqlAlchemy
# 数据库离线脚本 创建所有数据库表

from pro_flask import db
from pro_flask import app

with app.app_context():
    db.create_all()

