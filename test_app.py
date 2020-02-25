import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from app import create_app
from models import setup_db, Movie, Actor

load_dotenv()


class FSNDCapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = os.getenv('TEST_DATABASE_URL')
        setup_db(self.app, self.database_path)

        self.new_movie = {
            "title": "My Favorite Movie",
            "release_date": "31-Aug-1988",
        }

        self.new_actor = {
            "name": "Jack Black,
            "gender": "male",
            "age": "55"
        }

        self.casting_assistant_headers = {
            "Content-Type": "application/json",
            "Authorization": os.getenv('CASTING_ASSISTANT')
        }

        self.casting_director_headers = {
            "Content-Type": "application/json",
            "Authorization":  os.getenv('CASTING_DIRECTOR')
        }

        self.exec_producer_headers = {
            "Content-Type": "application/json",
            "Authorization":  os.getenv('EXECUTIVE_PRODUCER')
        }

        # binds the app to the current context (INSTANTIATION)
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create/remove all tables

    def tearDown(self):
        #Run after test
        pass

    # Handle GET requests
    def test_retrieve_movies(self):
        res = self.client().get('/movies', headers=self.exec_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_retrieve_actors(self):
        res = self.client().get('/actors', headers=self.exec_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #  POST requests
    def test_create_movie(self):
        res = self.client().post(
            '/movies', headers=self.exec_producer_headers, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_create_actor(self):
        res = self.client().post(
            '/actors', headers=self.exec_producer_headers, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    #  PATCH requests.
    def test_update_a_movie(self):
        movie = {
            "title": "Better than ever",
            "release_date": "19-Dec-2040",
        }
        res = self.client().patch('/movies/1',
                                  headers=self.exec_producer_headers, json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_update_an_actor(self):
        actor = {
            "name": "Rick James",
            "gender": "male",
            "age": "63"
        }
        res = self.client().patch('/actors/1',
                                  headers=self.exec_producer_headers, json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # DELETE requests.
    def test_delete_movie(self):
        res = self.client().delete('/movies/2',
                                   headers=self.exec_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_delete_actor(self):
        res = self.client().delete('/actors/2',
                                   headers=self.exec_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # ERROR HANDLERS

    # ERRORS ON GET endpoints

    def test_fail_retrieve_movies(self):
        res = self.client().get('/movies')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client")
        self.assertEqual(data['success'], False)

    def test_fail_retrieve_actors(self):
        res = self.client().get('/actors')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client")
        self.assertEqual(data['success'], False)

    #  ERRORS ON POST enpoints
    def test_fail_create_movie(self):
        res = self.client().post('/movies', json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client")
        self.assertEqual(data['success'], False)

    def test_fail_create_actor(self):
        res = self.client().post('/actors', json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client")
        self.assertEqual(data['success'], False)

    #  ERRORS ON PATCH enpoints.
    def test_fail_movie_update(self):
        movie = {
            "title": "Believe in Yourself,
            "release_date": "20-Apr-2030",
        }
        res = self.client().patch('/movies/1', json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client")
        self.assertEqual(data['success'], False)

    def test_fail_actor_update(self):
        actor = {
            "name": "Judy Blair",
            "gender": "female",
            "age": "21"
        }
        res = self.client().patch('/actors/1', json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client")
        self.assertEqual(data['success'], False)

    #  ERRORS ON DELETE enpoints.
    def test_fail_delete_movie(self):
        res = self.client().delete('/movies/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client")
        self.assertEqual(data['success'], False)

    def test_fail_remove_an_actor(self):
        res = self.client().delete('/actors/2')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['message'], "Unauthorized client error")
        self.assertEqual(data['success'], False)

    # ROLE BASED ACCESS CONTROL TESTING (ERROR HANDLERS)

    # CASTING ASSISTANT ROLE GET requests

    def test_retrieve_movies(self):
        res = self.client().get('/movies',
                                headers=self.casting_assistant_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_retrieve_actors(self):
        res = self.client().get('/actors',
                                headers=self.casting_assistant_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    # EXECUTIVE PRODUCER ROLE DELETE requests.

    def test_delete_movie(self):
        res = self.client().delete('/movies/190000',
                                   headers=self.exec_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    def test_delete_actor(self):
        res = self.client().delete('/actors/3000',
                                   headers=self.exec_producer_headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)


    # CASTING DIRECTOR ROLE PATCH requests
    def test_update_a_movie(self):
        movie = {
            "title": "This Movie was NEVER Made",
            "release_date": "NA-NA-NANA",
        }
        res = self.client().patch('/movies/44039',
                                  headers=self.casting_director_headers, json=movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)

    def test_update_an_actor(self):
        actor = {
            "name": "Not Found",
            "gender": "unsure",
            "age": "31"
        }
        res = self.client().patch('/actors/100',
                                  headers=self.casting_director_headers, json=actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "resource not found")
        self.assertEqual(data['success'], False)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
