# Generated by Django 4.1.4 on 2022-12-22 07:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_useraccount', '0015_alter_job_post_posted_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_post',
            name='jobholder',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='jobpost', to=settings.AUTH_USER_MODEL),
        ),
    ]
