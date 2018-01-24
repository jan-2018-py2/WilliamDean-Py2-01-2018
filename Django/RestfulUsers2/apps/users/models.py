from __future__ import unicode_literals
import re
from django.db import models

# Create your models here.
# Setting a built-in validator - we'll see if it works
EMAIL_REG = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validate(self, post_data):
        errors = {}

        # checking fields for emptiness
        for field, value in post_data.iteritems():
            if len(value) < 1:
                errors[field] = "{} field is required".format(field.replace('_', ' '))

            # checking for minimum length
            if field == "first_name" or field == "last_name":
                if not field in errors and len(value) < 2:
                    errors[field] = "{} field must be at least 2 characters".format(field.replace('_', ' '))  

        # checking email field for valid email
        if not "email" in errors and not re.match(EMAIL_REG, post_data['email']):
            errors['email'] = "invalid email"

        # if email is valid, confirm database for existing email
        else:
            if len(self.filter(email=post_data['email'])) > 1:
                errors['email'] = "email already in use"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
        return self.email
