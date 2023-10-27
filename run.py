import asyncio
from aiogram.enums import ParseMode
from aiogram import Bot, Dispatcher
from config import *
from routers import start_router, message_router, callback_router
from database import DatabaseManager

# Creates a connection pool for the database, and the database itself if it does not exist
db_manager = DatabaseManager(pool_name="my_pool", pool_size=25)
dbpool = db_manager.pool


async def main() -> None:
    dp = Dispatcher()

    # Adds handlers for different types of messages to the dispatcher
    dp.include_routers(start_router, message_router, callback_router)

    bot = Bot(token, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
