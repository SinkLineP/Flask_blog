import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
	DEBUG = False
		TESTING = False
		CSRF_ENABLED = True
		SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
		SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
		MAIL_SERVER = 'smtp.gmail.com'
		MAIL_PORT = 587
		MAIL_USE_TLS = True
		MAIL_USERNAME = os.environ.get('MAIL_USER')
		MAIL_PASSWORD = os.environ.get('MAIL_PASS')


class ProductionConfig(Config):
		DEBUG = False


class StagingConfig(Config):
		DEVELOPMENT = True
		DEBUG = True


class DevelopmentConfig(Config):
		DEVELOPMENT = True
		DEBUG = True


class TestingConfig(Config):
		TESTING = True