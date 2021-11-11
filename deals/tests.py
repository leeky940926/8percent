import json
from django.http import response
import jwt

from django.test  import (
    TestCase, 
    Client,
    client
)

from users.models import User
from deals.models import (
    Bank,
    Account,
    DealPosition,
    Deal
)

from eightpercent.settings import (
    SECRET_KEY, 
    ALGORITHM
)

class DealViewTest(TestCase) :
    def setUp(self) :
        global headers1, headers2
        
        user1          = User.objects.create(id=1, name='test1', email='test1@gmail.com', password='test')
        user2          = User.objects.create(id=2, name='test2', email='test2@gmail.com', password='test')
        
        access_token1  = jwt.encode({'id':1}, SECRET_KEY, ALGORITHM)
        access_token2  = jwt.encode({'id':2}, SECRET_KEY, ALGORITHM)
        
        headers1       = {'HTTP_Authorization' : access_token1}
        headers2       = {'HTTP_Authorization' : access_token2}
        
        bank1          = Bank.objects.create(id=1, name='에잇퍼센트은행')
        bank2          = Bank.objects.create(id=2, name='위코드은행')
        
        account1       = Account.objects.create(id=1, owner=user1, bank=bank1, number='194213023', balance=50000)
        account2       = Account.objects.create(id=2, owner=user2, bank=bank2, number='3942148201', balance=100000)
        
        deal_position1 = DealPosition.objects.create(id=1, position='입금')
        deal_position2 = DealPosition.objects.create(id=2, position='출금')
        
        deal1          = Deal.objects.create(id=1, account=account1, deal_position=deal_position1, amount=10000, balance=account1.balance+10000, description='입금입니다')
        deal2          = Deal.objects.create(id=2, account=account2, deal_position=deal_position2, amount=10000, balance=account2.balance-10000, description='출금입니다')
        
    def tearDown(self) :
        User.objects.all().delete()
        Bank.objects.all().delete()
        Account.objects.all().delete()
        DealPosition.objects.all().delete()
        Deal.objects.all().delete()
    
    def test_success_transfer_deal(self) :
        client = Client()
        
        deal_info = {
            'bank_id'          : 1,
            'deal_position_id' : 1,
            'account_id'       : 1,
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json(),{
            'message' : 'SUCCESS'
        })
    
    def test_failure_caused_key_error(self) :
        client = Client()
        
        deal_info = {
            'bank_iddddd'      : 1,
            'deal_position_id' : 1,
            'account_id'       : 1,
            'amount'           : 1000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(),{
            'message' : 'KEY_ERROR'
        })
    
    def test_failure_caused_amount_exceed_balance(self) :
        client = Client()
        
        deal_info = {
            'bank_id'          : 1,
            'deal_position_id' : 2,
            'account_id'       : 1,
            'amount'           : 100000000,
            'description'      : 'hihi'   
        }
        
        response = client.post('/deals', json.dumps(deal_info), content_type='application/json', **headers1)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'message' : 'CANNOT_REQUEST_EXCEED_BALANCE'
        })