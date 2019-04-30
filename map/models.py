from django.db import models

# Create your models here.

class City(models.Model):
    id = models.CharField(max_length=10,primary_key=True)
    country_code = models.CharField(max_length=50,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    place_name = models.CharField(max_length=50,null=True,blank=True)
    admin_name1 = models.CharField(max_length=50,null=True,blank=True)
    admin_name2 = models.CharField(max_length=50,null=True,blank=True)
    admin_name3 = models.CharField(max_length=50,null=True,blank=True)
    latitude = models.FloatField(null=True,blank=True)
    longitude = models.FloatField(null=True,blank=True)
    accuracy = models.IntegerField(null=True,blank=True)
    malaria_cause = models.IntegerField(null=True,blank=True)
    malaria_deaths = models.IntegerField(null=True,blank=True)
    malnutrition_cause = models.IntegerField(null=True,blank=True)
    malnutrition_deaths = models.IntegerField(null=True,blank=True)
    tuberculosis_cause = models.IntegerField(null=True,blank=True)
    tuberculosis_deaths = models.IntegerField(null=True,blank=True)
    population = models.IntegerField(null=True,blank=True)
    malaria_risk_factor = models.FloatField(null=True,blank=True)
    malnutrition_risk_factor = models.FloatField(null=True,blank=True)
    tuberculosis_risk_factor = models.FloatField(null=True,blank=True)
    malaria_risk_index = models.FloatField(null=True,blank=True)
    malnutrition_risk_index = models.FloatField(null=True,blank=True)
    tuberculosis_risk_index = models.FloatField(null=True,blank=True)





    
    def __str__(self):
        return self.place_name
    
