import logging
import os
import sys
import time
from encodings import utf_8


#创建日志的方法，和配置收集器
def get_logger():
    #给新建的日志收集器取名
    logger =logging.getLogger('FakeStore_AutoTest')
    #防止重复配置，同时给刚创建的日志收集器进行配置
    if not logger.handlers:
        #配置日志收集的级别
        logger.setLevel(logging.INFO)
        #配置收集后输出的格式，这里是{时间}
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')


        #创建写入控制台的渠道
        console_handler =  logging.StreamHandler()
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

        #创建写入到文件的渠道
        log_dir = "logs"
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)

        #配置文件名格式
        log_file = os.path.join(log_dir, f"test_{time.strftime('%Y%m%d')}.log")
        file_handler = logging.FileHandler(log_file,encoding='utf-8')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        return logger