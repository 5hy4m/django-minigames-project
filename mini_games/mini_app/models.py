from django.db import models

# Create your models here.
class archery_boards(models.Model):
    name = models.CharField(max_length=264)
    score = models.IntegerField(null=True)


    def  __str__(self):
        return (self.name)
