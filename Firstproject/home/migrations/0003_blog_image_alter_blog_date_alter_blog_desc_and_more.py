# Generated by Django 4.0.2 on 2022-02-25 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to='static/images/'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='desc',
            field=models.TextField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default=None, max_length=122, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='user_id',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='username',
            field=models.CharField(default=None, max_length=122, null=True),
        ),
    ]
