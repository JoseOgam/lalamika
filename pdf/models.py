from django.db import models
from django.conf import settings


class Semester(models.Model):
    sem = models.CharField(max_length=50)

    def __str__(self):
        return self.sem


class Unit(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Transcript(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    semester = models.ForeignKey(to=Semester, on_delete=models.CASCADE)
    unit = models.ForeignKey(to=Unit, on_delete=models.CASCADE)
    marks = models.DecimalField(decimal_places=1, max_digits=13)

    # def __str__(self):
    #     return "{user} ({semester}) [{unit}]".format(user=self.user, semester=self.semester, unit=self.unit)


class Complaints(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=200)
    regno = models.CharField(max_length=30)
    status = models.CharField(max_length=30)


class Viewtranscript(models.Model):
    my_sem = models.CharField(max_length=20)
