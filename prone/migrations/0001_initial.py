# Generated by Django 2.2.7 on 2020-01-10 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Context',
            fields=[
                ('num', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default='', max_length=100)),
                ('cat', models.CharField(default='', max_length=100)),
                ('desc', models.CharField(default='', max_length=1000)),
                ('pub_date', models.DateField()),
                ('img', models.ImageField(default='', upload_to='prone/images')),
            ],
        ),
    ]
