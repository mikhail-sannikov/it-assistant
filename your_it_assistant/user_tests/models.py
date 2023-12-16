from django.db import models

from users.models import User


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
    grade = models.IntegerField(default=0, unique=False)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.test}'


class Answer(models.Model):
    answer = models.TextField()
    explanation = models.TextField()
    right = models.BooleanField()

    def __str__(self):
        return f'{self.answer}'
