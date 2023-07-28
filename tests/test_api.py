from utils.api import API
import logging


class TestAPI(API):
    def test_get_list_users(self):
        logging.info("1. Test Get List Users")
        response = self.get(f"users?page=2")
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 200)

    def test_get_single_user(self):
        logging.info("2. Test Get Single User")
        response = self.get("users/2")
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 200)

    def test_get_single_user_not_found(self):
        logging.info("3. Test Get Single User Not Found")
        response = self.get("users/23")
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 404)

    def test_get_list_resource(self):
        logging.info("4. Test Get List Resource")
        response = self.get("unknown")
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 200)

    def test_get_single_resource(self):
        logging.info("5. Test Get Single Resource")
        response = self.get("unknown/2")
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 200)

    def test_get_single_resource_not_found(self):
        logging.info("6. Test Get Single Resource Not Found")
        response = self.get("unknown/23")
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 404)

    def test_post_create(self):
        logging.info("7. Test Post Create")
        data = {
            "name": "morpheus",
            "job": "leader"
        }
        response = self.post("users", data=data)
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 201)

    def test_put_update(self):
        logging.info("8. Test Put Update")
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = self.put("users/2", data=data)
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 200)

    def test_patch_update(self):
        logging.info("9. Test Patch Update")
        data = {
            "name": "morpheus",
            "job": "zion resident"
        }
        response = self.patch("users/2", data=data)
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 200)

    def test_delete(self):
        logging.info("10. Test Delete")
        response = self.delete("users/2")
        self.assert_status_code(response, 204)

    def test_post_register_successful(self):
        logging.info("11. Test Post Register Successful")
        data = {
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }
        response = self.post("register", data=data)
        logging.info(f"Response status code: {response.status_code}")
        self.assert_status_code(response, 200)

    def test_post_register_unsuccessful(self):
       logging.info("12. Test Post Register Unsuccessful")
       data = {
           "email": "sydney@fife"
       }
       response = self.post("register", data=data)
       logging.info(f"Response status code: {response.status_code}")
       self.assert_status_code(response, 400)

    def test_post_login_successful(self):
       logging.info("13. Test Post Login Successful")
       data = \
        {
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }
       response = self.post("login", data=data)
       logging.info(f"Response status code: {response.status_code}")
       self.assert_status_code(response, 200)

    def test_post_login_unsuccessful(self):
       logging.info("14. Test Post Login Unsuccessful")
       data = \
        {
            "email": "peter@klaven"
        }
       response = self.post("login", data=data)
       logging.info(f"Response status code: {response.status_code}")
       self.assert_status_code(response, 400)

    def test_get_delayed_response(self):
       logging.info("15. Test Get Delayed Response")
       response = self.get("users?delay=3")
       logging.info(f"Response status code: {response.status_code}")
       self.assert_status_code(response, 200)
