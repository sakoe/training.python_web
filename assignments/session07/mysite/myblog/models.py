from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
	title = models.CharField(max_length=128)
	text = models.TextField(blank=True)
	author = models.ForeignKey(User)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)
	published_date = models.DateTimeField(blank=True, null=True)

	def __unicode__(self):
		return self.title

class Category(models.Model):
    class Meta:
        verbose_name_plural = "categories"
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=
        True, null=True,
                                   related_name='categories', through='Categorization')

    def __unicode__(self):
        return self.name

class Categorization(models.Model):
    class Meta:
        verbose_name_plural = "categories"
        # Still have the awkward "Categorization object"
        # thingie in the admin panel, though.
    post = models.ForeignKey(Post)
    category = models.ForeignKey(Category)



