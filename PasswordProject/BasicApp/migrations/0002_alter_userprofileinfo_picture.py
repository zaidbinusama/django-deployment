# Generated by Django 3.2.5 on 2021-08-19 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BasicApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='picture',
            field=models.ImageField(blank=True, upload_to='profile_pics'),
        ),
    ]
