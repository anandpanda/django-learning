from django.db import models
from django.utils import timezone

# Create your models here.
class ChaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('PL', 'PLAIN'),
        ('EL', 'ELAICHI'),
    ]
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='chais/')
    chai_type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE)
    add_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')

    def __str__(self):
        return self.name