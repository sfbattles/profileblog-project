from django.db import models

# Create your models here.
class Job(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
    class Meta:
        db_table = 'Job'

    def __str__(self):
        return str(self.name)