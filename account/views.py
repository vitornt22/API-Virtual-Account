
from rest_framework.viewsets import ModelViewSet

from .models import Account
from .serializers import AccountSerializer

# Create your views here.


class AccountApi(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
