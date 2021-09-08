import os
basedir = os.path.abspath(os.path.dirname(__file__))
postgres_local_base = 'sqlite:///'
database_name = 'diagnostic'


class BaseConfig:
    """Base configuration."""
    SECRET_KEY = os.getenv('SECRET_KEY', 'diagnostic_secret')
    DEBUG = False
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name


class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    BCRYPT_LOG_ROUNDS = 4
    SQLALCHEMY_DATABASE_URI = postgres_local_base + database_name + '_test.db'
    PRESERVE_CONTEXT_ON_EXCEPTION = False


class ProductionConfig(BaseConfig):
    """Production configuration."""
    SECRET_KEY = 'diagnostic_secret'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://uixnrsvuvyrtdd:ffdc5d906356d59fb30af152687607d271c78e15ab8d5fb62759b88f4350587a@ec2-44-198-80-194.compute-1.amazonaws.com:5432/da0ps55fpsjq12'
