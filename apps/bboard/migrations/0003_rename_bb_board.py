# Generated by Django 4.2.1 on 2023-06-03 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0002_rubric_alter_bb_options_alter_bb_content_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bb',
            new_name='Board',
        ),
    ]
