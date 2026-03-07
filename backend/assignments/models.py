from django.db import models

from members.models import Member
from departments.models import Department
from organisation.models import (
    Continent,
    Zone,
    Country,
    District,
    Assembly
)


class Assignment(models.Model):

    member = models.ForeignKey(
        Member,
        on_delete=models.CASCADE,
        related_name="assignments"
    )

    role = models.CharField(max_length=150)

    department = models.ForeignKey(
        Department,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    continent = models.ForeignKey(
        Continent,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    district = models.ForeignKey(
        District,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    assembly = models.ForeignKey(
        Assembly,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):

        levels = [
            self.continent,
            self.zone,
            self.country,
            self.district,
            self.assembly
        ]

        filled = [level for level in levels if level is not None]

        if len(filled) > 1:
            raise ValueError("Assignment must target only one territorial level")

    def __str__(self):
        return f"{self.member} - {self.role}"
