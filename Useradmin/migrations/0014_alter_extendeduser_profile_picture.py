# Generated by Django 4.0.2 on 2022-03-20 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0013_alter_extendeduser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile-pictures/'),
        ),
    ]