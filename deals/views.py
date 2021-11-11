import json

from django.views     import View
from django.http      import JsonResponse
from django.db        import transaction
from django.db.utils  import IntegrityError

from enum             import Enum

from users.models     import User
from deals.models     import (
    Account,
    Bank,
    Deal, 
    DealPosition
)
from users.utils      import login_decorator

class DealPositionInfo(Enum) :
    입금 = 1
    출금 = 2

class BankInfo(Enum) :
    신한은행 = 1
    기업은행 = 2
    하나은행 = 3
    국민은행 = 4

class CheckError() :
    def check_bank_id(bank_id) :
        if not Bank.objects.filter(id = bank_id).exists() :
            raise Bank.DoesNotExist
    
    def check_deal_position_id(deal_position_id) :
        if not DealPosition.objects.filter(id = deal_position_id).exists() :
            raise DealPosition.DoesNotExist
    
    def check_account_id(account_id) :
        if not Account.objects.filter(id = account_id).exists() :
            raise Account.DoesNotExist

    def check_amount_for_deal(amount) :
        if amount <= 0 :
            raise IntegrityError
    
class DealView(View) :
    @login_decorator
    def post(self, request) :
        try :
            data = json.loads(request.body)

            with transaction.atomic() :
                
                bank_id          = data['bank_id']
                deal_position_id = data['deal_position_id']
                account_id       = data['account_id']
                amount           = data['amount']
                description      = data['description']
                
                CheckError.check_bank_id(bank_id)
                CheckError.check_deal_position_id(deal_position_id)
                CheckError.check_account_id(account_id)
                CheckError.check_amount_for_deal(amount)
                
                account = Account.objects.get(id = account_id)
                
                if deal_position_id == 1 :
                    last_balance    = account.balance + amount
                    account.balance = last_balance
                    account.save()
                
                if deal_position_id == 2 :
                    if amount > account.balance :
                        return JsonResponse({'message' : 'CANNOT_REQUEST_EXCEED_BALANCE'}, status=400)
                    
                    last_balance    = account.balance - amount
                    account.balance = last_balance
                    account.save()
            
            Deal.objects.create(
                account_id       = account_id,
                deal_position_id = deal_position_id,
                amount           = amount,
                description      = description,
                balance          = last_balance
            )
            
            return JsonResponse({'message' : 'SUCCESS'}, status=201)
                   
        except KeyError :
            return JsonResponse({'message' : 'KEY_ERROR'}, status=400)