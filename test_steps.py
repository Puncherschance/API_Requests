import pytest
import allure
from env import *


@pytest.mark.GET
@allure.feature("GET Requests")
class TestGetRequests:

    @allure.story("GET all available Posts")
    def test_get_all_posts(self, api, write_log):
        res = api.send_get_request(Env.url)
        api.validate_status_code(res, 200)
        write_log(res)

    @allure.story("GET the specific Post")
    @pytest.mark.parametrize("post_id", ("1", "2", "3", "4", "5"))
    def test_get_specific_post(self, api, post_id, write_log):
        res = api.send_get_request(Env.url+post_id)
        api.validate_status_code(res, 200)
        api.validate_schema(res)
        write_log(res)


@pytest.mark.POST
@allure.feature("POST Requests")
class TestPostRequests:

    @allure.story("POST new Post")
    @pytest.mark.parametrize("user_id", (1, 2, 3, 4, 5))
    def test_post_new_post(self, api, fake, user_id, write_log):
        fake_data = fake.generate_fake_data(user_id=user_id)
        res = api.send_post_request(Env.url, fake_data)
        api.validate_status_code(res, 201)
        api.validate_schema(res)
        write_log(res)


@pytest.mark.PUT
@allure.feature("PUT Requests")
class TestPutRequests:

    @allure.story("PUT in the specific Post")
    @pytest.mark.parametrize("post_id", ("1", "2", "3", "4", "5"))
    def test_put_in_post(self, api, fake, post_id, write_log):
        fake_data = fake.generate_fake_data(post_id=int(post_id))
        res = api.send_put_request(Env.url+post_id, fake_data)
        api.validate_status_code(res, 200)
        api.validate_schema(res)
        write_log(res)


@pytest.mark.PATCH
@allure.feature("PATCH Requests")
class TestPatchRequests:

    @allure.story("PATCH the specific Post")
    @pytest.mark.parametrize("post_id", ("1", "2", "3", "4", "5"))
    def test_patch_post(self, api, post_id, write_log):
        patched_title = api.patch_title()
        res = api.send_patch_request(Env.url+post_id, data=patched_title)
        api.validate_status_code(res, 200)
        api.validate_schema(res)
        write_log(res)


@pytest.mark.DELETE
@allure.feature("DELETE Requests")
class TestDeleteRequests:

    @allure.story("DELETE the specific Post")
    @pytest.mark.parametrize("post_id", ("1", "2", "3", "4", "5"))
    def test_delete_post(self, api, post_id, write_log):
        res = api.send_delete_request(Env.url+post_id)
        api.validate_status_code(res, 200)
        write_log(res)
