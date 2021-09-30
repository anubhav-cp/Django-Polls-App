from django.db import models
from django.db.models.base import Model



class Poll(models.Model):

    title = models.CharField(max_length=200)   # question fields

    # option field
    option_1 = models.CharField(max_length=200)  
    option_2 = models.CharField(max_length=200)
    option_3 = models.CharField(max_length=200)
    option_4 = models.CharField(max_length=200)

    # votes count field
    option_1_count = models.IntegerField(default=0)
    option_2_count = models.IntegerField(default=0)
    option_3_count = models.IntegerField(default=0)
    option_4_count = models.IntegerField(default=0)


    def __str__(self) -> str:
        return self.title
    
    def total(self):

        return self.option_1_count + self.option_2_count + self.option_3_count + self.option_4_count
