# Generated by Django 3.0.6 on 2020-05-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='image/')),
                ('summary', models.CharField(max_length=250)),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]
