from django.db import models

# Create your models here.


class Note(models.Model):

    title = models.CharField(max_length=500)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        "Author", on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.title


class Author(models.Model):

    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
