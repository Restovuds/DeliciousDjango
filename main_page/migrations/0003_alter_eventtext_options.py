# Generated by Django 5.1 on 2024-09-01 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_alter_eventtext_position'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='eventtext',
            options={'ordering': ('event', 'is_visible', 'position'), 'verbose_name': 'Event Text', 'verbose_name_plural': 'Event Texts'},
        ),
    ]
