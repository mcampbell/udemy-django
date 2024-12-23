# Generated by Django 5.1.2 on 2024-12-23 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("book_outlet", "0006_address_author_address"),
    ]

    operations = [
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("code", models.CharField(max_length=2)),
            ],
        ),
        migrations.AddField(
            model_name="book",
            name="published_countries",
            field=models.ManyToManyField(to="book_outlet.country"),
        ),
    ]
