from django.db import models

# Create your models here.

class Traveler(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=5) #women, men, M, F, Male, Female
    # vote = models.ManyToManyField(Post, related_name='users')

    def __unicode__(self):
        return u"{}".format(self.username)


class TravelList(models.Model):
    listname = models.CharField(max_length=30)
    user = models.ForeignKey(Traveler, related_name='travellists')


class Location(models.Model):
    continent = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    userlist = models.ManyToManyField(TravelList, related_name='locations')
    hotel = models.TextField(null=True)