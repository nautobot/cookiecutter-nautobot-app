"""This is a helper script meant for celery beat to check for migrations. The beat
error log is too large and hides from your terminal the most common case in which you
will have issues with the migrations or around the same time migrations are running."""

import time
from django.db import ProgrammingError
import nautobot

nautobot.setup()

from nautobot.extras.models.jobs import ScheduledJob

while True:
    try:
        list(ScheduledJob.objects.all())
        print("Migrations are complete, proceeding.")
        break
    except ProgrammingError:
        print("Migrations not complete yet, retrying in 5 seconds...")
        time.sleep(5)  # Wait for a few seconds before retrying