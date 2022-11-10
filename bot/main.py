from loguru import logger
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from bot.handlers import register_user_handlers
from bot.database import register_models
from bot.parsing import start_schedule
from bot.misc import Config, set_language, ThrottlingMiddleware


async def on_start_up(dp: Dispatcher) -> None:
    logger.info('Bot starts')
    register_models()
    register_user_handlers(dp)
    set_language()
    start_schedule()


def start_telegram_bot() -> None:
    bot = Bot(token=Config.TOKEN, parse_mode='HTML')
    dp = Dispatcher(bot, storage=MemoryStorage())
    dp.middleware.setup(ThrottlingMiddleware())
    executor.start_polling(dp, skip_updates=True, on_startup=on_start_up)
