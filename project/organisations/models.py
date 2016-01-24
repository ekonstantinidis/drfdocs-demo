import uuid
from django.db import models
from project.accounts.models import User


class Organisation(models.Model):

    class Meta:
        verbose_name_plural = "Organisations"
        ordering = ['name']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True)
    members = models.ManyToManyField(User, through='Membership', through_fields=('organisation', 'user'))

    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_no_of_members_active(self):
        return self.members.filter(is_active=True).count()

    def get_no_of_members_all(self):
        return self.members.count()


class Membership(models.Model):

    class Meta:
        unique_together = ("organisation", "user")

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    joined = models.DateTimeField(auto_now_add=True)

    organisation = models.ForeignKey(Organisation)
    user = models.ForeignKey(User)
    is_owner = models.BooleanField(default=False)
