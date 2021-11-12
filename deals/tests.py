import json
import jwt

from django.test  import (
    TestCase, 
    Client,
)

from users.models import User
from deals.models import (
    Bank,
    Account,
    DealPosition,
    Deal2021,
)

from eightpercent.settings import (
    SECRET_KEY, 
    ALGORITHM
)

class DealViewTest(TestCase) :
    def setUp(self) :
        global headers1, headers2, deal1, deal2, deal3, deal4
        
        user1          = User.objects.create(id=1, name='test1', email='test1@gmail.com', password='test')
        user2          = User.objects.create(id=2, name='test2', email='test2@gmail.com', password='test')
        
        access_token1  = jwt.encode({'user_id':1}, SECRET_KEY, ALGORITHM)
        access_token2  = jwt.encode({'user_id':2}, SECRET_KEY, ALGORITHM)
        
        headers1       = {'HTTP_Authorization' : access_token1}
        headers2       = {'HTTP_Authorization' : access_token2}
        
        bank1          = Bank.objects.create(id=1, name='에잇퍼센트은행')
        bank2          = Bank.objects.create(id=2, name='위코드은행')
        
        account1       = Account.objects.create(id=1, owner=user1, bank=bank1, number='194213023', balance=50000)
        account2       = Account.objects.create(id=2, owner=user2, bank=bank2, number='3942148201', balance=100000)
        
        deal_position1 = DealPosition.objects.create(id=1, position='입금')
        deal_position2 = DealPosition.objects.create(id=2, position='출금')
        
        deal1          = Deal2021.objects.create(id=1, account=account1, deal_position=deal_position1, amount=10000, balance=account1.balance+10000, description='입금입니다')
        deal2          = Deal2021.objects.create(id=2, account=account1, deal_position=deal_position2, amount=10000, balance=account1.balance-10000, description='출금입니다')
        deal3          = Deal2021.objects.create(id=3, account=account1, deal_position=deal_position1, amount=10000, balance=account1.balance+10000, description='입금입니다')
        deal4          = Deal2021.objects.create(id=4, account=account1, deal_position=deal_position1, amount=10000, balance=account1.balance+10000, description='입금입니다')
        
    def tearDown(self) :
        User.objects.all().delete()
        Bank.objects.all().delete()
        Account.objects.all().delete()
        DealPosition.objects.all().delete()
        Deal2021.objects.all().delete()
    
    def test_deal_post_success(self):
        client = Client()
        
        deal_info = {
            'deal_position_id' : 1,
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/1', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{
            'before_balance': 50000, 'after_balance': 51000
        })
    
    def test_deal_post_key_error(self):
        client = Client()
        
        deal_info = {
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/1', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{
            'message' : 'KEY_ERROR'
        })
    
    def test_deal_post_account_does_not_exist(self):
        client = Client()
        
        deal_info = {
            'deal_position_id' : 1,
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/3', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            'message' : 'ACCOUNT_DOES_NOT_EXIST'
        })

    def test_deal_post_invalid_deal_position_id(self):
        client = Client()
        
        deal_info = {
            'deal_position_id' : 3,
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/1', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_DEAL_POSITION_ID'
        })

    def test_deal_post_account_does_not_exist(self):
        client = Client()
        
        deal_info = {
            'deal_position_id' : 1,
            'amount'           : 0,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/1', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_AMOUNT'
        })

    def test_deal_post_invalid_account_id(self):
        client = Client()
        
        deal_info = {
            'deal_position_id' : 1,
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/1', json.dumps(deal_info), content_type='application/json', **headers2)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_ACCOUNT_ID'
        })

    def test_deal_post_insufficient_balance(self):
        client = Client()
        
        deal_info = {
            'deal_position_id' : 2,
            'amount'           : 100000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/1', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INSUFFICIENT_BALANCE'
        })

    def test_deal_post_json_decode_error(self):
        client = Client()
        
        response = client.post('/deals/1', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'JSON_DECODE_ERROR'
        })
    
    def test_deal_post_unknown_user(self):
        client = Client()
        
        deal_info = {
            'deal_position_id' : 1,
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals/1', json.dumps(deal_info), content_type='application/json')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(),{
            'message' : 'UNKNOWN_USER'
        })
    
    def test_deal_get_success(self):
        client = Client()
        
        data = [{
                'id'            : 1,
                'deal_position' : '입금',
                'deal_date'     : deal1.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'deal_amount'   : 10000,
                'deal_balance'  : 60000,
                'description'   : '입금입니다',
                },
                {
                'id'            : 2,
                'deal_position' : '출금',
                'deal_date'     : deal2.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'deal_amount'   : 10000,
                'deal_balance'  : 40000,
                'description'   : '출금입니다',
                },
                {
                'id'            : 3,
                'deal_position' : '입금',
                'deal_date'     : deal3.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'deal_amount'   : 10000,
                'deal_balance'  : 60000,
                'description'   : '입금입니다',
                },
                {
                'id'            : 4,
                'deal_position' : '입금',
                'deal_date'     : deal4.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'deal_amount'   : 10000,
                'deal_balance'  : 60000,
                'description'   : '입금입니다',
                }]
        
        response = client.get('/deals/1?start_date=2021-11-10&end_date=2021-11-12&sort=old', **headers1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'data' : data
        })

    def test_deal_get_success_deal_position_filter(self):
        client = Client()
        
        data = [{
                'id'            : 1,
                'deal_position' : '입금',
                'deal_date'     : deal1.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'deal_amount'   : 10000,
                'deal_balance'  : 60000,
                'description'   : '입금입니다',
                },
                {
                'id'            : 3,
                'deal_position' : '입금',
                'deal_date'     : deal3.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'deal_amount'   : 10000,
                'deal_balance'  : 60000,
                'description'   : '입금입니다',
                },
                {
                'id'            : 4,
                'deal_position' : '입금',
                'deal_date'     : deal4.created_at.strftime('%Y-%m-%d %H:%M:%S'),
                'deal_amount'   : 10000,
                'deal_balance'  : 60000,
                'description'   : '입금입니다',
                }]
        
        response = client.get('/deals/1?start_date=2021-11-10&end_date=2021-11-12&sort=old&deal_position_id=1', **headers1)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {
            'data' : data
        })

