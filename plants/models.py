from django.db import models


class PlantsData(models.Model):
    name = models.CharField(max_length=80, default='some plant')
    picture = models.URLField(max_length=200)
    picture2 = models.URLField(max_length=200)

    def __str__(self):
        return str(self.name)

