import logging


class Logger:

    @staticmethod
    def create_info_log(data):
        return logging.info(data)

    @staticmethod
    def log_exception(error):
        return logging.exception(error)
