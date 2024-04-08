import json
from unittest import TestCase
from unittest.mock import Mock, patch
from faker import Faker
import uuid
from src.main import app
from datetime import datetime, timedelta


class Emails_Test(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = app.test_client()

    def test_create(self):
        email = {
            'email': self.faker.email(),
            'app_id': str(uuid.uuid4()),
            'motivo': self.faker.text(),
        }
        response = self.test_client.post('/blacklists', data=json.dumps(email),
        headers={'Content-Type': 'application/json',
                                                  "Authorization": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJpYXQiOjE1OTYwNzYwMjJ9.7'})
        print(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
    