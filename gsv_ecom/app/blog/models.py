from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    parent_id = models.CharField(max_length=64, blank=True, null=True)

    def __str__(self):
        return self.name


class Blog(models.Model):  
    id = models.CharField(max_length=24, primary_key=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)  
    content = models.TextField()  
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to='blog_images/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0) 
    category = models.ManyToManyField(Category)  
    is_publish = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    id = models.CharField(max_length=24, primary_key=True)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE) 
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"Comment on {self.blog.title} by {self.id}"