def test_deal_get_account_does_not_exist(self):
        client = Client()
        
        response = client.get('/deals/3?start_date=2021-11-10&end_date=2021-11-12&sort=old&deal_position_id=1', **headers1)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json(), {
            'message' : 'ACCOUNT_DOES_NOT_EXIST'
        })

def test_deal_get_invalid_account_id(self):
        client = Client()
        
        response = client.get('/deals/2?start_date=2021-11-10&end_date=2021-11-12&sort=old&deal_position_id=1', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_ACCOUNT_ID'
        })

def test_deal_get_key_error(self):
        client = Client()
        
        response = client.get('/deals/1?start_date=2021-11-10&sort=&deal_position_id=1', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'KEY_ERROR'
        })

def test_deal_get_invalid_deal_position_id(self):
        client = Client()
        
        response = client.get('/deals/1?start_date=2021-11-10&end_date=2021-11-12&sort=&deal_position_id=3', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_DEAL_POSITION_ID'
        })

def test_deal_get_invalid_date(self):
        client = Client()
        
        response = client.get('/deals/1?start_date=2021-11-10&end_date=123123123123&sort=&deal_position_id=1', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'INVALID_DATE'
        })

def test_deal_get_unknown_user(self):
        client = Client()
        
        response = client.get('/deals/1?start_date=2021-11-10&end_date=2021-11-12&sort=&deal_position_id=1')
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.json(), {
            'message' : 'UNKNOWN_USER'
        })