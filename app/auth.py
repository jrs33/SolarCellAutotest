from functools import wraps
from flask import request, Response

'''
Utility wrapper functions used on routes to ensure basic authentication
'''

def checkAuth(username, password):
	return username == 'bu_eds_admin' and password == 'bostoncells36'

def authenticate():
	return Response('Unverified; need proper credentials', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requiresAuth(f):
	@wraps(f)
	def decorated(*args, **kwargs):
		auth = request.authorization
		if not auth or not checkAuth(auth.username, auth.password):
			return authenticate()
		return f(*args, **kwargs)
	return decorated
