from django.db import models

class drugInterectionTable(models.Model):
    levels = [
        ("major","Major"),
        ("minor","Minor"),
        ('moderate', "Moderate"),
        ('unknown', "Unknown")
    ]
    drug1_id = models.CharField(max_length=20)
    drug1_name = models.CharField(max_length=255)
    drug2_id = models.CharField(max_length=20)
    drug2_name = models.CharField(max_length=255)
    level = models.CharField(max_length=20, choices=levels, default="unknown")