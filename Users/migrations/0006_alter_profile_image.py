# Generated by Django 4.0.4 on 2022-06-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='pictures/default.jpg', upload_to='pictures'),
        ),
    ]
