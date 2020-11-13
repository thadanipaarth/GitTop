#--------------------------------------------------------------------------------------------
# Last Edited: 11 Nov'20
# Description: This file contains the organization class, with its dependacies and required functions
# -------------------------------------------------------------------------------------------

import requests
import sys
import json
from requests.auth import HTTPBasicAuth
from authentication_information import login_information

class Organization:
	
	#class constructor
	def __init__(self,name_of_organization,order):
		self.name=name_of_organization
		self.request_link_fork="https://api.github.com/search/repositories?q=user:"+self.name+"&per_page=100&sort="+order+"&order=desc"

	def get_request_url(self,page_number):
		return self.request_link_fork+"&page="+str(page_number)

	#This function returns the top_respositores with their forks and contributors url for further processing
	def get_top_repositories(self,repo_number):
		top_repositories={}

		top_repositories['data']=[]
		top_repositories['request_code']=200 #Defined request_code parameter to get if any error is occured while fetching

		page_number=1
		total_results=sys.maxsize

		while len(top_repositories['data'])<repo_number and len(top_repositories['data'])<total_results:
			
			if login_information['personal_access_token']!=None:
				response=requests.get(self.get_request_url(page_number),auth=HTTPBasicAuth("username",login_information['personal_access_token']))
			else:
				response=requests.get(self.get_request_url(page_number))
			json_object=json.loads(response.content)
			
			try:
				total_results=json_object['total_count']
			except:
				top_repositories['request_code']=400 #Returing with an error and the error message is passed on as message in the dictonary. 
				top_repositories['message']=json_object
				top_repositories['data']= None
				break

			for each in json_object['items']:
				if len(top_repositories['data']) == repo_number: #If the required repositories are fetched then the loop is broken as there are 100 results in single search query
					break
				top_repositories['data'].append(
					{
						'name':each['name'],
						'contributors_url': each['contributors_url'],
						'forks': each['forks_count']
					}
				)
			page_number=page_number+1
		try:
			top_repositories['number_of_repositories']=len(top_repositories['data'])
			top_repositories['matched_with_query_repository_number']=(top_repositories['number_of_repositories'] == repo_number) #This quantity reflects if the number of repositories to fecthed (passed to the function) are obtained
		except:
			None
		top_repositories['organization']=self.name

		return top_repositories
