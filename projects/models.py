from django.db import models
import uuid

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True) 
    # null is set as true to allow db table to have null vals and blank for form
    featured_image = models.ImageField(null=True, blank = True, default="default.jpg")
    demo_link = models.CharField(max_length=2000, null=True, blank = True)
    source_link = models.CharField(max_length=2000, null=True, blank = True)
    tags = models.ManyToManyField('Tag', blank=True)
    vote_total = models.IntegerField(default=0, null = True, blank = True)
    vote_ratio = models.IntegerField(default=0, null = True, blank = True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    def __str__(self):
        return self.title

class Review(models.Model):
    #Creating a tuple to add vote
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote'),
    )
    #owner
    # When a foreignkey is taken in models, you will be able to see a dropdown on admin panel to relate this model to the foreign key model
    project = models.ForeignKey(Project, on_delete=models.CASCADE) 
    # Basically on_delete is kept to delete related reviews when a project is deleted

    body = models.TextField(null= True, blank= True)
    value = models.CharField(max_length = 200, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    def __str__(self):
        return self.value
    

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique = True, primary_key = True, editable = False)
    def __str__(self):
        return self.name

