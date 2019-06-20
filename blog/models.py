from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    image = models.ImageField(upload_to='images/blog/')
    class Meta:
        db_table = 'Blog'

    def __str__(self):
        return str(self.title)
