from django.db import models

class Bank(models.Model):
    name = models.CharField(max_length = 50, unique = True)

    class Meta:
        db_table = 'banks'

class Account(models.Model):
    owner   = models.ForeignKey('users.User', on_delete = models.CASCADE)
    bank    = models.ForeignKey('Bank', on_delete = models.CASCADE)
    number  = models.CharField(max_length = 100, unique = True)
    balance = models.PositiveBigIntegerField(default = 0)
    
    class Meta:
        db_table = 'accounts'
    
    def __str__(self):
        return self.number

class DealPosition(models.Model):
    position = models.CharField(max_length = 50)
    
    class Meta:
        db_table = 'deal_positions'
    
    def __str__(self):
        return self.position

class Deal(models.Model):
    account       = models.ForeignKey('Account', on_delete = models.CASCADE)
    deal_position = models.ForeignKey('DealPosition', on_delete = models.CASCADE)
    amount        = models.PositiveBigIntegerField()
    created_at    = models.DateTimeField(auto_now_add = True, db_index = True)
    balance       = models.PositiveBigIntegerField()
    description   = models.CharField(max_length = 100)
    
    class Meta:
        db_table = 'deals'