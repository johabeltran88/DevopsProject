import json
from unittest import TestCase
from unittest.mock import patch
from faker import Faker
import uuid
from src.main import app
from datetime import datetime, timedelta


class Emails_Test(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    #@patch('src.commons.validation_util.requests.get')
    def test_create(self, mocked_get):
        mocked_get.return_value.status_code = 200
        email = {
            'email': self.faker.email(),
            'app_id': str(uuid.uuid4()),
            'motivo': self.faker.text(),
        }
        response = self.test_client.post('/blacklists', data=json.dumps(email),
        headers={'Content-Type': 'application/json',
                                                  "Authorization": 'Valid Token'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertIsNotNone(json.loads(response.get_data())['createdAt'])

    