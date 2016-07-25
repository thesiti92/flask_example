import requests, time
user1 = {"first_name": "Becky", "last_name": "GoodHair",
        "age": "27", "email": "becky@goodhair.com"}
user2 = {"first_name": "Harnek", "last_name": "Gulati",
        "age": "96", "email": "xxchipotlegawdxx@gmail.com"}
user3 = {"first_name": "Bill", "last_name": "Gates",
        "age": "62", "email": "moneymoney123@gatesfoundation.com"}
url = "http://localhost:5000/sendUser"
response = requests.post(url, json=user1)
print(response.text)
time.sleep(1)
response = requests.post(url, json=user2)
print(response.text)
time.sleep(1)
response = requests.post(url, json=user3)
print(response.text)
