from django.db import models

class ShelfLayout(models.Model):
    layout_data = models.JSONField()