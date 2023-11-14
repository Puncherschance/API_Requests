import pytest
from methods import *


@pytest.fixture()
def api():
    api = Api()
    return api


@pytest.fixture()
def fake():
    fake = Fake()
    return fake


@pytest.fixture()
def write_log():
    def log(res):
        logger.create_info_log(f"Status Code = {res.status_code}")
        logger.create_info_log(res.text)
        logger.create_info_log("Test completed!")
        return res
    logger = Logger()
    logger.create_info_log("Starting test!")
    return log
