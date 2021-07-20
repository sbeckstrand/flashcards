from django.db import models

# Create your models here.
class Collection(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    color = models.CharField(max_length=10)
    created_date = models.DateTimeField('created date')
    is_active = models.BooleanField(default=True)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def is_favorite(self):
        return self.is_favorite

    def is_active(self):
        return self.is_active

class Card(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    header = models.CharField(max_length=100)
    body = models.CharField(max_length=300)
    color = models.CharField(max_length=10)
    created_date = models.DateTimeField('created date')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.header

    def is_favorite(self):
        return self.is_favorite

    def is_active(self):
        return self.is_active
    


