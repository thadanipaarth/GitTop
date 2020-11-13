#------------------------------------------------------------------------------
# This file contains all the code related to the /get_top_repo_committees resource
#------------------------------------------------------------------------------

from app.utilities.repository import Repository
from app.utilities.organization import Organization
from flask import jsonify
from flask_restful import reqparse 
from app.main import app, Resource
from app.utilities.parameter_util import *

class get_top_repo_committees(Resource):
	def get(self):

		# Specifying the required arguments and their help message in case the have not been provided
		parser= reqparse.RequestParser()
		parser.add_argument(
			'parameter',
			type=str,
			required=True,
			help="Bad Request, Parameter cannot be blank"
		)
		parser.add_argument(
			'org',
			type=str,
			required=True,
			help="Bad Request, Organization cannot be blank",
			)
		parser.add_argument(
			'repo',
			type=int,
			required=True,
			help="Bad Request, Number of repository cannot be blank",
			)
		parser.add_argument(
			'committees',
			type=int,
			required=True,
			help="Bad Request, Number of committees cannot be blank",
			)
		
		args_parser=parser.parse_args()
		valid=check_valid_parameter(args_parser['parameter'])
		if valid!=None:
			return jsonify(valid)

		organization=Organization(args_parser['org'],args_parser['parameter'])
		top_repositries=organization.get_top_repositories(args_parser['repo'])
		
		for each in top_repositries['data']:
			repository=Repository(args_parser['org'],each['name'])
			top_committees=repository.get_top_contributors(args_parser['committees'])
			each['top_committees']=top_committees
		return jsonify(top_repositries)