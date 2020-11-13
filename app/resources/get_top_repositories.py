#------------------------------------------------------------------------------
# This file contains all the code related to the /get_top_repositories resource
#------------------------------------------------------------------------------

from app.resources.organization import Organization
from flask import jsonify
from flask_restful import reqparse 
from app.main import app, Resource

available_order=['fork']
error={
	'Order_Not_Found':{
		"message":"Bad Request, Order not found",
		"documentation":"https://github.com/thadanipaarth/GitTop.git"
	}
}
class get_top_repositories(Resource):
	def post(self):

		# Specifying the required arguments and their help message in case the have not been provided
		parser= reqparse.RequestParser()
		parser.add_argument(
			'parameter',
			type=str,
			required=True,
			help="Bad Request, Organization cannot be blank"
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
			help="Bad Request, Number of repositories cannot be blank",
			)
		
		args_parser=parser.parse_args()
		
		if parameter not in available_order:
			return jsonify(error['Order_Not_Found'])

		organization=Organization(args_parser['org'])

		if parameter == 'fork':
			top_repositries=organization.get_top_repositories_fork(args_parser['repo'])
		
		return jsonify(top_repositries)