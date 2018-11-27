from django.db import models


class Issues(models.Model):
    id_number = models.IntegerField()
    url = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    comments = models.IntegerField()

    def __str__(self):
        return self.title.split('\n')[0]
