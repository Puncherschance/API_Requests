from jsonschema import validate
import requests
import allure
import json
from faker import Faker
from log import Logger
import os.path
from config import BASE_DIR


class Api:

    @staticmethod
    def send_get_request(url):
        with allure.step("Send GET request to Server."):
            return requests.get(url)

    @staticmethod
    def send_post_request(url, data):
        with allure.step("Send POST request to Server."):
            headers = {"Content-type": "application/json; charset=UTF-8"}
            return requests.post(url, data=data, headers=headers)

    @staticmethod
    def send_put_request(url, data):
        with allure.step("Send PUT request to Server."):
            headers = {"Content-type": "application/json; charset=UTF-8"}
            return requests.put(url, data=data, headers=headers)

    @staticmethod
    def send_patch_request(url, data):
        with allure.step("Send PATCH request to Server."):
            headers = {"Content-type": "application/json; charset=UTF-8"}
            return requests.patch(url, data=data, headers=headers)

    @staticmethod
    def send_delete_request(url):
        with allure.step("Send DELETE request to Server."):
            return requests.delete(url)

    @staticmethod
    def text_to_json(text):
        return json.loads(text)

    @staticmethod
    def patch_title():
        return json.dumps({"title": "PATCHED!"})

    @staticmethod
    def load_schema(file_name):
        path = os.path.join(BASE_DIR, 'scheme', file_name)
        with open(path) as file:
            return json.loads(file.read())

    @staticmethod
    def validate_schema(res):
        with allure.step("Validate received JSON Schema."):
            def compare(res):
                try:
                    api = Api()  # как убрать?
                    validate(api.text_to_json(res.text), api.load_schema("get_specific_post.json"))
                    return True
                except Exception:
                    logger = Logger()  # как убрать?
                    logger.log_exception(error_message)
                    return False
            error_message = "Json is incorrect!"
            assert compare(res), error_message

    @staticmethod
    def validate_status_code(actual, expected):
        with allure.step("Validate received Status Code."):
            def compare(actual, expected):
                try:
                    assert actual.status_code == expected
                    return True
                except Exception:
                    logger = Logger()  # как убрать?
                    logger.log_exception(error_message)
                    return False
            error_message = f"Status Code {actual.status_code} is not equal with {expected}!"
            assert compare(actual, expected), error_message


class Fake:

    @staticmethod
    def generate_fake_data(user_id=1, post_id=1):
        fake = Faker()
        return json.dumps({"title": fake.city(), "body": fake.text(), "id": post_id, "userId": user_id})
