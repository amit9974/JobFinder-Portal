# Generated by Django 4.1.4 on 2022-12-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_useraccount', '0013_job_post_job_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='posted_at',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
