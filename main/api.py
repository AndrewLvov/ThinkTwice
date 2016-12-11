from flask_restless import APIManager

from .models import Site
from app import app, db

manager = APIManager(app, flask_sqlalchemy_db=db)
manager.create_api(Site, methods=['GET', 'POST', 'DELETE'])

