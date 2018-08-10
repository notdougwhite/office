from django.db import models
from django.utils import timezone
import datetime

# Create your models here.


class Case(models.Model):
    your_name = models.CharField(max_length=200, verbose_name="Last Name of adopting Parent")
    childs_name = models.CharField(max_length=200, verbose_name="Current last name of child/Children being adopted")
    case_number = models.CharField(max_length=200, blank=True)
    entry_date = models.DateTimeField(verbose_name='Date Entered', auto_now_add=True)

    def __str__(self):
        return self.your_name + " / " + self.childs_name

    def was_recently_entered(self):
        return self.entry_date >= timezone.now() - datetime.timedelta(days=1)


class Client(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    dob = models.DateField('Date of Birth')

    def __str__(self):
        return self.full_name


class Child(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    current_name = models.CharField(max_length=200)
    new_name = models.CharField(max_length=200, blank=True)
    dob = models.DateField('Date of Birth')

    class Meta:
        verbose_name_plural = "children"

    def __str__(self):
        return self.current_name


class Document(models.Model):
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    petition = models.BooleanField(default=False)
    app_order = models.BooleanField(default=False)
    final_decree = models.BooleanField(default=False)

    def fields(self):
        return [f.name for f in self._meta.fields+self._meta.many_to_many]
