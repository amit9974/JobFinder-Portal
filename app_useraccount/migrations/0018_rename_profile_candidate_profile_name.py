# Generated by Django 4.1.4 on 2022-12-22 07:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_useraccount', '0017_alter_job_post_jobholder'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='profile',
            new_name='profile_name',
        ),
    ]