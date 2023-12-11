from django.db import models

# Create your models here.
class Country(models.Model):
    Country_Code=models.CharField(max_length=100,primary_key=True)
    Country_Name=models.CharField(max_length=100)
    

    def __str__(self):
        return self.Country_Code
    

class Capital(models.Model):
    Country_Code=models.OneToOneField(Country,on_delete=models.CASCADE)
    Capital_Name=models.CharField(max_length=100,primary_key=True)
    Currency=models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.Capital_Name