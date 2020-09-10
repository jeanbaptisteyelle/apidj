# Generated by Django 2.2.12 on 2020-09-09 19:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0010_auto_20200907_2115'),
    ]

    operations = [
        migrations.AddField(
            model_name='reseauxsociau',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='created_by_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='siteinfo',
            name='about_footer_description',
            field=models.TextField(),
        ),
    ]