from django.http import JsonResponse
from integrations.services.pluggy.api import PluggyAPI

api = PluggyAPI()


def testing_api_vamo_q_vamo(request):
    connectors = api.list(
        countries=request.GET.getlist('countries'),
        types=request.GET.getlist('types'),
        name=request.GET.get('name'),
        sandbox=request.GET.get('sandbox'),
        health_details=request.GET.get('healthDetails'),
        is_open_finance=request.GET.get('isOpenFinance'),
        supports_payment_initiation=request.GET.get('supportsPaymentInitiation')
    )
    return JsonResponse(connectors)