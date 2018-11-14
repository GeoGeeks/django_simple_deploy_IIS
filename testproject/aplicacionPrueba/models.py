from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

class User(models.Model):
	name = models.CharField(max_length=50)
	id_persona = models.AutoField(primary_key=True)

