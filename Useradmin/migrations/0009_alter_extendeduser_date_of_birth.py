# Generated by Django 4.0.2 on 2022-03-13 15:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0008_alter_extendeduser_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='date_of_birth',
            field=models.DateField(default=datetime.date(2006, 3, 13)),
        ),
    ]
