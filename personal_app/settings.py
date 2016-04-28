# -*- coding: utf-8 -*-
"""Application configuration."""
import os
import datetime


class Config(object):
    """Base configuration."""

    # SECRET_KEY = os.environ.get('PERSONAL_APP_SECRET', "shalalala")  
    # TODO: Change me
    SECRET_KEY = os.urandom(24)
    APP_DIR = os.path.abspath(os.path.dirname(__file__))  # This directory
    PROJECT_ROOT = os.path.abspath(os.path.join(APP_DIR, os.pardir))
    BCRYPT_LOG_ROUNDS = 13
    ASSETS_DEBUG = False
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BLOGGING_URL_PREFIX = "/blog"
    BLOGGING_DISQUS_SITENAME = "test"
    REMEMBER_COOKIE_DURATION = datetime.timedelta(minutes=1)
    PERMANENT_SESSION_LIFETIME = datetime.timedelta(minutes=1)


class ProdConfig(Config):
    """Production configuration."""

    ENV = 'prod'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/example'  # TODO: Change me
    DEBUG_TB_ENABLED = False  # Disable Debug toolbar


class DevConfig(Config):
    """Development configuration."""

    ENV = 'dev'
    DEBUG = True
    DB_NAME = 'dev.db'
    # Put the db file in project root
    DB_PATH = os.path.join(Config.PROJECT_ROOT, DB_NAME)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(DB_PATH)
    DEBUG_TB_ENABLED = True
    ASSETS_DEBUG = True  # Don't bundle/minify static assets
    CACHE_TYPE = 'simple'  # Can be "memcached", "redis", etc.
    BLOG_DB = "dev_blog.db"
    BLOG_PATH = os.path.join(Config.PROJECT_ROOT, BLOG_DB)
    SQLALCHEMY_BINDS = {
    'blog': 'sqlite:///{0}'.format(BLOG_PATH)}


class TestConfig(Config):
    """Test configuration."""

    TESTING = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    BCRYPT_LOG_ROUNDS = 4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
    WTF_CSRF_ENABLED = False  # Allows form testing
