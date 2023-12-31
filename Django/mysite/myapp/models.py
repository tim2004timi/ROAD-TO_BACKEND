from django.db import models
from django.urls import reverse


class IsTheBestManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_the_best=Friends.Status.THE_BEST)


class Friends(models.Model):
    class Status(models.IntegerChoices):
        NOT_THE_BEST = 0, "Не лучший друг"
        THE_BEST = 1, "Лучший друг"

    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)
    description = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_the_best = models.BooleanField(choices=Status.choices, default=Status.NOT_THE_BEST)
    gender = models.ForeignKey("Gender", on_delete=models.PROTECT, related_name="notes")
    tags = models.ManyToManyField("TagFriends", blank=True, related_name="tags")
    objects = models.Manager()
    is_the_best_manager = IsTheBestManager()
    girlfriend = models.OneToOneField("GirlFriend", on_delete=models.SET_NULL, null=True,
                                      blank="True", related_name="boyfriend")

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


class Gender(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("gender-slug", kwargs={"gender_slug": self.slug})


class TagFriends(models.Model):
    objects = models.Manager()
    tag = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True)

    def __str__(self):
        return self.tag

    def get_absolute_url(self):
        return reverse("tag", kwargs={"tag_slug": self.slug})


class GirlFriend(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=50, default="-")
    boyfriends_count = models.IntegerField(blank=True, default=0)

    def __str__(self):
        return self.name
