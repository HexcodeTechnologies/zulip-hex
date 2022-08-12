# Generated by Django 1.11.6 on 2018-01-10 01:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0133_rename_botuserconfigdata_botconfigdata"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScheduledMessage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("subject", models.CharField(max_length=200)),
                ("content", models.TextField()),
                ("scheduled_timestamp", models.DateTimeField(db_index=True)),
                ("delivered", models.BooleanField(default=False)),
                (
                    "realm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.Realm"
                    ),
                ),
                (
                    "recipient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.Recipient"
                    ),
                ),
                (
                    "sender",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
                    ),
                ),
                (
                    "sending_client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="zerver.Client"
                    ),
                ),
                (
                    "stream",
                    models.ForeignKey(
                        null=True, on_delete=django.db.models.deletion.CASCADE, to="zerver.Stream"
                    ),
                ),
            ],
        ),
    ]
