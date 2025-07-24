import logging
from pythonjsonlogger.json import JsonFormatter

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

log_format = '%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s'


log_file_handler = logging.FileHandler('logs.json', 'w')

formatter = JsonFormatter(log_format)

log_file_handler.setFormatter(formatter)

logger.addHandler(log_file_handler)