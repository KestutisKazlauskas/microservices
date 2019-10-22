
import json
import unittest

from app.tests.base import BaseTestCase

class TestUserService(BaseTestCase):

    def test_users(self):
        response = self.client.get('/users/ping/')

        data = json.loads(response.data.decode())
        self.assertEqual(response.status_code, 200)
        self.assertIn('pong', data['message'])
        self.assertIn('success', data['status'])

    def test_create_user(self):
        """Test user creation to the database"""
        request_data = {
            'username': 'kestutis',
            'email': 'kestutis@test.com'
        }
        with self.client:
            response = self.client.post(
                '/users/',
                data=json.dumps(request_data),
                content_type='application/json'
            )
            data = json.loads(response.data.decode())
            # check if response is created
            self.assertEqual(response.status_code, 201)
            # check all data values
            for key in request_data:
                self.assertIn(data[key], request_data[key])

    def test_required_data_send(self):
        """Test validation without a required data"""
        required_data = {
            'username': 'kestutis',
            'email': 'kestutis@test.com'
        }
        with self.client:
            for key in required_data:

                data = required_data.copy()
                del data[key]

                response = self.client.post(
                    '/users/',
                    data=json.dumps(data),
                    content_type='application/json'
                )
                data = json.loads(response.data.decode())
                
                self.assertEqual(response.status_code, 400)
                self.assertEqual(data['message'], f'{key} is required!')

    def test_incorrect_email(self):
        pass

    def test_duplicated_user_by_email(self):
        pass

if __name__ == '__main__':
    unittest.main()