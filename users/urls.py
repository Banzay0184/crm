from . import views
from django.urls import path

urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign_out/', views.sign_out, name='sign_out'),
    path('construction/', views.construction, name='construction'),
]
