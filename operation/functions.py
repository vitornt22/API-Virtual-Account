

from account.models import Account
from rest_framework import status
from rest_framework.response import Response

from .models import Operation
from .serializers import OperationSerializer


# verifying balance or limit of account to substract the value
# of debit or credit
def verify_balance_or_limit_account(operation):
    category = operation['category']
    value = operation['value']
    account = operation['account']

    if category == 'debit':
        if value <= account.balance:
            operation['previousBalance'] = account.balance
            operation['account'].balance -= value
            operation['account'].save()
            operation['currentBalance'] = operation['account'].balance
            return True
        else:
            return False

    if category == 'credit':
        if value <= account.limit:
            operation['previousBalance'] = account.balance
            operation['account'].limit -= value
            operation['account'].save()
            operation['currenteBalance'] = operation['account'].balance
            return True
        else:
            return False


def set_category_operation(category, data):
    try:
        data['category'] = category
        data['account'] = Account.objects.get(id=data['account'])
        if (verify_balance_or_limit_account(data)):
            m = Operation(**data)
            m.category = category
            # Adding current balance of account, to list extracts and show
            # initial and final balance of a period
            m.currentBalance = m.account.balance
            if category == 'debit':
                m.installments = None
            m.save()
            return m
        else:
            return False
    except Account.DoesNotExist:
        return None


# This method returns serializer of operations created or error message,
# if there is
def return_method(operation):
    if operation is not None:
        if operation is False:
            error = 'Saldo ou Limite insuficiente'
        else:
            return Response(OperationSerializer(operation).data, status=status.HTTP_200_OK)  # noqa

    else:
        error = 'Erro inesperado'
    return Response({'Error': error}, status=status.HTTP_400_BAD_REQUEST)
