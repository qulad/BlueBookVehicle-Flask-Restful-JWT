import requests

BASE = "http://localhost:5000/api/v1/"

headers = {
    "Content-Type": "application/json"
}
def user_register_test_1():
    data = {
        "email": "testcase1@example.com",
        "password1": "0123456789",
        "password2": "0123456789",
        "first_name": "asd",
        "last_name": "ss",
        "user_name": "testcase1",
        "phone_number": "1234",
        "profile_image_url": "static/images/no_picture_found.jpg",
        "birth_date": "2020-01-08T18:52:50.637635"
    }
    response = requests.post(BASE + "user/auth/register", json=data, headers=headers)
    if response.status_code == 201:
        print(f"TEST CASE 1:....................PASSED")
    else:
        print(f"TEST CASE 1:....................FAILED -> {response.status_code}")
        print(response.json())

def user_register_test_2():
    data = {
        "email": "testcase1@example.com",
        "password1": "0123456789",
        "password2": "0123456789",
        "first_name": "asd",
        "last_name": "ss",
        "user_name": "testcase1",
        "profile_image_url": "static/images/no_picture_found.jpg",
        "phone_number": "1234",
        "birth_date": "2020"
    }
    response = requests.post(BASE + "user/auth/register", json=data, headers=headers)
    if response.status_code == 409:
        print(f"TEST CASE 2:....................PASSED")
    else:
        print(f"TEST CASE 2:....................FAILED -> {response.status_code}")

def user_register_test_3():
    data = {
        "email": "testcase3@example.com",
        "password1": "0123456789",
        "password2": "asdasd",
        "first_name": "asd",
        "last_name": "ss",
        "user_name": "testcase3",
        "profile_image_url": "static/images/no_picture_found.jpg",
        "phone_number": "1234",
        "birth_date": "2020"
    }
    response = requests.post(BASE + "user/auth/register", json=data, headers=headers)
    if response.status_code == 400:
        print(f"TEST CASE 3:....................PASSED")
    else:
        print(f"TEST CASE 3:....................FAILED -> {response.status_code}")

def user_register_test_4():
    data = {
        "email": "testcase4@example.com",
        "password1": "0123456789",
        "password2": "0123456789",
        "first_name": "asd",
        "last_name": "ss",
        "user_name": "testcase3",
        "profile_image_url": "static/images/no_picture_found.jpg",
        "phone_number": "1234",
        "birth_date": "2020"
    }
    response = requests.post(BASE + "user/auth/register", json=data, headers=headers)
    if response.status_code == 409:
        print(f"TEST CASE 4:....................PASSED")
    else:
        print(f"TEST CASE 4:....................FAILED -> {response.status_code}")
