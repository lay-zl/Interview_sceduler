from django.db import models

# Create your models here.

choices=[
    ('Technical-1','Technical-1'),
    ('Technical-2','Technical-2'),
    ('Managerial Round','Managerial Round'),
    ('HR','HR'),
    ('Other','Other')
]

choice = [
    ('passed', 'Passed'),
    ('failed', 'Failed'),
    ('pending', 'Pending'),
    ('rescheduled', 'Rescheduled'),
         ]
class Interview(models.Model):
    company = models.CharField(max_length=255)
    date = models.DateField()
    time = models.CharField(max_length=100)
    round = models.CharField(max_length=100,choices=choices)
    hr_name = models.CharField(max_length=100)
    hr_contact = models.CharField(max_length=100)
    result = models.CharField(max_length=100,choices=choice,null=True,blank=True)
    size = models.CharField(max_length=100,null=True,blank=True)
    url = models.URLField(null=True,blank=True)
    linkdin = models.URLField(null=True,blank=True)
    comment = models.TextField(null=True,blank=True)



    def __str__(self):
        return self.company

class Hr(models.Model):
    name = models.CharField(max_length=100)
    mob = models.CharField(max_length=16)
    compnay = models.CharField(max_length=100)
    date = models.DateField(null=True)
    description = models.TextField()

    def __str__(self):
        return self.name +' '+self.compnay