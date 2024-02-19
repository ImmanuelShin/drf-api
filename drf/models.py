from django.db import models
from django.contrib.auth import get_user_model

RATING_CHOICES = [
    (1, '1 - Shouldn\'t exist'),
    (2, '2 - Doesn\' make sense'),
    (3, '3 - Mid'),
    (4, '4 - Makes sense'),
    (5, '5 - Peak'),
]

class DRF(models.Model):
    owner = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField()
    rating = models.IntegerField(choices=RATING_CHOICES, default=3) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name