import json

import config as config
# from config import db, app
import controller.beast_controller
import utils.database_reset as db_restart
from tests import Beast_test, Ability_test, Plan_test, User_test
import requests

# db_restart.reset_db(db, app)
json_string = []
GET_sequence =[]
POST_sequence = []
UPD_sequence = []


# Beast tests
json_string.append('{ "name": "testName", "source": "TestSource", "description": "testDescription","stat_block": "test stats block", "token":"1256"}')
GET_sequence.append( Beast_test.GET )
POST_sequence.append( Beast_test.POST )
UPD_sequence.append( Beast_test.UPD )

'''
# Ability tests
json_string.append('{ "mechanics": "testMechanics","name": "testName","short_description": "testDescription", "token":"1256" }')
GET_sequence.append( Ability_test.GET )
POST_sequence.append( Ability_test.POST )
UPD_sequence.append( Ability_test.UPD )


# Plan tests
json_string.append('{"monthly_allowance": 55,"name": "testName","price": 5.5, "token":"1256"}')
GET_sequence.append( Plan_test.GET )
POST_sequence.append( Plan_test.POST )
UPD_sequence.append( Plan_test.UPD )


# User tests
json_string.append('{"name": "testName","password": "TestPassword","plan_id": 2, "token":"1256"}')
GET_sequence.append( User_test.GET )
POST_sequence.append( User_test.POST )
UPD_sequence.append( User_test.UPD )
'''


def run_tests():
    print('test run stated')
    i = 0
    for test in GET_sequence:
        json_data = json.loads(json_string[i])
        i += 1
        print("Testing GETs")
        for call in test:
            # try to find a way to make the proper loop of all request considering some are del/update/post or just get
            # maybe do a list for all four in each file.

            try:
                response = requests.get(call)
                response.raise_for_status()  # Raise an exception for HTTP errors
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"An error occurred: {err}")

    i = 0
    for test in POST_sequence:
        print('Testing POSTs')
        json_data = json.loads(json_string[i])
        i += 1
        for call in test:
            try:
                headers = {'Content-Type': 'application/json'}
                response = requests.post(call, json=json_data, headers=headers)
                response.raise_for_status()  # Raise an exception for HTTP errors
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"An error occurred: {err}")

    i = 0
    for test in UPD_sequence:
        print('Testing UPDATEs')
        json_data = json.loads(json_string[i])
        i += 1
        for call in test:
            try:
                response = requests.put(call, json=json_data, headers=headers)
                response.raise_for_status()  # Raise an exception for HTTP errors
                print(f"Response Status Code: {response.status_code}")
                print(f"Response Body: {response.text}")
            except requests.exceptions.HTTPError as http_err:
                print(f"HTTP error occurred: {http_err}")
            except Exception as err:
                print(f"An error occurred: {err}")

if __name__ == '__main__':
#   config.app.run(debug=True, port='5600')
    print('strating test_run')
    run_tests()