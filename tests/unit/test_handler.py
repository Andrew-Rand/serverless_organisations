import json
import time

import pytest

from organizations.user.create import app
from .testing_db import db


@pytest.fixture()
def fixture_event():
    return {
        "body": "{\"first_name\": \"John\", \"last_name\": \"Golt\", "
                "\"email\": \"whoisjohngolt" + str(time.time_ns()) + "@gmail.com\", \"password\": \"1111\"}"
    }


class TestRegistrationAPI:
    def test_lambda_handler(self, fixture_event):
        result = app.lambda_handler(fixture_event, '')
        data = json.loads(result['body'])

        assert result['statusCode'] == 201
        assert 'message' in result['body']
        assert data['message'] == 'Registered Successfully'


    def teardown(self):

        # run after test and delete test record from database

        mongo = db.MongoDBConnection()
        with mongo:
            database = mongo.connection['myDB']
            collection = database['registrations']

            # Get last inserted id
            queryset = collection.find().sort([("_id", -1)]).limit(1)
            for result in queryset:
                result_id = result["_id"]

            # drop last inserted id
            collection.delete_one({"_id": result_id})
