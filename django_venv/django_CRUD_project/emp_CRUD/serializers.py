from rest_framework import serializers

from emp_CRUD.models import employee_Tables

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = employee_Tables
        fields = ('emp_ID', 'emp_name', 'emp_age', 'emp_sex')
