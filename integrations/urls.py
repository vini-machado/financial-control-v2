from django.urls import path
from integrations.views import testing_api_vamo_q_vamo

urlpatterns = [
    path('connectors/', testing_api_vamo_q_vamo, name='connectors.list'),
]