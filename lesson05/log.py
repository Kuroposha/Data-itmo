import logging
# дебаггинг - может принтить на экран и в файл

formatt = '[%(levelname)s] %(asctime).19s [%(filename)s:%(lineno)d] %(messege)s'

logging.basicConfig(
    level=logging.DEBUG,
    format=formatt
)

logger = logging.getLogger()

logger.info('Информационное сообщение')
