# Generated by Django 5.1.2 on 2024-10-17 00:28

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("todo", "0002_todomodel_dutdate_todomodel_priority"),
    ]

    operations = [
        migrations.RenameField(
            model_name="todomodel",
            old_name="dutdate",
            new_name="duedate",
        ),
    ]
