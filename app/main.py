#---------------------------------------------------------------------------------------------------
# Last Edited: 13 Nov'20
# Description: This file contains the main REST API file 
#---------------------------------------------------------------------------------------------------
from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse

##Definging the error messages
errors={
	"Resource_Not_Found":{
		"message": "Resource Not Found",
		"documentation_url": "https://github.com/thadanipaarth/GitTop"
	}
}

app= Flask(__name__)
api=Api(app)
app.config['JSON_SORT_KEYS']=False
## Handling the 404 Not Found error, and returning the custom message
@app.errorhandler(404)
def resource_not_found(Resource):
	return jsonify(errors['Resource_Not_Found'])

resources={

	"api_information": "https://git-top.herokuapp.com/",
	"top_respository":"https://git-top.herokuapp.com/get_top_repositories",
	"top_committies":"https://git-top.herokuapp.com/get_top_committees",
	"top_respositories_and_top_committies":"https://git-top.herokuapp.com/get_top_repo_committees",
	"documentation": "https://github.com/thadanipaarth/GitTop"

}

class api_info(Resource):
	def get(self):
		return jsonify(resources)

# Adding '/' basic Api Information route
api.add_resource(api_info,'/')

# Importing and adding the /get_top_repositories resource
from app.resources.get_top_repositories import get_top_repositories
api.add_resource(get_top_repositories,'/get_top_repositories')

# Importing and adding the /get_top_committees resource
from app.resources.get_top_committees import get_top_committees
api.add_resource(get_top_committees,'/get_top_committees')

# Importing and adding the /get_top_repo_committees resource
from app.resources.get_top_repo_committees import get_top_repo_committees
api.add_resource(get_top_repo_committees,'/get_top_repo_committees')

if __name__ == '__main__':
	app.run(debug=False)

