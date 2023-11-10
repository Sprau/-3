import requests

class APITest:
    def __init__(self, base_url):
        self.base_url = base_url

    def get_user(self, user_id):
        url = f"{self.base_url}/user/{user_id}"
        response = requests.get(url)
        return response

    def create_user(self, user_data):
        url = f"{self.base_url}/user"
        response = requests.post(url, json=user_data)
        return response

    def update_user(self, user_id, updated_data):
        url = f"{self.base_url}/user/{user_id}"
        response = requests.put(url, json=updated_data)
        return response

    def delete_user(self, user_id):
        url = f"{self.base_url}/user/{user_id}"
        response = requests.delete(url)
        return response

    def get_store(self, store_id):
        url = f"{self.base_url}/store/{store_id}"
        response = requests.get(url)
        return response

    def create_store(self, store_data):
        url = f"{self.base_url}/store"
        response = requests.post(url, json=store_data)
        return response

    def update_store(self, store_id, updated_data):
        url = f"{self.base_url}/store/{store_id}"
        response = requests.put(url, json=updated_data)
        return response

    def delete_store(self, store_id):
        url = f"{self.base_url}/store/{store_id}"
        response = requests.delete(url)
        return response

# Пример использования
base_url = "https://petstore.swagger.io/"
api_test = APITest(base_url)

# Тестирование сущности "user"
user_id = 1
user_data = {"username": "john_doe", "email": "john@example.com"}
updated_user_data = {"username": "john_doe_updated", "email": "john_updated@example.com"}

response = api_test.get_user(user_id)
print(response.json())

response = api_test.create_user(user_data)
print(response.json())

response = api_test.update_user(user_id, updated_user_data)
print(response.json())

response = api_test.delete_user(user_id)
print(response.status_code)

# Тестирование сущности "store"
store_id = 1
store_data = {"name": "Example Store", "location": "City Center"}
updated_store_data = {"name": "Updated Store", "location": "New Location"}

response = api_test.get_store(store_id)
print(response.json())

response = api_test.create_store(store_data)
print(response.json())

response = api_test.update_store(store_id, updated_store_data)
print(response.json())

response = api_test.delete_store(store_id)
print(response.status_code)