# Generated by Django 2.0.4 on 2018-04-19 02:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_auto_20180418_1049'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Status',
            new_name='status',
        ),
    ]
