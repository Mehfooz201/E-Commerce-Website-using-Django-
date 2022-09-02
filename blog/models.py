from django.db import models

# Create your models here.

class Blogpost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    head0 = models.CharField(max_length=500, default='')
    content0 = models.CharField(max_length=5000, default='')

    head1 = models.CharField(max_length=500, default='')
    content1 = models.CharField(max_length=5000, default='')

    head3 = models.CharField(max_length=500, default='')
    content3 = models.CharField(max_length=5000, default='')

    pub_date = models.DateField()

    thumbnail = models.ImageField(upload_to='shop/image', default='')

    def __str__(self):
        return self.title
