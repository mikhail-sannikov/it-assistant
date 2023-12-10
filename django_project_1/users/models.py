from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f'{self.username}'


class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()
    explanation = models.TextField()
    variant = models.ManyToManyField('Variant',
                                     related_name='question_variants')

    def __str__(self):
        return f'{self.question}'


class Variant(models.Model):
    variant = models.TextField()

    def __str__(self):
        return f'{self.variant}'


class Test(models.Model):
    title = models.CharField(max_length=30, null=True)
    question = models.ManyToManyField(Questions,
                                      related_name='test_questions')

    def __str__(self):
        return f'{self.title}'


class TestsList(models.Model):
    test = models.ForeignKey(Test, null=True, on_delete=models.CASCADE)
    grade = models.IntegerField(null=True, unique=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test}'


class WrongAnswer(models.Model):
    wrong_answer = models.TextField()
    explanation = models.TextField()

    def __str__(self):
        return f'{self.wrong_answer}'
