import os
from sqlalchemy import Column, String, Integer, create_engine
from flask_sqlalchemy import SQLAlchemy
import json

database_name = "casting_agency"
database_path = "postgres://{}:{}@{}/{}".format('stevenelbery','stevenelbery','localhost:5432', database_name)

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app, database_path=database_path):
  app.config["SQLALCHEMY_DATABASE_URI"] = database_path
  app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
  db.app = app
  db.init_app(app)
  db.create_all()

'''
Movie

'''
class Movie(db.Model):
  __tablename__ = 'movies'

  id = Column(Integer, primary_key=True, nullable=False, unique=True)
  title = Column(String(80), nullable=False)
  release_date = Column(Date, nullable=False)


  def __init__(self, title, release_date):
    self.title = title
    self.release_date = release_date

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'title': self.title,
      'release date': self.release_date
    }

'''
Actor

'''
class Actor(db.Model):
  __tablename__ = 'actors'

  id = Column(Integer, primary_key=True)
  name = Column(String(80), nullable=False)
  age = Column(Integer, nullable=False)
  gender = Column(String(20), nullable=False)

  def __init__(self, name, age, gender):
    self.name = name
    self.age = age
    self.gender = gender

  def insert(self):
    db.session.add(self)
    db.session.commit()
  
  def update(self):
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def format(self):
    return {
      'id': self.id,
      'name': self.title,
      'age': self.age,
      'gender': self.gender 
    }
