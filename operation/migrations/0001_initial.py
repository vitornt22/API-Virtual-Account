# Generated by Django 4.1.2 on 2022-10-28 04:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, choices=[('debit', 'debit'), ('credit', 'credit')], error_messages={'invalid': "Value must be 'debit' or 'credit'"}, max_length=8, null=True)),
                ('value', models.FloatField()),
                ('description', models.CharField(max_length=200)),
                ('currenteBalance', models.FloatField()),
                ('installments', models.IntegerField(blank=True, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]
