from django.db import models

class Blog(models.Model):

    """This Class is to create blog databse"""

    title = models.CharField(max_length = 100)
    description = models.TextField()
    date = models.DateField()
