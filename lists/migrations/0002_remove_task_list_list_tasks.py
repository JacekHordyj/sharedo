# Generated by Django 4.1 on 2023-01-02 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(model_name="task", name="list",),
        migrations.AddField(
            model_name="list",
            name="tasks",
            field=models.ManyToManyField(blank=True, to="lists.task"),
        ),
    ]
