from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('go/<int:id>/', views.go_link),
    path('register/', views.register_redirect),
    path('login/', views.login_redirect),
    path('register_code/', views.register_code),
    path('register_tele/', views.register_tele),
]