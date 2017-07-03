from piston.handler import BaseHandler
#from client import IndivoClient
#from xml.dom import minidom as XML
#import xmltodict, json
#import xml.etree.ElementTree as ET
#from xml.etree.ElementTree import XML, fromstring, tostring
#import sys, string, os
from django.http import HttpResponse
from django.http import QueryDict 

import urllib 
import MySQLdb
from emp_CRUD.models import employee_Tables



########################## Mysql DB Interaction by Abhisek #####################################
class testDBInsertHandler( BaseHandler ):
	def create(self, request):
		# Creating an entry in EMP_INFO table in django_db database from MySQL
		# Value taken from json file via. POST call using POST man
		allowed_methods = ('POST')
		model = employee_Tables
		if request.method == 'POST':
			ID = request.data['id']
			name = request.data['name']
			sex = request.data['sex']
			age = request.data['age']

			emp_info = employee_Tables(emp_ID = ID,emp_name = name,emp_age = age, emp_sex = sex)
			emp_info.save()
					
class testDBReadHandler( BaseHandler ):
	# Retrieving an entry from EMP_INFO table in django_db database from MySQL 
	# using primary key emp_ID via. GET call
	def read(self,request,emp_id):
		allowed_methods = ('GET')
		model = employee_Tables
		if request.method == 'GET':
			return employee_Tables.objects.filter(emp_ID=emp_id).values("emp_ID","emp_name","emp_age","emp_sex")
			
class POST_ReadHandler( BaseHandler ):
	# Retrieving an entry from EMP_INFO table in django_db database from MySQL 
	# using primary key emp_ID via. POST call
	def create(self,request,**kwargs):
		allowed_methods = ('POST')
		model = employee_Tables
		if request.method == 'POST':
			ID = request.data['id']
			return employee_Tables.objects.filter(emp_ID=ID).values("emp_ID","emp_name","emp_age","emp_sex")
		
class POST_UpdateHandler( BaseHandler ):
	# Update an entry in EMP_INFO table in django_db database from MySQL 
	# using primary key emp_ID via. POST call
	def create(self,request):
		allowed_methods = ('POST')
		model = employee_Tables
		if request.method == 'POST':
			ID = request.data['id']
			name = request.data['name']
			## Update the emp_name as name where emp_ID is ID
			emp_tuple = employee_Tables.objects.get(emp_ID=ID)
			emp_tuple.emp_name = name
			emp_tuple.save()
			return employee_Tables.objects.filter(emp_ID=ID).values("emp_ID","emp_name","emp_age","emp_sex")

class POST_DeleteHandler( BaseHandler ):
	# Deleting an entry from EMP_INFO table in django_db database from MySQL 
	# using primary key emp_ID via. POST call
	def create(self,request):
		allowed_methods = ('POST')
		model = employee_Tables
		if request.method == 'POST':
			ID = request.data['id']
			## Delete employee record based on emp_ID
			emp_tuple = employee_Tables.objects.get(emp_ID=ID)
			#emp_tuple.emp_name = name
			emp_tuple.delete()
			return employee_Tables.objects.filter(emp_ID=ID).values("emp_ID","emp_name","emp_age","emp_sex")

			
