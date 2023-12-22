# recommendations/models.py
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    selected_services = models.ManyToManyField('Service', blank=True)

class Service(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# myapp/models.py
from django.db import models

class UserData(models.Model):
    Recent_Activities = models.IntegerField()
    Purchase_History = models.IntegerField()
    Account_Type = models.CharField(max_length=10)
    Money_on_Account = models.FloatField()
    Age = models.IntegerField()
    Monthly_Income = models.FloatField()
    Credit_Score = models.IntegerField()
    Number_of_Dependents = models.IntegerField()
    Education_Level = models.CharField(max_length=20)
    Gender = models.CharField(max_length=10)
    Services_Taken = models.CharField(max_length=100)


class FinancialService(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
