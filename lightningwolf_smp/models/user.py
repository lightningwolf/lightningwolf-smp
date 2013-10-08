#!/usr/bin/env python
# coding=utf8
import json
import bcrypt
import hashlib


from lightningwolf_smp.application import db
from flask import url_for
from flask.ext.login import current_user


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)
    salt = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    permissions = db.Column(db.Text, nullable=False)

    # Flask-Login integration
    @staticmethod
    def is_authenticated():
        return True

    @staticmethod
    def is_active():
        return True

    @staticmethod
    def is_anonymous():
        return False

    def get_id(self):
        return self.id

    def is_correct_password(self, password):
        salted = hashlib.sha512(password + self.salt).hexdigest().encode('utf-8')
        hashed = self.password.encode('utf-8')
        return bool(bcrypt.hashpw(salted, hashed) == hashed)

    def roles(self):
        return json.loads(self.permissions)['role']

    def save(self):
        db.session.add(self)
        return db.session.commit()

    def delete(self):
        db.session.delete(self)
        return db.session.commit()

    def get_username(self):
        return self.username

    def get_perm(self):
        roles = self.roles()
        for role in roles:
            if role == 'admin':
                return 'admin'
        return 'user'

    def __repr__(self):
        return '<User %r>' % self.username

    # Flask-LwAdmin integration
    def __unicode__(self):
        return self.username

    def set_edit_button(self, pre):
        pre['url'] = url_for(pre['url'], user_id=self.id)
        return pre

    def set_del_button(self, pre):
        """
        Check for del button in Pager. If current_user is the same as user then Del button is not visable
        :param pre: Flask-LwAdmin action dictionary
        :return: Flask-LwAdmin action dictionary
        """
        pre['url'] = url_for(pre['url'], user_id=self.id)
        if current_user.username == self.username:
            pre['visable'] = False
        return pre