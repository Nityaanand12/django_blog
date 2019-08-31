from django.conf import settings
from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.
class SearchQuery(models.Model):
	user = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
	query = models.CharField(max_length=220)
	timestamp = models.DateTimeField(auto_now_add=True)
