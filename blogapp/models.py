from django.db import models
from django.contrib.auth.models import User
from django.utils.timesince import timesince
class Card(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=100, unique=True)
    image_url = models.URLField()
    content = models.TextField()
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now=True)
    
    def __str__ (self):
        return self.title
    
    class Meta:
        ordering = ['id']
    
    # def comment_count(self):
    #     return self.comment_set.all().count()
    
    # def view_count(self):
    #     return self.postview_set.all().count()
    
    # def like_count(self):
    #     return self.like_set.all().count()
        
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    @property
    def timesince(self):
        return timesince(self.time_stamp)
    
    def __str__(self):
        return self.user.username
    
class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username
    
class PostView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE) 
    time_stamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username