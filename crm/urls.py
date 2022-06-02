from .views import *
from django.urls import path

urlpatterns = [
    path('', leads, name='leads'),
    path('project/', projects, name='project'),
    path('sales_funnel/', sales_funnel, name='sales_funnel'),
    path('update_lead/<pk>', update_lead, name='update_lead_url'),
    path('delete_lead/<pk>', delete_lead, name='delete_lead'),
    path('delete_project/<pk>', delete_project, name='delete_project'),
    path('change_status/<pk>', change_status, name='change_status_url')
]
