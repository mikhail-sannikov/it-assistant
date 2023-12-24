from django.db import models

from users.models import User


class Object(models.Model):
    object = models.CharField(max_length=20)
    theme_data = models.ManyToManyField('Theme')

    def __str__(self):
        return self.object


class Theme(models.Model):
    theme = models.CharField(max_length=40)
    educational_data = models.ManyToManyField('EducationalResource')

    def __str__(self):
        return self.theme


class EducationalResource(models.Model):
    reference = models.CharField(max_length=200)

    def __str__(self):
        return self.reference


class UserObjectData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    progress = models.FloatField(default=0)


class UserThemeData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    passed_theme = models.BooleanField(default=False, null=True)
