# Generated by Django 4.1.4 on 2022-12-18 03:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_useraccount', '0003_job_post_jobholder'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_post',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app_useraccount.job_category'),
        ),
    ]
