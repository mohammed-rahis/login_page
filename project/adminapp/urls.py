from django.urls import path,include
from adminapp import views

urlpatterns = [
   
    path('admin_login',views.admin_login, name= 'admin_login'),
    path('createuser',views.createuser, name= 'createuser'), 
    path('deleteuser/<int:id>/',views.deleteuser, name= 'deleteuser'), 
    path('updateuser/<int:id>/',views.updateuser, name= 'updateuser'), 
]
