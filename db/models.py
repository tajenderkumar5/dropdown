from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class States(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class District(models.Model):
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name       

class City(models.Model):
    District=models.ForeignKey(District,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name         

        

class Person(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)
    states=models.ForeignKey(States,on_delete=models.SET_NULL,null=True)
    district=models.ForeignKey(District,on_delete=models.SET_NULL,null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)



    def __str__(self):
        return self.name
