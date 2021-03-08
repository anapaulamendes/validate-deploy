# Generated by Django 3.1.7 on 2021-03-07 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Approvals",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("token", models.CharField(max_length=255, unique=True)),
                ("approved", models.BooleanField(default=False)),
                ("email", models.EmailField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Release",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ReleaseName", models.CharField(max_length=255)),
                ("ReleaseId", models.IntegerField(unique=True)),
                ("TeamProject", models.CharField(max_length=255)),
            ],
        ),
    ]
