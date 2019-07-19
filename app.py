"""Application factory"""

# Third party library
from flask import Flask, jsonify
from flask_graphql import GraphQLView
from flask_cors import CORS

# local imports
from config import app_config
from database import db, migrate
from src.schemas import schema


def create_app(env):
	"""
	Flask application factory.
	"""

	# initialization the application
	app = Flask(__name__)
	app.url_map.strict_slashes = False
	app.config.from_object(app_config[env])
	
	# cross origin initialization
	CORS(app)

	# binding the database and migrate to the flask app instance
	db.init_app(app)
	migrate.init_app(app, db)

	# Models
	import database.models

	# Views
	app.add_url_rule(
			'/graphql',
			view_func=GraphQLView.as_view(
					'graphql',
					schema=schema,
					graphiql=True  # for having the GraphiQL interface
			)
	)
	
	# root route
	@app.route('/', methods=['GET'])
	def index():
		"""
		Index route for the API
		"""
		
		return jsonify(
				status='Healthy',
		)

	# return because of test.
	return app
