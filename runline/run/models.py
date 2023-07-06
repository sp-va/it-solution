from django.db import models

class TextForLine(models.Model):
    text = models.CharField(max_length=50)
