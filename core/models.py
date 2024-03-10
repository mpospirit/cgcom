from django.db import models

# Create your models here.
class BlogViews(models.Model):
    id = models.AutoField(primary_key=True)
    blogId = models.IntegerField()
    dateCreated = models.DateTimeField(auto_now_add=True)
    ipAddress = models.CharField(max_length=255)
    userAgent = models.CharField(max_length=255)

    def __str__(self):
        return self.blogId
    
    class Meta:
        db_table = "BlogViews"