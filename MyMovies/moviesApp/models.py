from django.db import models

class PersonManager(models.Manager):
    def all_with_prefetch_movies(self):
        qs = self.get_queryset()
        return qs.prefetch_related(
                'directed',
                'writing_credits',
                )

class Person(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    born = models.DateField()

    objects = PersonManager()

    class Meta:
        ordering = ('last_name', 'first_name')

    def __str__(self):
        return '{}, {} ({})'.format(
                    self.last_name,
                    self.first_name, 
                    self.born)

class MovieManager(models.Manager):
    def all_with_related_persons(self):
        qs = self.get_queryset()
        qs = qs.select_related(
                'director')
        qs = qs.prefetch_related(
                'writers')
        return qs

class myMovie(models.Model):
    title = models.CharField(max_length=140)
    plot = models.TextField()
    year = models.PositiveIntegerField()
    director = models.ForeignKey(
            to='Person',
            null=True,
            on_delete=models.SET_NULL,
            related_name='directed',
            blank=True)
    writers = models.ManyToManyField(
            to='Person',
            related_name='writing_credits',
            blank=True)

    objects = MovieManager()

    def __str__(self):
        return '{} ({})'.format(
        self.title, self.year)
