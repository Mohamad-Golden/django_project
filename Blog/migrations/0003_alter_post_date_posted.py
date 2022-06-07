# Generated by Django 3.2.5 on 2021-07-27 21:14

from django.db import migrations, models
import persiantools.jdatetime


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0002_alter_post_date_posted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date_posted',
            field=models.DateTimeField(default=persiantools.jdatetime.JalaliDateTime.now),
        ),
    ]