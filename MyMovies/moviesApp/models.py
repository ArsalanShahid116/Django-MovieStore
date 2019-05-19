from django.db import models

class myMovie(models.Model):
    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()

    def __str__(self):
        return '{} ({})'.format(
        self.title, self.year)
