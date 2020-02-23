import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)

  CORS(app)

  return app

APP = create_app()

#Get movies from casting_agency database

@app.route('/movies')
@requires_auth('get:movies)
def retrieve_movies():
  try:
      movies = Movie.query.all()

      if len(drinks) == 0:
        abort(404)

      return jsonify({
        'success': True,
        'movies': movies
        })
  except:
    abort(422)

#Get actors from casting_agency database

@app.route('/actors')
@requires_auth('get:actors)
def retrieve_actors():
  try:
      actors = Actor.query.all()

      if len(actors) == 0:
        abort(404)

      return jsonify({
        'success': True,
        'actors': actors
        })
  except:
    abort(422)


if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)