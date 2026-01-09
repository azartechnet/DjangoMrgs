from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('login/',views.login_view,name='login'),
    path('employee/',views.add_employee,name='employee'),
    path('employees/',views.list_employees,name='employees'),
    path('edit_employee/<int:id>/',views.edit_employee,name='edit_employee'),
    path('delete_employee/<int:id>/',views.delete_employee,name='delete_employee'),
]