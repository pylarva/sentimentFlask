# !/usr/bin/env python
# -*- coding:utf-8 -*-
from . import db
from sqlalchemy import Column,Integer,String
from sqlalchemy_utils import ChoiceType


class Users(db.Model):
    """
    用户表
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return self.username

    def to_json(self):
        json_user = {
            'id': self.id,
            'username': self.username,
            'email': self.email
        }

        return json_user


class Sentiment(db.Model):
    """
    情感分析样本表
    """
    __tablename__ = 'Sentiment'

    Sentiment_choices = (
        ('1', '善言正语'),
        ('2', '中性宽容'),
        ('3', '罪恶谴责'),
        )

    type_choices = (
        ('1', '女装'),
        ('2', '男装'),
        ('3', '童装'),
        ('4', '母婴装'),
        ('5', '其他')
    )

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    customer = db.Column(db.String(80), unique=False, nullable=True)
    start_time = db.Column(db.String(80), unique=False, nullable=True)
    end_time = db.Column(db.String(80), unique=False, nullable=True)
    spend_time = db.Column(db.String(80), unique=False, nullable=True)
    sample = db.Column(db.String(1000), unique=False, nullable=True)
    rank = db.Column(ChoiceType(Sentiment_choices))
    category = db.Column(ChoiceType(type_choices))

    def __repr__(self):
        return self.username

    def to_json(self):
        sentiment_json = {
            'id': self.id,
            'username': self.username,
            'customer': self.customer,
            'start_time': self.start_time,
            'end_time': self.end_time,
            'sample': self.sample,
            'rank': self.rank.value,
            'category': self.category.value,
            'spend_time': self.spend_time,

        }

        return sentiment_json










