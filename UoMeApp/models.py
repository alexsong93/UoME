from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from datetime import datetime

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    #phone_number = models.CharField(max_length=15, blank=True)

class Group(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    members = models.ManyToManyField(User);
    pub_date = models.DateTimeField()
    slug = models.SlugField(max_length=40, unique=True)
    
    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return "/groups/%s" % self.slug
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        
        self.pub_date = datetime.now()
        super(Group, self).save(*args, **kwargs)

# Create your models here.
class Event(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField()
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/events/%s" % self.slug
    
class UoMePost(models.Model):
    ower_name = models.ForeignKey(User, related_name='ower')
    receiver_name = models.ForeignKey(User, related_name='receiver')
    event = models.ForeignKey(Event)
    item_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    comments = models.TextField()
    pub_date = models.DateTimeField()
    slug = models.SlugField(max_length=40, unique=True)
     
    class Meta:
        ordering = ["pub_date"]
      
    def __unicode__(self):
        return "%s, %s" % (self.pub_date, self.item_name)
  
    def get_absolute_url(self):
        return "/%s/%s/" % (self.event, self.slug)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.item_name)
        
        self.pub_date = datetime.now()
        super(UoMePost, self).save(*args, **kwargs)
    
    
    
    