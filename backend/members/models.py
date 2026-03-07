from django.db import models
from django.conf import settings
from organisation.models import Assembly


class Member(models.Model):

    STATUS_CHOICES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
        ("DECEASED", "Deceased"),
        ("TRANSFERRED", "Transferred"),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    sex = models.CharField(max_length=10)
    birth_date = models.DateField(null=True, blank=True)

    phone = models.CharField(max_length=30, blank=True)
    email = models.EmailField(blank=True)
    address = models.TextField(blank=True)

    assembly = models.ForeignKey(
        Assembly,
        on_delete=models.PROTECT,
        related_name="members"
    )

    join_date = models.DateField()

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="ACTIVE"
    )

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["last_name", "first_name"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
