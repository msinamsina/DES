from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login-register', views.loging_or_register, name='login_or_register'),
    path('create-user/', views.create_user, name='create_user'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('user-page/', views.user_page, name='user_page'),
]
