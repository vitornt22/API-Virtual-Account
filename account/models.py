from django.db import models


# Create your models here.
class Account(models.Model):
    owner = models.CharField(max_length=200, null=False, blank=False)
    cpf = models.CharField(max_length=11, null=False, blank=False, unique=True)
    limit = models.FloatField()
    balance = models.FloatField()
    numberAccount = models.CharField(max_length=15, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
