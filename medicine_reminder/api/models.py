from django.db import models

# Create your models here.
class Bucketlist(models.Model):
    """This class represnts the bucketlist model"""
    name = models.CharField(max_length=225, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """return a human readable represntation o"f the model in instance"""
        return "{}".format(self.name)
