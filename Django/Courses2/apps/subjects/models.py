from __future__ import unicode_literals

from django.db import models

# Create your models here.
class SubjectManager(models.Manager):
    def validate(self, post_data):
        errors = []
        if len(post_data['name']) < 3:
            errors.append("Name field must be 3 characters or more")
        if len(post_data['desc']) < 8:
            errors.append("Description field must be 8 characters or more")
        return errors

class Subject(models.Model):
    name = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = SubjectManager()