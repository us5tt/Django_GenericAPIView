# Generated by Django 3.2.8 on 2021-10-14 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('usd_price', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]