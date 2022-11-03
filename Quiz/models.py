from tkinter import CASCADE
from unicodedata import category
from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=256)
    def __str__(self):
        return self.name


class python_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class django_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class mathematical_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class spots_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class entertainment_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class technology_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class nature_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class history_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

class movies_questions(models.Model):
    question = models.CharField(max_length=255)
    answer = models.CharField(max_length=255)
    option_1 = models.CharField(max_length=255)
    option_2 = models.CharField(max_length=255)
    option_3 = models.CharField(max_length=255)
    option_4 = models.CharField(max_length=255)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
