# Generated by Django 4.1.4 on 2022-12-20 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_useraccount', '0012_job_post_posted_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_post',
            name='job_type',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
