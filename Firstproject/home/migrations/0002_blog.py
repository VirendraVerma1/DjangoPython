# Generated by Django 4.0.2 on 2022-02-17 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=122)),
                ('desc', models.TextField()),
                ('user_id', models.IntegerField(max_length=122)),
                ('username', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]