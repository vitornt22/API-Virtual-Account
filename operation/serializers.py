

from account.models import Account
from rest_framework import serializers

from .models import Operation


def get_previous_balance(date):
    d = Operation.objects.filter(date__lte=date).first()
    return d.currentBalance


class OperationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Operation
        fields = '__all__'
        extra_kwargs = {'category': {'read_only': True},
                        'currentBalance': {'read_only': True},
                        'previousBalance': {'read_only': True}}


class ExtractsSerializer(serializers.Serializer):
    initialBalance = serializers.SerializerMethodField('get_initial_balance')
    finalBalance = serializers.SerializerMethodField('get_final_balance')
    extracts = serializers.SerializerMethodField('get_extracts')

    def get_extracts(self, obj):
        return OperationSerializer(obj, many=True).data

    def get_initial_balance(self, obj):
        if Operation.objects.all() is None:
            account = Account.objects.get(id=self.context.get('account'))
            return account.balance
        elif obj is None:
            date = self.context.get('date')
            # This method return current balance of account
            # searching previous operation date,if there is no operation in
            # this period
            get_previous_balance(date)
        else:
            return obj.first().currentBalance

    def get_final_balance(self, obj):
        if Operation.objects.all() is None:
            account = Account.objects.get(id=self.context.get('account'))
            return account.balance
        elif obj is None:
            date = self.context.get('date')
            # This method return current balance of account
            # searching previous operation date,if there is no operation in
            # this period
            get_previous_balance(date)
        else:
            return obj.last().currentBalance
