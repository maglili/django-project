from django.db import models

# Create your models here.
class Full_table(models.Model):
    alias = models.CharField(max_length=128)
    feture_name = models.CharField(max_length=128)

    def __str__(self):
        return self.alias
