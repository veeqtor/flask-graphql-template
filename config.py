"""Configuration Module"""

# System imports
import os
from pathlib import Path

# Third party library
from dotenv import load_dotenv

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


class Config(object):
	"""
	base app configuration class
	"""

	TESTING = False
	DEBUG = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')


class Development(Config):
	"""
	Development config
	"""

	DEBUG = True
	
	
class Production(Config):
	"""
	Production config
	"""
	
	pass


class Testing(Config):
	"""
	Test config
	"""

	TESTING = True
	SQLALCHEMY_DATABASE_URI = os.getenv('TEST_DATABASE_URI')


app_config = {
	'development': Development,
	'production': Production,
	'testing': Testing
}
