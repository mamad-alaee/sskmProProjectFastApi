from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger

import shutil
from os.path import exists,isdir
from os import mkdir,getcwd,listdir

def say_hello():
    print("Hello, World!")

def say_hello_5s():
    scheduler = BackgroundScheduler()
    scheduler.add_job(say_hello, 'interval', seconds=5)
    scheduler.start()

def say_hello_5Am():
    scheduler = BackgroundScheduler()
    scheduler.add_job(say_hello, 'cron', hour=5,minute=10,second=33)
    scheduler.start()


def say_hello_mon_8Am():
    scheduler = BackgroundScheduler()
    trigger = CronTrigger(day_of_week='mon', hour=8, minute=10, second=33)
    scheduler.add_job(say_hello, trigger)

def copy_files():
    print("called")
    cwd = getcwd()

    backup_dir = f"{cwd}\\backup"
    if not isdir(backup_dir):
        mkdir(backup_dir)


    log_file_path = f"{cwd}\\log"
    if isdir(log_file_path):
        for file in listdir(log_file_path):
            shutil.copy(f"{log_file_path}\\{file}", backup_dir)


def copy_files_every_5s():
    scheduler = BackgroundScheduler()
    # trigger = CronTrigger(seconds=5)
    scheduler.add_job(copy_files,"interval",seconds=5)
    scheduler.start()

