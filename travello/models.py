from django.db import models

class Destination(models.Model):
    id: int
    name: models.CharField(max_length=100)
    img: models.ImageField(upload_to='pics')
    desc: models.TextField()
    price: models.IntegerField()
    offer: models.BooleanField(default=False)

    class Meta:
        app_label = 'travelloProject'

class News(models.Model):
    id: models.IntegerField()
    img: models.ImageField(upload_to='pics')
    day: models.IntegerField()
    month: models.CharField(max_length=100)
    title: models.CharField(max_length=100)
    text: models.TextField()

    class Meta:
        app_label = 'travelloProject'
