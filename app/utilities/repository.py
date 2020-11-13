#--------------------------------------------------------------------------------------------
# Last Edited: 11 Nov'20
# Description: This file contains the Repository class, with its dependacies and required functions
# -------------------------------------------------------------------------------------------
import requests
import sys
import json
from requests.auth import HTTPBasicAuth
from authentication_information import login_information

class Repository:
	def __init__(self,organization,repository):
		self.org=organization
		self.repo=repository
		self.link="https://api.github.com/repos/"+self.org+"/"+self.repo+"/contributors?per_page=100&page="
	
	def generate_request_link(self,page_number):
		return self.link + str(page_number)
	
	def get_top_contributors(self,number_of_committees):
		
		top_contributors={}

		top_contributors['data']=[]
		top_contributors['request_code']=200
		top_contributors['organization']=self.org
		top_contributors['repository']=self.repo
		
		page_number=1

		while len(top_contributors['data'])<number_of_committees:
			if login_information['personal_access_token']!=None:
				response=requests.get(self.generate_request_link(page_number),auth=HTTPBasicAuth("username",login_information['personal_access_token']))
			else:
				response=requests.get(self.generate_request_link(page_number))
			json_object=json.loads(response.content)
	
			if int(response.status_code/100) == 4:
				top_contributors['request_code']=400
				top_contributors['message']=json_object['message']
				top_contributors['data']=None
				break

			if len(json_object) == 0:
				break

			for each in json_object:
				if len(top_contributors['data']) == number_of_committees:
					break
				top_contributors['data'].append({
					'name':each['login'],
					'avatar_url':each['avatar_url'],
					'contributions':each['contributions'],
					'url':each['url']
					})

			page_number=page_number+1
		try:
			top_contributors['number_of_results']=len(top_contributors['data'])
			top_contributors['matched_with_query_repository_number'] =(top_contributors['number_of_results']==number_of_committees)
		except:
			None
		return top_contributors