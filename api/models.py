from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class MyUserManager(BaseUserManager):
    def create_user(self, username, password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        
        user = self.model(username=username, **extra_fields)
        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self.create_user(username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    gender = models.CharField(max_length=100)
    employeeid = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    username = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    
    # Driver-specific fields
    is_driver = models.BooleanField(default=False)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    license_plate = models.CharField(max_length=20, blank=True, null=True)

    objects = MyUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username

class Cab(models.Model):
    start = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    availableSeats = models.SmallIntegerField()
    driver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_driver': True})
    startTime = models.TimeField(default=timezone.now)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.driver.license_plate} - {self.driver.name}"

class Ride(models.Model):
    driver = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'is_driver': True})
    start = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    cabNumber = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)

    def __str__(self):
        return f"{self.time} Ride with {self.driver.name}"

class location(models.Model):
    latitude=models.FloatField()
    longitude=models.FloatField()
