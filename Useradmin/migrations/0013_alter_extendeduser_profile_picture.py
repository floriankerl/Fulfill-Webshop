# Generated by Django 4.0.2 on 2022-03-20 17:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Useradmin', '0012_alter_extendeduser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extendeduser',
            name='profile_picture',
            field=models.ImageField(default='profile-pictures/user_icon.png', upload_to='profile-pictures/'),
        ),
    ]
