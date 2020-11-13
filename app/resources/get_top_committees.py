#------------------------------------------------------------------------------
# This file contains all the code related to the /get_top_committees resource
#------------------------------------------------------------------------------

from app.utilities.repository import Repository
from flask import jsonify
from flask_restful import reqparse 
from app.main import app, Resource

class get_top_committees(Resource):
	def get(self):

		# Specifying the required arguments and their help message in case the have not been provided
		parser= reqparse.RequestParser()
		parser.add_argument(
			'org',
			type=str,
			required=True,
			help="Bad Request, Organization cannot be blank",
			)
		parser.add_argument(
			'repo',
			type=str,
			required=True,
			help="Bad Request, repository cannot be blank",
			)
		parser.add_argument(
			'committees',
			type=int,
			required=True,
			help="Bad Request, Number of committees cannot be blank",
			)
		
		args_parser=parser.parse_args()
		repository=Repository(args_parser['org'],args_parser['repo'])
		top_committees=repository.get_top_contributors(args_parser['committees'])
		
		return jsonify([top_committees])