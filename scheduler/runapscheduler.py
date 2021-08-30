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

scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)


def hello():
    print('=== hello scheduler ===')


def start():
    scheduler.add_job(
        hello,
        trigger=CronTrigger(second="*/10"),
        id="hello_scheduler",
        max_instances=1,
        replace_existing=True,
    )
    logger.info("Added job 'hello_scheduler'.")

    scheduler.start()
    logger.info("Started scheduler...")


def stop():
    scheduler.shutdown()
    logger.info("Stopped scheduler...")
