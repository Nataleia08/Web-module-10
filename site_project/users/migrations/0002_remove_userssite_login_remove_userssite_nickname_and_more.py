# Generated by Django 4.2 on 2023-04-25 18:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userssite",
            name="login",
        ),
        migrations.RemoveField(
            model_name="userssite",
            name="nickname",
        ),
        migrations.AddField(
            model_name="userssite",
            name="first_name",
            field=models.CharField(default="default first name", max_length=200),
        ),
        migrations.AddField(
            model_name="userssite",
            name="last_name",
            field=models.CharField(default="default last name", max_length=200),
        ),
        migrations.AddField(
            model_name="userssite",
            name="password",
            field=models.CharField(default="default password", max_length=200),
        ),
        migrations.AddField(
            model_name="userssite",
            name="username",
            field=models.CharField(default="username", max_length=200),
        ),
        migrations.AlterField(
            model_name="userssite",
            name="email",
            field=models.CharField(default="email@example.com", max_length=200),
        ),
        migrations.AlterField(
            model_name="userssite",
            name="phone",
            field=models.CharField(default="+380 00 0000000", max_length=200),
        ),
    ]