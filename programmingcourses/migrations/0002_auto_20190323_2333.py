# Generated by Django 2.1.7 on 2019-03-23 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programmingcourses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
