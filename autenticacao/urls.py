from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cadastro),
    path('auth/', views.auth, name ='auth' ),
]