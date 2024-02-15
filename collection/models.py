from django.db import models
from .models import *


# 4

from django.core.exceptions import ValidationError
import os


gender = (
    ('Male', 'Male'),
    ('Female', 'Female')
)
# 3
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.jpg', '.jpeg', '.png', '.tiff', '.giff']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')

def user_directory_path(request, filename):
    # 6
    return '/'.join(['content', request.contact, filename])

# Create your models here.
class Person(models.Model): 
    first_name = models.CharField(max_length=30) # String
    last_name = models.CharField(max_length=120) # String
    gender = models.CharField(max_length=7, choices=gender) # String 
    dob = models.DateField()
    # 5
    avatar = models.FileField(blank=True, upload_to=user_directory_path,  validators=[validate_file_extension])
    contact = models.CharField(max_length=150, blank=True, null=True)
    active = models.BooleanField(default=True)