SQLALCHEMY_DATABASE_URI = \
    "postgresql://postgres:postgres@db/postgres"

# SQLALCHEMY_TRACK_MODIFICATIONS = True


try:
    from local_settings import *
except ImportError:
    pass