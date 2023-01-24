import asyncio
import logging

from aiogram import Bot, Dispatcher

from config_data.config import Config, load_config
from handlers.user_handlers import register_user_hadlers
from handlers.other_handlers import register_other_handlers


# инициализация логгера
logger = logging.getLogger(__name__)

# функция для регистрации всех хэндлеров
def register_all_handlers(dp: Dispatcher) -> None:
    register_user_hadlers(dp)
    register_other_handlers(dp)
    
# функция конфигурирования и запуска бота
async def main():
    # конфигурирование логгирования
    logging.basicConfig(
        level=logging.INFO,
        format=u'%(filename)s:%(lineno)d #%(levelname)-8s '
               u'[%(asctime)s] - %(name)s - %(message)s'
    )

    # вывод в консоль информации о запуске бота
    logger.info('Starting bol')

    # загрузка конфига в переменную config
    config: Config = load_config()

    # инициализация бота и диспетчера
    bot: Bot = Bot(token=config.tg_bot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher(bot)

    # регистраци всех хэндлеров
    register_all_handlers(dp)

    # запускаем polling
    try:
        dp.skip_updates()   # пропуск накопленных, за время отсутствия бота в сети, апдейтов
        await dp.start_polling()
    finally:
        await bot.close()

if __name__ == '__main__':
    try:
        # запуск функции main
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        # вывод в консоль сообщение об ошибке
        # при получении исключения KeyboardInterrupt или SystemExit
        logger.error('Bot stopped!')
