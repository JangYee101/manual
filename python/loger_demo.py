#coding: utf-8
import os
import logging
import logging.handlers
log_file = 'my.log'
log_file = ''

logger = logging.getLogger('JY')
logger.setLevel(level = logging.DEBUG)
#日志文件大小最大为1024k，文件个数最多4个，my.log存放最新日志，my.log4存放最旧日志
if log_file != '':
    handler = logging.handlers.RotatingFileHandler(log_file, maxBytes=1024, backupCount=3)
else:#调试模式，打印到终端
    handler = logging.StreamHandler()

fmt = '%(message)s'
formatter = logging.Formatter(fmt)
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.debug('test')

