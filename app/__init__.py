# app/__init__.py

from flask import Flask
from flask_restful import Api
from flask_pymongo import PyMongo
from app.config import Config
from moviepy.config import change_settings

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)
mongo = PyMongo(app)

change_settings({"IMAGEMAGICK_BINARY": r"C:\\Program Files\\ImageMagick-7.1.1-Q16-HDRI\\magick.exe"})
from app import routes
