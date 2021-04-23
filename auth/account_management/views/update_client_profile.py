from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from account_management.models import Account


@api_view(['PUT', ])
def update_client_profile(request):
    request_data = request.data
    try:
        account = Account.objects.get(username=request_data['username'], account_type='client')
    except Account.DoesNotExist:
        return Response(data='account not found', status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        data = {'username': account.username}
        account.phone_number = request_data.get('phone_number', None) if request_data.get('phone_number',
                                                                                          None) is not None else account.phone_number
        account.save()
        data['phone_number'] = account.phone_number
        data['response'] = 'Account update success'

        return Response(data=data, status=status.HTTP_200_OK)
    return Response(data='invalid request', status=status.HTTP_400_BAD_REQUEST)
