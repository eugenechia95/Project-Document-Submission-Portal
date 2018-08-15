from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.urls import reverse
import uuid
import datetime

# Create your models here.

def _get_age(self):
        #functions to calculate whatever you want...
        today = date.today()
        x = today.year - self.opening_date.year
        return x

class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    country = models.CharField(max_length=200, help_text="Enter country")

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('country-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.country
    
class City(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    city = models.CharField(max_length=200, help_text="Enter city")

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('city-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.city

class BuildingType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular type")
    buildingtype = models.CharField(max_length=200, help_text="Enter type")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.buildingtype

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    project_name = models.CharField(max_length=200, help_text="Enter project name")
    project_description = models.TextField(help_text="Enter project description", null=True)
    access_personnel = models.ManyToManyField(Group, null=True, blank=True)
    buildingtype = models.ForeignKey('BuildingType', on_delete=models.SET_NULL, null=True)
#    project_manager = models.ManyToManyField(User, null=True)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True, blank=True)
    city = models.ForeignKey('City', on_delete=models.SET_NULL, null=True, blank=True)
    GFA = models.DecimalField(max_digits=10, decimal_places=2)
    floors= models.IntegerField(null=True, blank=True)
    kickoff_meeting=models.BooleanField(default = False)
    kickoff_meeting_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)
    concept_DAP=models.BooleanField(default = False)
    concept_DAP_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)
    mockup_DAP=models.BooleanField(default = False)
    mockup_DAP_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)
    design_drawing_approved=models.BooleanField(default = False)
    construction=models.BooleanField(default = False)
    construction_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)
    pop_team=models.BooleanField(default = False)
    pop_team_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)
    IST=models.BooleanField(default = False)
    IST_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)
    completion=models.BooleanField(default = False)
    completion_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)
    opening_date= models.DateField(null=True, blank=True, help_text="Enter the following format: YYYY-MM-DD",)

    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('project-detail', args=[str(self.id)])
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.project_name
    



    
class Phase(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    title = models.CharField(max_length=200, help_text="Enter phase name", default = "NIL")
#    doc1 = models.FileField(upload_to=None, max_length=100,)
#    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)

    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    title = models.CharField(max_length=200, help_text="Enter phase name", default = "NIL")
#    doc1 = models.FileField(upload_to=None, max_length=100,)
#    project = models.ForeignKey('Project', on_delete=models.SET_NULL, null=True)

    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.title


    
class Documentinstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular document")
    name = models.CharField(max_length=200, help_text="Enter document name",)
    phase = models.ForeignKey(Phase, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    refdoc = models.FileField(upload_to= "uploads/ref", max_length=100, null=True, blank=True)
    doc = models.FileField(upload_to= "uploads", max_length=100, null=True, blank=True)
    feedback_document = models.FileField(upload_to= "uploads/com", max_length=100, null=True, blank=True)
    submitter = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank = True)
    dos = models.DateField(null=True, blank=True,)
    dor = models.DateField(null=True, blank=True,)
    comment = models.TextField(help_text="Enter comments", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete= models.CASCADE, null=True, blank = True)
    CHOICES = (
        ('Pending', 'Pending'),
        ('Under Review', 'Under Review'),
        ('Reviewed', 'Reviewed'),
        ('Resubmission Required', ' Resubmission Required'),
    )

    reviewed_status = models.CharField(max_length = 22, choices=CHOICES, default='Pending')

    def get_absolute_url(self):
        """
        Returns the url to access a particular equipment instance.
        """
        return reverse('document-detail', args=[str(self.id)])    
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
    
class templateset(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    name = models.CharField(max_length=200, help_text="Enter phase name", default = "NIL")

    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    
class templateinstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular project")
    name = models.CharField(max_length=200, help_text="Enter phase name", default = "NIL")
    refdoc = models.FileField(upload_to= "uploads/templateref", max_length=100, null=True, blank=True)
    templateset = models.ForeignKey('templateset', on_delete=models.CASCADE, null=True)

    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
