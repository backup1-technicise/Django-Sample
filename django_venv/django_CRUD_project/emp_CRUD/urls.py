from django.conf.urls import url
#from django.conf.urls.defaults import *
#from piston.resource import Resource
#from piston.authentication import HttpBasicAuthentication

from emp_CRUD.handlers import testDBInsertHandler # DB POST insert by Abhisek
from emp_CRUD.handlers import testDBReadHandler   # DB GET read by Abhisek
from emp_CRUD.handlers import POST_ReadHandler	 # DB POST read by Abhisek
from emp_CRUD.handlers import POST_UpdateHandler  # DB UPDATE read by Abhisek
from emp_CRUD.handlers import POST_DeleteHandler  # Delete from DB by Abhisek

'''
auth = HttpBasicAuthentication(realm="Django Piston Example")

class CsrfExemptResource( Resource ):
	"""
	def __init__( self, handler, authentication = auth ):
	"""
	def __init__( self, handler, authentication = None ):
		super( CsrfExemptResource, self ).__init__( handler, authentication )
		self.csrf_exempt = getattr( self.handler, 'csrf_exempt', True )

'''
testDBInsertHandler_resource = CsrfExemptResource( testDBInsertHandler ) # DB POST insert by Abhisek
testDBReadHandler_resource = CsrfExemptResource( testDBReadHandler )	# DB GET read by Abhisek
POST_ReadHandler_resource = CsrfExemptResource( POST_ReadHandler )	# DB POST read by Abhisek
POST_UpdateHandler_resource = CsrfExemptResource( POST_UpdateHandler )  # DB POST update by Abhisek
POST_DeleteHandler_resource = CsrfExemptResource( POST_DeleteHandler )  # Delete from DB by Abhisek



urlpatterns = [ 
	#url( r'^testPost/', testPostHandler_resource ),
	url( r'^testDBInsert/', testDBInsertHandler_resource ),
	url( r'^testDBDisplay/(?P<emp_id>.*)/', testDBReadHandler_resource ),
	url( r'^POST_read/', POST_ReadHandler_resource ),
	url( r'^POST_update/', POST_UpdateHandler_resource ),
	url( r'^POST_delete/', POST_DeleteHandler_resource ),
]

