from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=20)
    theme_data = models.ManyToManyField('ThemeList')

    def __str__(self):
        return self.name


class Theme(models.Model):
    theme = models.CharField(max_length=40)
    passed_theme = models.BooleanField(default=0)


class ThemeList(models.Model):
    theme = models.CharField(max_length=40)
    educational_data = models.ManyToManyField('EducationalResource')

    def __str__(self):
        return self.theme


class EducationalResource(models.Model):
    reference = models.CharField(max_length=200)
    summary = models.TextField(null=True)

    def __str__(self):
        return self.reference
