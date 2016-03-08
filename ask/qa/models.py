from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
	title = models.CharField(max_length=255)
	text = models.TextField()
	added_at = models.DateField()
	rating = models.IntegerField()
	author = models.ForeignKey(User, related_name="a",
		null=True, on_delete=models.SET_NULL)
	likes = models.ManyToManyField(User, related_name="l")

class Answer(models.Model):
	text = models.TextField()
	added_at = models.DateField()
	question = models.ForeignKey(Question,
		null=False, on_delete=models.PROTECT)
	author=models.ForeignKey(User,
		null=True, on_delete=models.SET_NULL)
