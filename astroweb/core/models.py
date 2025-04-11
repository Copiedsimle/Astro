from django.db import models

class BirthDetails(models.Model):
    user_id = models.IntegerField()
    birth_date = models.DateField()
    birth_time = models.TimeField()
    birth_place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    zodiac_sign = models.CharField(max_length=20, blank=True, null=True)
    life_path_number = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.user_id} - {self.birth_date}"