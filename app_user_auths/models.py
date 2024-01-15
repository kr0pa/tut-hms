from django.db import models
from django.contrib.auth.models import AbstractUser

from shortuuid.django_fields import ShortUUIDField

def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (instance.user.id, filename)
    return "user_{0}/{1}".format(instance.user.id, filename)

class Gender(models.TextChoices):
    MALE = 'F', 'Male'
    FEMALE = 'M', 'Female'
    OTHER = 'O', 'Other'
        
class IndentityType(models.TextChoices):
    NATIONAL_IDENTICATION_NUMBER = 'NIN', 'National Identication Number'
    DRIVER_LICENSE = 'DL', 'Driver License'
    INTERNATIONAL_PASSPORT = 'International Passport'


# Create your models here.
class User(AbstractUser):    
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=Gender.choices, default=Gender.MALE)
    
    otp = models.CharField(max_length=100, null=True, blank=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return self.username
    
class Profile(models.Model):
    pid = ShortUUIDField(length=7, max_length=25, alphabet="qazwsxedcrfvtgbyhnujmikolp1234567890")
    image = models.FileField(upload_to=user_directory_path, default="default.jpg", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=100, choices=Gender.choices, default=Gender.MALE)
    country = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    
    identity_type = models.CharField(max_length=100, choices=IndentityType.choices, null=True, blank=True)
    indentity_image = models.FileField(upload_to=user_directory_path, default="id.jpg", null=True, blank=True)
    
    facebook = models.URLField(null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    
    wallet = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    verified = models.BooleanField(default=False)
    
    date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-date']
        
    def __str__(self):
        if self.full_name:
            return f"{self.full_name}"
        else:
            return f"{self.user.username}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    