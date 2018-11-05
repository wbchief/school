class Config:
    '''
    配置基类
    '''
    DEBUG = True
    SECRET_KEY = 'pingfan'
    SQLALCHEMY_DATABASE_URI = 'mysql://school:school@localhost/school'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config_map = {
    'testing': DevelopmentConfig,
    'production': ProductionConfig
}