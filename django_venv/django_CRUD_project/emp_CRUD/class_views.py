# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from emp_CRUD.models import employee_Tables
from emp_CRUD.serializers import EmployeeSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# Create your views here.

class EmpList(APIView):

	@csrf_exempt
	def emp_list(request):
    		"""
    		GET all employees, or POST or create a new employee.
    		"""
    		if request.method == 'GET':
        		employees = employee_Tables.objects.all()
        		serializer = EmployeeSerializer(employees, many=True)
        		return JsonResponse(serializer.data, safe=False)


	@csrf_exempt
	def emp_create(request):
    		if request.method == 'POST':
        		data = JSONParser().parse(request)
        		serializer = EmployeeSerializer(data=data)
        		if serializer.is_valid():
            			serializer.save()
            			return JsonResponse(serializer.data, status=201)
			else:
            			return JsonResponse(serializer.errors, status=400)

class EmpList_details(APIView):
	@csrf_exempt
	def get_emp_by_id(request, emp_id):
		# Retrieve EMP by its emp ID
		try:
        		emp = employee_Tables.objects.get(emp_ID=emp_id)
    		except emp.DoesNotExist:
        		return HttpResponse(status=404)
  
		if request.method == 'GET':
        		serializer = EmployeeSerializer(emp)
        		return JsonResponse(serializer.data)


	@csrf_exempt
	def update_emp_by_id(request, emp_id):
		# Retrieve EMP by its emp ID
		try:
        		emp = employee_Tables.objects.get(emp_ID=emp_id)
    		except emp.DoesNotExist:
        		return HttpResponse(status=404)
  
		if request.method == 'PUT':
        		data = JSONParser().parse(request)
        		serializer = EmployeeSerializer(emp, data=data)
        		if serializer.is_valid():
            			serializer.save()
            			return JsonResponse(serializer.data)
			else:
        			return JsonResponse(serializer.errors, status=400)


	@csrf_exempt
	def delete_emp_by_id(request, emp_id):
		# Retrieve EMP by its emp ID
		try:
        		emp = employee_Tables.objects.get(emp_ID=emp_id)
    		except emp.DoesNotExist:
        		return HttpResponse(status=404)

		if request.method == 'DELETE':
        		emp.delete()
        		return HttpResponse(status=204)




'''
@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Snippet.objects.get(pk=pk)
    except Snippet.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SnippetSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = SnippetSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)
'''
