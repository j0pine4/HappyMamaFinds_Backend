# Generated by Django 4.2.1 on 2023-07-24 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserAuth', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='message',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
    ]