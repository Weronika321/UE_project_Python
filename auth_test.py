import requests
import datetime

url = "https://postman-echo.com/basic-auth"
header = {"Authorization" : "Basic cG9zdG1hbjpwYXNzd29yZA=="}
response = requests.get(url, headers=header)
print(response.status_code)
print(response.json())
print(datetime.datetime.now().strftime('%H:%M:%S'))
