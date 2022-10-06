from apscheduler.schedulers.asyncio import AsyncIOScheduler
from loguru import logger
from bot.misc.parser import update_database


def start_schedule() -> None:
    logger.info('Schedule started')
    scheduler = AsyncIOScheduler()
    scheduler.add_job(update_database, 'interval', minutes=120, id='database')
    scheduler.start()