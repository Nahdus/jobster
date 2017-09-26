
from django.db import models
from django.core.urlresolvers import reverse

class Resume(models.Model):
    Name=models.CharField(max_length=100)
    Age=models.PositiveIntegerField(max_length=2)
    Qualification=models.CharField(max_length=200)
    Email=models.EmailField(max_length=150)
    Phone_number = models.PositiveIntegerField(max_length=9)
    About_Me=models.TextField(max_length=1000)
    Skills=models.CharField(max_length=500)
    is_selected = models.BooleanField(default=False)

    def __str__(self):
        return(str(self.pk)+" "+self.Name+" "+self.Qualification)

    def get_absolute_url(self):
        return reverse('submitresume:submit-resume')


