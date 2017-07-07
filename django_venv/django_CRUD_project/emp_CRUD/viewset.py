from rest_framework import viewsets
from emp_CRUD.models import employee_Tables
from emp_CRUD.serializers import EmployeeSerializer

class EmpViewSet(viewsets.ModelViewSet):
 	queryset = employee_Tables.objects.all()
 	serializer_class = EmployeeSerializer


class EmpdetailsViewSet(viewsets.ModelViewSet):
 	queryset = employee_Tables.objects.all()
 	serializer_class = EmployeeSerializer


