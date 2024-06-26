from django.db import models

class Post(models.Model):
    title = models.CharField("Title", max_length=200)
    description = models.TextField("Description")
    author = models.CharField("Author", max_length=200)
    date = models.DateTimeField("Date")

    def __str__(self):
        return f"{self.title}, {self.author}"

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
