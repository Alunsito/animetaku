from django.db import models

# Create your models here.
class anime(models.Model):
    name_anime = models.CharField(max_length=200)
    release_date = models.DateTimeField('Release Date')
    genres = models.CharField(max_length=200)

    def __str__(self):
        return self.name_anime


class user(models.Model):
    name_user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name_user

class review(models.Model):
    user_post = models.ForeignKey(user, on_delete=models.CASCADE)
    text_post = models.CharField(max_length=5000)
    date_post = models.DateField('Post Date')



