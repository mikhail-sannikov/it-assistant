from django.db import models


class Object(models.Model):
    name = models.CharField(max_length=20)
    theme_data = models.ManyToManyField('Theme')
    is_active = models.BooleanField(default=False)
    progress = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Theme(models.Model):
    theme = models.CharField(max_length=40)
    passed_theme = models.BooleanField(default=False, null=True)
    summary = models.TextField(blank=True, null=True)
    educational_data = models.ManyToManyField('EducationalResource')

    def __str__(self):
        return self.theme


class EducationalResource(models.Model):
    reference = models.CharField(max_length=200)

    def __str__(self):
        return self.reference
