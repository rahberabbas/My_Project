# Generated by Django 2.2.7 on 2020-01-10 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='context',
            name='videofile',
            field=models.FileField(null=True, upload_to='videos/', verbose_name=''),
        ),
    ]
