# Generated by Django 5.0.2 on 2024-04-23 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organs', '0002_rename_content_contact_message'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='timeStamp',
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='contact',
            name='message',
            field=models.TextField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=13),
        ),
    ]