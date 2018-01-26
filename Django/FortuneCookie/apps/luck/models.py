# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..fortune.models import User
from django.db import models

class ProverbManager(models.Manager):
    def validate_proverb(self, post_data):
        # validate proverbs
        errors = []
        if len(post_data['proverb']) < 1:
            errors.append('fields are required')
        if not "author" in post_data and len(post_data['new_author']) < 3:
            errors.append('new author names must 3 or more characters')

        if "author" in post_data and len(post_data['new_author']) > 0 and len(post_data['new_author']) < 3:
            errors.append('new author names must 3 or more characters')
        return errors

    def create_proverb(self, clean_data, user_id):
        # retrive or create author
        the_author = None
        if len(clean_data['new_author']) < 1:
            the_author = Author.objects.get(id=int(clean_data['author']))
        else:
            the_author = Author.objects.create(name=clean_data['new_author'])
        # returns a Proverb object
        return self.create(
            proverb = clean_data['proverb'],
            book = the_book,
            posted_by = User.objects.get(id=user_id)
        )

    def recent_and_not(self):
        '''
        returns a tuple with the zeroeth index containing query for 3 most recent proverbs, and the first index
        containing the rest
        '''
        return (self.all().order_by('-created_at')[:3], self.all().order_by('-created_at')[3:])

class Proverb(models.Model):
    proverb = models.TextField()
    author = models.ForeignKey(Author, related_name="proverbs")
    posted_by = models.ForeignKey(User, related_name="proverbs_left")
    created_at = models.DateTimeField(auto_now_add=True)
    objects = ProverbManager()
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
