# Generated by Django 4.0.2 on 2022-02-17 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_alter_extenduser_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extenduser',
            name='profile_picture',
            field=models.ImageField(default='avatar.png', upload_to='profile_picture/'),
        ),
    ]
