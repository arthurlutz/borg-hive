# Generated by Django 3.0.5 on 2020-05-05 15:25

import borghive.lib.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('borghive', '0017_auto_20200504_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repositoryuser',
            name='name',
            field=models.CharField(default='3eiii5yt', max_length=8, unique=True),
        ),
        migrations.AlterField(
            model_name='sshpublickey',
            name='public_key',
            field=models.TextField(max_length=2048, validators=[django.core.validators.RegexValidator(message='SSH Public Key should match format: ssh-xxx AAAA... comment', regex='ssh-([a-zA-Z0-9]+) (AAAA[0-9A-Za-z+/=]+)( [\\w\\-@]+)?'), borghive.lib.validators.ssh_public_key_validator]),
        ),
    ]
