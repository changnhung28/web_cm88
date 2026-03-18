from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('go/<int:id>/', views.go_link, name='go_link'),

    path('register/', views.register_redirect, name='register'),
    path('login/', views.login_redirect, name='login'),
    path('code/', views.register_code, name='code'),
    path('tele/', views.register_tele, name='tele'),
]