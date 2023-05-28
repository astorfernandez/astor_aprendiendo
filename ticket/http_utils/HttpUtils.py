import requests


class HttpUtils:

    def get(self, url):
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data
        else:
            error_message = f"The request failed with the status: {response.status_code}"
            raise Exception(error_message)


