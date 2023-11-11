from django.db import models
from django.urls import reverse


class IsTheBestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_the_best=1)


class Friends(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_the_best = models.BooleanField(default=True)

    objects = models.Manager()
    is_the_best_manager = IsTheBestManager()

    def __str__(self):
        return self.name

    class Meta:
        pass
        # ordering = ["-time_create"]
        # indexes = [
        #     models.Index(fields=["-time_create"])
        # ]

    def get_absolute_url(self):
        return reverse("friend-slug", kwargs={"fr_slug": self.slug})
