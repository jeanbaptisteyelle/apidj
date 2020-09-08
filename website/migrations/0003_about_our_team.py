# Generated by Django 2.2.12 on 2020-09-04 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20200904_1505'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=150)),
                ('image', models.ImageField(upload_to='image/about')),
                ('description', models.TextField()),
                ('lien', models.URLField()),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'verbose_name': 'About',
                'verbose_name_plural': 'Abouts',
            },
        ),
        migrations.CreateModel(
            name='Our_team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/our_team')),
                ('nom', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('date_add', models.DateTimeField(auto_now_add=True, null=True)),
                ('date_update', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.BooleanField(blank=True, default=True)),
            ],
            options={
                'verbose_name': 'Our_team',
                'verbose_name_plural': 'Our_teams',
            },
        ),
    ]