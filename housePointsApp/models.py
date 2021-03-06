from django.db import models

class House(models.Model):
    name = models.CharField(max_length=30)
    points = models.IntegerField(default=0)
    color = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name + ": " + str(self.points) + "; color: " + self.color + "; id: " + str(self.id)
