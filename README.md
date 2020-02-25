# Casting-Agency-App

Motivation


The Casting Agency App is a build for a casting agency in need of a system to manage actors and movies. I've taken the role of the Executive Producer for the agency and have been tasked with effectively managing these resources in a role based access environment.

Getting Started


Installing Dependencies
Python 3.7
Follow instructions in the Python documentation to install the latest release of python for your environement (https://docs.python.org/3/)

Virtual Enviornment


A virtual environment is not requireed but is recommended for this build. Using a virtual environment for your Python builds aids in ensuring that the project's requirements are containerized. See the Python documentation for additional information on configuring virtual environments. (https://docs.python.org/3/)

PIP Dependencies


After confirguring and running your virtual environment, run the following command from your project's root folder in order to install dependencies:

pip install -r requirements.txt

Running this command will install all of the required packages specified in the requirements.txt file.

Core Dependencies


Flask is a a web framework that provides tools, libraries, and technologies used to build modern web applications. Flask is a requirement to handle requests and responses for this project.

JavaScript Object Signing and Encryption (JOSE) is used to encode, decode, and verify JWTS.

Setting Up the Database


First, create a database 'casting_agency' and 'casting_agency_test' for development and test environments. Make sure Postgres is running and restore an existing database for both the 'casting_agency' and 'casting_agency_test' databses using the casting_agency.psql file included in this repository. 

Navigate to the project's root folder and run the folling terminal command:

psql casting_agency < casting_agency.psql

Starting the Server


Navigate to the project's root folder and verify that you're running your virtual environt. 

Each time you open a terminal window related to this project, run the following terminal command:

export FLASK_APP=app.py
export FLASK_ENV=development
flask run --reload

To start the server, execute the following terminal command:

flask run --reload

The --reload flag command will detect file changes and automatically estart the server when changes are found.

Testing


Run the unit tests for the Casting Agency App by running the 'app_test.py' file using the following terminal command: 

python app_test.py

Feel free to test the endpoints using Postman by importing the postman collection file, 'casting_agency_collection.json. Each directory in the collection represents the roles used. 

Usage of the {{url}} variable as the localhost url


The {{remote}} variable is the bridge to the live application.

Auth Resources


Generate access tokens by creating an account using the URL and credentials provided below: 

There are 3 test accounts that are already configured. See the creendtials and UBAC details below: 

username fsndtest@gmail.com
password: P@$$word2020

username fsndtest2@gmail.com
password: P@$$word2020

username: fsndtest@yahoo.com
password:  P@$$word2020
