# Generated by Django 2.2.12 on 2020-09-04 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_about_our_team'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='phone',
        ),
    ]