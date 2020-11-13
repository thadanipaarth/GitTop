#---------------------------------------------------------------------------------------------------
# This file contains the parameter checking conditions and if found that provided odering is not avaliable, error is returned
#---------------------------------------------------------------------------------------------------

available_order=['fork']
error={
	'Order_Not_Found':{
		"message":"Bad Request, Parameter not found",
		"documentation":"https://github.com/thadanipaarth/GitTop"
	}
}
def check_valid_parameter(parameter):
	if parameter not in available_order:
		return error['Order_Not_Found']
	else:
		return None