# Generated by Django 4.1.4 on 2022-12-20 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_useraccount', '0011_job_post_img_alter_job_category_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_post',
            name='posted_at',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
