import json
from unittest import TestCase
from faker import Faker
import uuid
from application import application


class ControllerTest(TestCase):
    def setUp(self):
        self.faker = Faker()
        self.test_client = application.test_client()

    def test_create(self):
        email = {
            'email': self.faker.email(),
            'app_uuid': str(uuid.uuid4()),
            'blocked_reason': self.faker.text(),
        }
        response = self.test_client.post(
            '/blacklists',
            data=json.dumps(email),
            headers={'Content-Type': 'application/json', 'Authorization': '40797d32-4825-4391-a2c3-051ab9e79a77'})
        self.assertEqual(response.status_code, 201)
        self.assertIsNotNone(json.loads(response.get_data())['id'])
        self.assertIsNotNone(json.loads(response.get_data())['createdAt'])
