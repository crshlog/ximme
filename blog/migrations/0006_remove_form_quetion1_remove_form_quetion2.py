# Generated by Django 4.2.3 on 2023-09-20 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_form_quetion2_alter_form_quetion1_delete_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='form',
            name='quetion1',
        ),
        migrations.RemoveField(
            model_name='form',
            name='quetion2',
        ),
    ]
