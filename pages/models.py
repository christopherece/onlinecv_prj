from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class About(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    description = RichTextField()
    image = models.ImageField(upload_to='about_images/')
    fb_link = models.URLField(max_length=200, null=True, blank=True)
    twitter_link = models.URLField(max_length=200, null=True, blank=True)
    linkedin_link = models.URLField(max_length=200, null=True, blank=True)
    github_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
    

class Experience(models.Model):
    company_name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = RichTextField()

    def __str__(self):
        return super().__str__()
    
class Education(models.Model):
    school_name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    gpa = models.FloatField(null=True, blank=True)
    description = RichTextField()

    def __str__(self):
        return super().__str__()
    
class Interests(models.Model):
    interests = RichTextField(null=True, blank=True)
    def __str__(self):
        return super().__str__()

class Certifications(models.Model):
    certificate_name = models.CharField(max_length=100)
    certificate_startdate = models.DateField(null=True, blank=True)
    certificate_enddate = models.DateField(null=True, blank=True)
    certificate_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return super().__str__()
    