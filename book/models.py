from django.db import models
from django.utils.translation import gettext as _

class Book (models.Model):

  InvoiceID = models.CharField(max_length=100,null=True)
  Branch = models.CharField(max_length=255,null=True)
  City = models.CharField(max_length=255,null=True)
  Customer_type = models.CharField(max_length=300,null=True)
  Gender = models.CharField(max_length=300,null=True)
  Product_line= models.CharField(max_length=300,null=True)
  Unit_price= models.FloatField(max_length=20,null=True)
  Quantity =  models.IntegerField(null=True)
  Tax =  models.IntegerField(null=True)
  Total =  models.IntegerField(null=True)
  Date= models.DateField(null=True)
  Time = models.TimeField(null=True)
  Payment = models.CharField(max_length=255,null=True)
  cogs = models.FloatField(max_length=20,null=True)
  groosmarginpercent = models.FloatField(null=True)
  grossincome = models.FloatField(null=True)
  Rating = models.FloatField(max_length=200,null=True)


  def __str__(self):
        return f"self.invoiceid"

class MOnthlyGrossIncome(models.Model):

  highestgrossincome = models.FloatField(null=True)


  def __str__(self) -> str:
     return self.highestgrossincome

