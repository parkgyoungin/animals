from django.db import models



class Member(models.Model):
    name = models.CharField(max_length=10)
    user_id = models.CharField(max_length=10)
    password = models.CharField(max_length=12)
    phone_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=2)
    animal_count = models.IntegerField()




