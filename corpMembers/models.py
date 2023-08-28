from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

class Category(models.Model):
    BATCH_CHOICES = (
        ('batchA', 'Batch A'),
        ('batchB', 'Batch B'),
        ('batchC', 'Batch C'),
       
    )

    STREAM_CHOICES = (
        ('stream1', 'Stream 1'),
        ('stream2', 'Stream 2'),
    )

    YEAR_CHOICES = (
        ('2022', '2022'),
        ('2023', '2023'),
        ('2024', '2024'),
        ('other', 'Other'),
    )
    
    batch_name = models.CharField(max_length=100, choices=BATCH_CHOICES, default='batch1')
    stream_number = models.CharField(max_length=100, choices=STREAM_CHOICES, default='stream1')
    year = models.CharField(max_length=100, choices=YEAR_CHOICES, default='2022')

    def __str__(self):
        return f"{self.batch_name} - {self.stream_number} ({self.year})"


class User(AbstractUser):
    STATUS_CHOICES = (
        ('Single', 'Single'),
        ('married', 'Married'),
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    discipline = models.CharField(max_length=20)
    image = models.ImageField(upload_to='photos/', blank=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(unique=True)
    PPA=models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)

    def get_url(self):
        return reverse('cmdetails', args=[self.pk])

   
    def __str__(self):
        return self.username
