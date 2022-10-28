from account.models import Account
from django.db import models

CATEGORY = (('debit', 'debit'), ('credit', 'credit'))
# Create your models here.


class Operation(models.Model):
    category = models.CharField(
        choices=CATEGORY, max_length=8, null=True, blank=True,
        error_messages={'invalid': "Value must be 'debit' or 'credit'"})
    value = models.FloatField()
    description = models.CharField(max_length=200)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    currentBalance = models.FloatField()
    previousBalance = models.FloatField()
    installments = models.IntegerField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
