# Generated by Django 3.2.4 on 2021-09-16 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hawk', '0002_auto_20210830_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_data',
            name='qr_code',
            field=models.ImageField(blank=True, help_text='student image', upload_to='qr_codes'),
        ),
    ]
