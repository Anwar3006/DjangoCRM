from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    # path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('record/<int:id>', views.customer_record, name='record'),
    path('delete_record/<int:id>', views.delete_record, name='delete_record'),
    path('insert_record/', views.insert_record, name='insert_record'),
    path('update_record/<int:id>', views.update_record, name='update_record'),

]
