from django.db import models
import uuid
from users.models import Profile

# Create your models here.

class List(models.Model):
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner= models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE)
    coowner=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.CASCADE,related_name = "sharing")
    title = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'List - ' + self.title
    


class Task(models.Model):
    owner_list = models.ForeignKey(List,on_delete=models.CASCADE,null = True)
    id = models.UUIDField(default= uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=300,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)
    deadline =models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return 'Task - ' + self.name

    class Meta:
        ordering=['completed']