from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class user_image(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile_image')
    image=models.ImageField(upload_to='profile_image/')

    def __str__(self):
        return f"{self.user.username}"

class Category(models.Model):
    category=models.CharField(max_length=50)
    slug=models.SlugField(max_length=50, unique=True, null=True,blank=True)

    def __str__(self):
        return self.category

class blog_post(models.Model):
    title=models.CharField(max_length=100)
    content=models.TextField()
    category=models.ManyToManyField(Category)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    post_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
