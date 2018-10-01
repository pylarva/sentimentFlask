# !/usr/bin/env python
# -*- coding:utf-8 -*-

from flask_testing import TestCase
from pro_flask import app, db
from pro_flask.models import Users


class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('settings.DevelopmentConfig')
        return app

    def setUp(self):
        db.create_all()
        user = Users(username="admin", email="admin@123.com")
        db.session.add(user)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()