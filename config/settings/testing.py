from grimoirelab.core.config.settings import *  # noqa: F403,F401

import django_rq.queues

from fakeredis import FakeRedis, FakeStrictRedis

LOGGING = {}

SQL_MODE = [
    'NO_ZERO_IN_DATE',
    'NO_ZERO_DATE',
    'ERROR_FOR_DIVISION_BY_ZERO',
    'NO_AUTO_CREATE_USER',
    'NO_ENGINE_SUBSTITUTION',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'NAME': 'grimoirelab_db',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'sql_mode': ','.join(SQL_MODE)
        },
        'TEST': {
            'NAME': 'testgrimoire',
            'CHARSET': 'utf8mb4',
            'COLLATION': 'utf8mb4_unicode_520_ci',
        },
        'HOST': '127.0.0.1',
        'PORT': 3306
    }
}


# Configuration to pretend there is a Redis service
# available. We need to set up the connection before
# RQ Django reads the settings. Also, the connection
# must be the same because in fakeredis connections
# do not share the state. Therefore, we define a
# singleton object to reuse it.
class FakeRedisConn:
    """Singleton FakeRedis connection."""

    def __init__(self):
        self.conn = None

    def __call__(self, _, strict):
        if not self.conn:
            self.conn = FakeStrictRedis() if strict else FakeRedis()
        return self.conn


django_rq.queues.get_redis_connection = FakeRedisConn()
