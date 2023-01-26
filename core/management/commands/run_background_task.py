# django command to run background task
# python manage.py run_background_task
import time

from django.core.management.base import BaseCommand
from core.tasks import check_urls
from django.conf import settings


class Command(BaseCommand):
    help = 'Run background task'

    def handle(self, *args, **options):
        # get interval from settings

        interval = settings.BACKGROUND_TASK_RUN_INTERVAL
        while True:
            # check urls every interval
            check_urls()
            time.sleep(interval)
