# Generated by Django 4.2.1 on 2023-11-12 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_gender_friends_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friends',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='myapp.gender'),
        ),
    ]
