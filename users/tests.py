import json
import jwt

from django.test import TestCase, Client

from users.models          import User
from eightpercent.settings import SECRET_KEY, ALGORITHM

class Test(TestCase):
    def setUp(self):
        User.objects.bulk_create([
            User(
                id       = 1,
                name     = 'test1',
                email    = 'test1@naver.com',
                password = "1234"
            ),
            User(
                id       = 2,
                name     = 'test2',
                email    = 'test2@naver.com',
                password = "3333"
            ),
            User(
                id       = 3,
                name     = 'test3',
                email    = 'test3@naver.com',
                password = "2222"
            ),
            User(
                id       = 4,
                name     = 'test4',
                email    = 'test4@naver.com',
                password = "4444"
            ),
            User(
                id       = 5,
                name     = 'test5',
                email    = 'test5@naver.com',
                password = "5555"
            )
        ])
    
    def tearDown(self):
        User.objects.all().delete()
    
    def test_success_signin(self):
        client = Client()
        data   = {
            "id"       : 1,
            "email"    : "test1@naver.com",
            "password" : "1234"
        }
        access_token = jwt.encode({"id": data['id']}, SECRET_KEY, algorithm=ALGORITHM)
        response     = client.post('/users/signin', json.dumps(data), content_type='applications/json')

        self.assertEqual(response.json(),
            {
                "token": access_token
            }
        )
        self.assertEquals(response.status_code,201)
    
    def test_fail_do_not_exist_email_signin(self):
        client = Client()
        data   = {
            "id"       : 2,
            "email"    : "amwg@naver.com",
            "password" : "4125"
        }

        response = client.post('/users/signin', json.dumps(data), content_type='applications/json')

        self.assertEqual(response.json(),
            {
                "message": "INVALID_EMAIL!"
            }
        )
        self.assertEquals(response.status_code,401)
    
    def test_fail_wrong_password_in_signin(self):
        client = Client()
        data   = {
            "id"       : 2,
            "email"    : "test2@naver.com",
            "password" : "412asd5"
        }

        response = client.post('/users/signin', json.dumps(data), content_type='applications/json')

        self.assertEqual(response.json(),
            {
                "message": "INVALID_PASSWORD!"
            }
        )
        self.assertEquals(response.status_code,401)

    def test_fail_key_error_in_signin(self):
        client = Client()
        data     = {}
        response = client.post('/users/signin', json.dumps(data), content_type='applications/json')

        self.assertEqual(response.json(),
            {
                "message": "KEY_ERROR"
            }
        )
        self.assertEquals(response.status_code,400)