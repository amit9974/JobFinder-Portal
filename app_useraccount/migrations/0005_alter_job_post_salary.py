# Generated by Django 4.1.4 on 2022-12-18 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_useraccount', '0004_job_post_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='salary',
            field=models.CharField(max_length=10, null=True),
        ),
    ]