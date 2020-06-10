
from django.db import models


class Language(models.Model):

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        indexes = [models.Index(fields=['name'])]


class Project(models.Model):

    name = models.CharField(max_length=255)  # .name
    full_name = models.CharField(max_length=255, unique=True) # .full_name
    description = models.TextField()  # .description
    url = models.URLField(unique=True)  # .html_url
    initial_stars = models.IntegerField()  # .stargazers_count
    current_stars = models.IntegerField(default=0)  # .stargazers_count
    language = models.ForeignKey(Language, related_name="projects", on_delete=models.CASCADE)  # .language
    add_date = models.DateField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{}".format(
            self.name
        )

    class Meta:
        verbose_name_plural = "Stars"
        indexes = [
            models.Index(fields=[
                'name',
                'full_name',
                'description'
            ])
        ]
