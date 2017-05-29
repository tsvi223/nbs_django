from django.db import models

class accountLimited(models.Model):
    branch  = models.CharField(max_length = 20)
    bank = models.CharField(max_length = 20 , null = True)
    account = models.CharField(max_length = 20 , null = True)
    def __str__(self):
        
        return self.account
#
