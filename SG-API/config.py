import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '<~m>M)\xc5L\xd3\xc1\x1b\xe2\xff\x07r\x1b\x9a\xdf\x91\xc3'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    #email配置
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'a541203951@163.com'
    MAIL_PASSWORD = 'chengyu911017'
    FLASKY_MAIL_SUBJECT_PREFIX = '[Alan]'
    FLASKY_MAIL_SENDER = 'Alan Chen <a541203951@163.com>'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

config = {
    'default': DevelopmentConfig, 
}
