import random

import time

from flask_login import UserMixin

from schoolspider import db


class Login(db.Model):
    '''
    用户登录表
    '''
    __tablename__ = 'school'
    username = db.Column(db.String(64), primary_key=True)
    password = db.Column(db.String(64))
    flag = db.Column(db.String(2), index=True)
    counts = db.Column(db.Integer)


    def __repr__(self):
        return '<Login %r>' % self.username

    def insert_data(self, n=100):
        '''

        :return:
        '''
        random.seed(time.time())
        for i in range(n):
            username = random.randrange(100000, 1000000)
            password = random.randrange(100000, 1000000)
            try:
                login = Login(username=username, password=password, flag=1)
                db.session.add(login)
                db.session.commit()
            except Exception as e:
                print(e.args)
                db.session.rollback()

    def insert_admin(self, n=100):
        '''
        插入管理员
        :return:
        '''
        random.seed(time.time())
        for i in range(n):
            username = random.randrange(100000, 1000000)
            password = random.randrange(100000, 1000000)
            try:
                login = Login(username=username, password=password, flag='2', counts=0)
                db.session.add(login)
                db.session.commit()
            except Exception as e:
                print(e.args)
                db.session.rollback()


