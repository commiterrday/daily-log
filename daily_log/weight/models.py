from django.db import models

# Create your models here.
class Weight(models.Model):
    time = models.DateTimeField()
    kg = models.FloatField()
    body_fat = models.FloatField()

    def __str__(self):
        return '%.1f kg, %.1f%%' % (self.kg, self.body_fat)

    class Meta:
        ordering = ["time"]
