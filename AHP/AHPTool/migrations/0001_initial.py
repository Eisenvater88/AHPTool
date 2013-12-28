# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
  #  dependencies = [(u'AHPTool', '__first__')]

    operations = [
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('name', models.CharField(max_length=200),)],
            bases = (models.Model,),
            options = {},
            name = 'Dimension',
        ),
        migrations.CreateModel(
            fields = [(u'id', models.AutoField(verbose_name=u'ID', serialize=False, auto_created=True, primary_key=True),), ('Dim1', models.ForeignKey(to=u'AHPTool.Dimension', to_field=u'id'),), ('Dim2', models.ForeignKey(to=u'AHPTool.Dimension', to_field=u'id'),), ('rating', models.IntegerField(default=1, choices=((9, 9,), (8, 8,), (7, 7,), (6, 6,), (5, 5,), (4, 4,), (3, 3,), (2, 2,), (1, 1,),)),), ('date', models.DateTimeField(auto_now=True),)],
            bases = (models.Model,),
            options = {},
            name = 'Rating',
        ),
    ]
