# -*- coding: utf-8 -*-
# !/usr/bin/env python

# @Time    : 2021/8/24 21:11
# @Author  : NoWords
# @FileName: runapscheduler.py
import logging

from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django.conf import settings

logger = logging.getLogger(__name__)


def hello():
    print('=== hello scheduler ===')


def start():
    scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)

    # Adding this job here instead of to crons.
    # This will do the following:
    # - Add a scheduled job to the job store on application initialization
    # - The job will execute a model class method at midnight each day
    # - replace_existing in combination with the unique ID prevents duplicate copies of the job
    scheduler.add_job(
        hello,
        trigger=CronTrigger(second="*/10"),
        id="hello_scheduler",
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Added job 'hello_scheduler'.")

    # Add the scheduled jobs to the Django admin interface
    # register_events(scheduler)
    logger.info("Starting scheduler...")
    scheduler.start()
