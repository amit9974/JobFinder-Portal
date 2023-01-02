# Generated by Django 4.1.4 on 2022-12-19 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_useraccount', '0005_alter_job_post_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=100)),
                ('experience', models.CharField(max_length=20)),
                ('current_ctc', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('mobile', models.CharField(max_length=10)),
                ('resume', models.FileField(upload_to='media/employee/resume')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
