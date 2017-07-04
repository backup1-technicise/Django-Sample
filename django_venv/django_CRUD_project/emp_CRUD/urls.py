from django.conf.urls import url
from emp_CRUD import views

urlpatterns = [ 
	url( r'^show_Employees/$', views.emp_list ),
	url( r'^create_Employee/$', views.emp_create ),
	url( r'^show_employee_by_ID/(?P<emp_id>.*)/$', views.get_emp_by_id ),
	url( r'^update_employee_by_ID/(?P<emp_id>.*)/$', views.update_emp_by_id ),
	url( r'^delete_employee_by_ID/(?P<emp_id>.*)/$', views.delete_emp_by_id ),
]

