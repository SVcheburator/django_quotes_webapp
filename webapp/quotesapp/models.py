from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=25, null=False, unique=True)

    def __str__(self):
        return f"{self.name}"


class Authors(models.Model):
    fullname = models.CharField(max_length=30, null=False)
    born_date = models.DateTimeField(null=False)
    born_location = models.CharField(max_length=50, null=False)
    description = models.CharField(max_length=150, null=False)

    def __str__(self):
        return f"{self.fullname}"


class Quotes(models.Model):
    tags = models.ManyToManyField(Tag)
    author = models.ManyToManyField(Authors)
    quote = models.CharField(null=False)

    def __str__(self):
        return f"{self.quote}"