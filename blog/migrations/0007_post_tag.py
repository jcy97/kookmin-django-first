# Generated by Django 5.0.4 on 2024-05-18 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0006_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="tag",
            field=models.ManyToManyField(blank=True, to="blog.tag"),
        ),
    ]
