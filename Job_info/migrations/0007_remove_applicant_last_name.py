# Generated by Django 4.1.7 on 2023-04-10 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Job_info', '0006_rename_first_name_applicant_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='applicant',
            name='last_name',
        ),
    ]
