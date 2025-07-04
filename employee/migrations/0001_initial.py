# Generated by Django 5.2.4 on 2025-07-04 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Employee",
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
                ("emp_id", models.CharField(max_length=10)),
                ("name", models.CharField(max_length=20)),
                ("designation", models.CharField(max_length=10)),
                ("email", models.EmailField(max_length=20)),
                ("add", models.CharField(max_length=20)),
                ("salary", models.IntegerField(max_length=10)),
            ],
        ),
    ]
