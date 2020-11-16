# GitTop - Top Result Fetching REST API

GitTop is a REST API that return the top repositories and committees by using different GitHub parameters like forks, commits, addition, deletetions as applicable. As of now, only fork parameter has been implemented. Additions are welcomed!

The current version of API has been hosted on [git-top.herokuapp.com](http://git-top.herokuapp.com/)

### Installation
1. Navigate to the main directory in the command prompt
2. Create a virtual envirnoment and activate it. (Reference for doing the same: [Click Here](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/))
3. `pip install -r requirments.txt`
4. `python wsgi.py`

### Available Resources
1. `/` : Gives the aviable resources and documentation link
2. `/get_top_repository` : To get the top repositories of a particual organization
> Mandatory Arguments:
> 1. org: defines the name of the organization that is owner of the repository
> 2. repo: number of top results the user wishes
> 3. parameter: the order by which the repositories should be ordered
>
> Sample Query: http://git-top.herokuapp.com/get_top_repositories?parameter=forks&org=google&repo=6
3. `/get_top_committees` : To get the top committees of a particular repository.
> Mandatory Arguments:
> 1. org: defines the name of the organization that is owner of the repository
> 2. repo: defined the name of the repository
> 3. committees: number of top results the user wishes
>
> Sample Query: http://git-top.herokuapp.com/get_top_committees?org=google&repo=libphonenumber&committees=5
4. `/get_top_repo_committees` : To get the top committees of every top repository of an organization
> Mandatory Arguments:
> 1. org: defines the name of the organization that is owner of the repository
> 2. repo: number of top results the user wishes
> 3. committees: number of top committees the user wishesfor each repository
>
> Sample Query: http://git-top.herokuapp.com/get_top_repo_committees?parameter=forks&org=google&repo=5&committees=2
