# Generated by Django 4.1.3 on 2022-12-07 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="dibuat",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]