from django.db import models

class Horoscope(models.Model):
    SIGN_CHOICES = [
        ('aries', 'Aries'),
        ('taurus', 'Taurus'),
        ('gemini', 'Gemini'),
        ('cancer', 'Cancer'),
        ('leo', 'Leo'),
        ('virgo', 'Virgo'),
        ('libra', 'Libra'),
        ('scorpio', 'Scorpio'),
        ('sagittarius', 'Sagittarius'),
        ('capricorn', 'Capricorn'),
        ('aquarius', 'Aquarius'),
        ('pisces', 'Pisces'),
    ]
    
    sign = models.CharField(max_length=20, choices=SIGN_CHOICES)
    date = models.DateField()
    prediction = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['sign', 'date']
        ordering = ['-date', 'sign']
    
    def __str__(self):
        return f"{self.get_sign_display()} - {self.date}" 