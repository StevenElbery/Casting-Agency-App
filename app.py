import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db_drop_and_create_all, setup_db, Movie, Actor
from auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)

  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers','Content-Type,Authorization,true')
    response.headers.add('Access-Control-Allow-Methods','GET,POST,PATCH,PUT,DELETE,OPTIONS')
  
    return response

#db_drop_and_create_all()

#Movie Enpoints

#Get movies from casting_agency database

  @app.route('/api/movies')
  @requires_auth('get:movies')
  def retrieve_movies(jwt):
    
    try:
      movies = Movie.query.all()

      if len(movies) == 0:
        abort(404)

      return jsonify({
        'success': True,
        'movies': movies
        }), 200
        
    except:
      abort(422)

#Get actors from casting_agency database

  @app.route('/actors')
  @requires_auth('get:actors')
  def retrieve_actors(jwt):
    try:
      actors = Actor.query.all()

      if len(actors) == 0:
        abort(404)

      return jsonify({
        'success': True,
        'actors': actors
        }), 200
        
    except:
      abort(422)

#Delete movies from casting_agency database

  @app.route('/movies/<int:movie_id>', methods=['DELETE'])
  @requires_auth('delete:movies')
  def delete_movie(jwt,movie_id):
    try:
      movie = Movie.query.filter(Movie.id == movie_id).one_or_none()

      if movie is None:
        abort(404)

      movie.delete()

      return jsonify({
        'success': True,
        'delete': movie_id
      }), 200

    except:
      abort(422)

#Delete actors from casting_agency database

  @app.route('/actors/<int:actor_id>', methods=['DELETE'])
  @requires_auth('delete:actors')
  def delete_actor(jwt,actor_id):
    try:
      actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

      if actor is None:
        abort(404)

      actor.delete()

      return jsonify({
        'success': True,
        'delete': actor_id
      }), 200

    except:
      abort(422)

# POST /movies - create a new row in the movies table

  @app.route('/movies')
  @requires_auth('post:movies')
  def create_movie(jwt):
    body = request.get_json()
    
    new_title = body.get('title', None)
    new_release_date = body.get('release_date', None)
    search = body.get('search', None)
  
    try:
      movie = Movie(title=new_title, release_date=new_release_date)
      movie.insert()
      
      return jsonify({
        'success': True,
        'movies': movie
        }), 200
    except:
      abort(422)

# POST /actors - create a new row in the actors table

  @app.route('/actors')
  @requires_auth('post:actors')
  def create_actor(jwt):
    body = request.get_json()
    
    new_name = body.get('name', None)
    new_age = body.get('age', None)
    new_gender = body.get('gender', None)
    search = body.get('search', None)
  
    try:
      actor = Actor(name=new_name, age=new_age, gender=new_gender)
      movie.insert()
      
      return jsonify({
        'success': True,
        'actors': actor
        }), 200
    except:
      abort(422)

# PATCH /movies - update a row in the movies table

  @app.route('/movies/<int:movie_id>', methods=['PATCH'])
  @requires_auth('patch:movies')
  def update_movie(jwt,movie_id):
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    body = request.get_json()
    
    if movie is None:
        abort(404)

    title = body.get('title')
    release_date = body.get('release_date')

    try:
      movie.title = title
      movie.release_date = release_date

      movie.update()

      return jsonify({
        'success': True,
        'movies': movie
      }), 200
      
    except Exception:
      abort(400)

# PATCH /actors - update a row in the actors table

  @app.route('/actors/<int:actor_id>', methods=['PATCH'])
  @requires_auth('patch:actors')
  def update_actor(jwt,actor_id):
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()

    body = request.get_json()

    if actor is None:
      abort(404)
   
    name = body.get('name')
    age = body.get('age')
    gender = body.get('name')

    try:
      actor.name = name
      actor.age = age
      actor.gender = gender

      actor.update()

      return jsonify({
        'success': True,
        'actors': actor
      }), 200
      
    except:
      abort(400)

# Error Handlers - 400, 404, 422

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      'success': False,
      'error': 404,
      'message': "Not Found"
      }), 404
  
  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
      'success': False,
      'error': 422,
      'message': "Unable to process the contained instructions"
      }), 422

  @app.errorhandler(400)
  def syntaxError(error):
    return jsonify({
      'success': False,
      'error': 400,
      'message': "Syntax error detected"
      }), 400  
      
# Authenticatiom Error Handler

  @app.errorhandler(AuthError)
  def authError(error, status_code):
    return jsonify({
      'success': False,
      'error': error,
      'status_code': status_code
    })

  return app

app = create_app()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)