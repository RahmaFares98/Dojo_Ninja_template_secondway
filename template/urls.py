# your_app_name/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'), 
    path('add_dojo', views.add_dojo, name='add_dojo'),
    path('add_ninja', views.add_ninja, name='add_ninja'),
    path('delete_btn/<int:dojo_id>/', views.delete_btn, name='delete_btn'),
]
