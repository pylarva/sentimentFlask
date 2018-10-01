# !/usr/bin/env python
# -*- coding:utf-8 -*-


class BaseConfig(object):
    # SESSION_TYPE = 'redis'  # session类型为redis
    # SESSION_KEY_PREFIX = 'session:'  # 保存到session中的值的前缀
    # SESSION_PERMANENT = True  # 如果设置为False，则关闭浏览器session就失效。
    # SESSION_USE_SIGNER = False  # 是否对发送到浏览器上 session:cookie值进行加密

    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root@172.16.1.141:3306/flask02?charset=utf8"
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:root@192.168.2.10:3306/flask02?charset=utf8"
    SQLALCHEMY_DATABASE_URI = "sqlite:////opt/git/pro_flask_simple/sqlite.db"
    # SQLALCHEMY_POOL_SIZE = 5
    # SQLALCHEMY_POOL_TIMEOUT = 30
    # SQLALCHEMY_POOL_RECYCLE = -1

    # 追踪对象的修改并且发送信号
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    pass


class TestingConfig(BaseConfig):
    pass