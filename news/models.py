from django.db import models


class Editor(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = [
            'first_name'
        ]


class Tags(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Articles(models.Model):
    title = models.CharField(max_length=40)
    post = models.TextField()
    editor = models.ForeignKey(Editor)
    tags = models.ManyToManyField(Tags)