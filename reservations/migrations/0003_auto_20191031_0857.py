# Generated by Django 2.2.5 on 2019-10-30 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_auto_20191020_0637'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('cancled', 'Cancled')], default='pending', max_length=12),
        ),
    ]