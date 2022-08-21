from django_q.models import Schedule
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings


class Command(BaseCommand):
    def handle(self, *args, **options):
        job_name = settings.BACKGROUND_JOB['name']
        fetchInterval = settings.BACKGROUND_JOB['fetchInterval']
        func = settings.BACKGROUND_JOB['func_name']

        if Schedule.objects.filter(name=job_name).count() == 0:
            Schedule.objects.create(
                name=job_name,
                func=func,
                minutes=fetchInterval,
                schedule_type=Schedule.MINUTES,
            )
        else:
            print(f'Job {job_name} already exists ')
