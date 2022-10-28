

import datetime

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .functions import return_method, set_category_operation
from .models import Operation
from .serializers import ExtractsSerializer, OperationSerializer


class OperationApi (ModelViewSet):
    queryset = Operation.objects.all().order_by('date')
    serializer_class = OperationSerializer

    def get_queryset(self):
        return super().get_queryset()

    # disabling create method to access set operations method through endpoint
    # defined below
    def create(self, request):
        response = {
            'message': 'Create function is not offered in this path.'}
        return Response(response, status=status.HTTP_403_FORBIDDEN)

    # endpoint to set debit in virtual account
    @action(methods=['POST'], detail=False)
    def toDebit(self, request, *args, **kwargs):
        # defining category to operation (debit or credit)
        debit = set_category_operation('debit', request.data)
        # Return the serializer of the operation or error message
        return return_method(debit)

    # endpoint to set debit in virtual account

    @action(methods=['POST'], detail=False, url_name='')
    def toCredit(self, request):
        # defining category to operation (debit or credit)
        credit = set_category_operation('credit', request.data)
        # Return the serializer of the operation or error message
        return return_method(credit)  # noqa

    @action(methods=['GET'], detail=False)
    def getExtracts(self, request, pk, * args, **kwargs):
        month = int(kwargs['month'])
        year = int(kwargs['year'])
        extracts = Operation.objects.filter(account=pk,
                                            date__month=month,  # noqa
                                            date__year=year).order_by('date')

        date = datetime.date(day=1, month=month, year=year)

        if extracts is None:
            return Response({})
        return Response(ExtractsSerializer(
                extracts,
                many=False,
                context={'list': extracts, 'date': date, 'account': pk}
                ).data, status=status.HTTP_200_OK)  # noqa
