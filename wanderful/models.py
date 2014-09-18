from django.db import models

# Create your models here.

class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    username = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=5) #women, men, M, F, Male, Female
    # vote = models.ManyToManyField(Post, related_name='users')

    def __unicode__(self):
        return u"{}".format(self.username)


class UserList(models.Model):
    listname = models.CharField(max_length=30)
    user = models.ForeignKey(User, related_name='userlists')


class Location(models.Model):
    continent = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    userlist = models.ManyToManyField(UserList, related_name='locations')
    hotel = models.TextField(null=True)