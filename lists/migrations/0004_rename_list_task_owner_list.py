# Generated by Django 4.1 on 2023-01-03 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0003_remove_list_tasks_task_list"),
    ]

    operations = [
        migrations.RenameField(
            model_name="task", old_name="list", new_name="owner_list",
        ),
    ]
