from utils.response_saver import save_response_to_file as sa
import requests


class API:
    base_url = "https://reqres.in/api"

    def get(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        print(f"\nGET request to {url}")
        response = requests.get(url)
        print(f"Response status code: {response.status_code}")
        sa(response, 'api_response.json')
        return response


    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        print(f"\nPOST request to {url}")
        response = requests.post(url, data=data)
        print(f"Response status code: {response.status_code}")
        sa(response, 'api_response.json')
        return response

    def put(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        print(f"\nPUT request to {url}")
        response = requests.put(url, data=data)
        print(f"Response status code: {response.status_code}")
        sa(response, 'api_response.json')
        return response

    def patch(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        print(f"\nPATCH request to {url}")
        response = requests.patch(url, data=data)
        print(f"Response status code: {response.status_code}")
        sa(response, 'api_response.json')
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}/{endpoint}"
        print(f"\nPATCH request to {url}")
        response = requests.delete(url)
        print(f"Response status code: {response.status_code}")
        sa(response, 'api_response.json')
        return response




    def assert_status_code(self, response, expected_status_code):
        assert response.status_code == expected_status_code
