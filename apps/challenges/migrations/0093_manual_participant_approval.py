# Generated by Django 2.2.20 on 2023-06-09 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("participants", "0012_remove_docker_repository_uri_from_team"),
        ("challenges", "0092_challenge_allow_cancel_running_submissions"),
    ]

    operations = [
        migrations.AddField(
            model_name="challenge",
            name="approved_participant_teams",
            field=models.ManyToManyField(
                blank=True,
                related_name="approved_challenge_participant_teams",
                to="participants.ParticipantTeam",
            ),
        ),
        migrations.AddField(
            model_name="challenge",
            name="manual_participant_approval",
            field=models.BooleanField(default=False),
        ),
    ]
