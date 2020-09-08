# Generated by Django 2.2.12 on 2020-09-04 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='contact_info',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='newletter',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='reseauxsociau',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reseauxsociau',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='reseauxsociau',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='date_add',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='status',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]