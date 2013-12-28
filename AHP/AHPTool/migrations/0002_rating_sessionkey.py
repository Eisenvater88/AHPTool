# encoding: utf8
from django.db import models, migrations
import datetime


class Migration(migrations.Migration):
    
    dependencies = [('AHPTool', '0001_initial')]

    operations = [
        migrations.AddField(
            field = models.CharField(default='', max_length=200),
            preserve_default = False,
            name = 'sessionkey',
            model_name = 'rating',
        ),
    ]
