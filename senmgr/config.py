class Default(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/senmgr.db'
    SECRET_KEY = 'dev'

class Test(object):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/senmgr-unittests.db'
    SECRET_KEY = 'test'
    
