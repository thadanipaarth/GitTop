from flask import Flask,jsonify
from flask_restful import Resource, Api, reqparse

errors={

	"Request_Not_Found":{
		"message": "Not Found",
		"documentation_url": "https://github.com/thadanipaarth/GitTop.git"
	}

}

app= Flask(__name__)
api=Api(app, catch_all_404s = True, errors=errors)

resources={
	"api_information": "https://git-top.herokuapp.com/",
	"top_respository":"https://git-top.herokuapp.com/",
	"top_committies":"https://git-top.herokuapp.com/",
	"documentation": "https://github.com/thadanipaarth/GitTop"
}

class api_info(Resource):
	def get(self):
		return jsonify(resources)

# Route
api.add_resource(api_info,'/')

from app.resources.get_top_repositories import get_top_repositories
api.add_resource(get_top_repositories,'/get_top_repositories')

from app.resources.get_top_committees import get_top_committees
api.add_resource(get_top_committees,'/get_top_committees')

if __name__ == '__main__':
	app.run(debug=True)

