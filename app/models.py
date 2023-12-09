from django.db import models

# Create your models here.
class Country(models.Model):
    Country_Code=models.CharField(max_length=100,primary_key=True)
    Country_Name=models.CharField(max_length=100)
    Currency=models.CharField(max_length=100)

    

class Capital(models.Model):
    Country_Code=models.ForeignKey(Country,on_delete=models.CASCADE)
    Capital_ID=models.PositiveIntegerField(primary_key=True)
    Capital_Name=models.CharField(max_length=100)

    