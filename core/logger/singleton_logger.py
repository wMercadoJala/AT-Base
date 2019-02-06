# -*- coding: utf-8 -*-
import logging
import os
import datetime
from pathlib import Path


class SingletonType(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonType, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class SingletonLogger(object, metaclass=SingletonType):
    _logger = None

    def __init__(self):
        """
        This method is to initialize logger.
        """
        self._logger = logging.getLogger("crumbs")
        self._logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s \t [%(levelname)s] | %(filename)s:%(lineno)s] > %(message)s')

        now = datetime.datetime.now()
        current_dir = str(Path().absolute())

        dir_name = "{}/log".format(current_dir)
        if not os.path.isdir(dir_name):
            os.mkdir(dir_name)
        file_handler = logging.FileHandler(dir_name + "/todo.ly_" + now.strftime("%Y-%m-%d") + ".log")

        stream_handler = logging.StreamHandler()

        file_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)

        self._logger.addHandler(file_handler)
        self._logger.addHandler(stream_handler)

    def get_logger(self):
        """
        This method is to get logger.
        @:return logger.
        """
        return self._logger
