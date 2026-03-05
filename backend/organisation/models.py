from django.db import models


class Continent(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Zone(models.Model):
    name = models.CharField(max_length=100)
    continent = models.ForeignKey(
        Continent, on_delete=models.CASCADE, related_name="zones"
    )

    class Meta:
        unique_together = ("name", "continent")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.continent})"


class Country(models.Model):
    name = models.CharField(max_length=100)
    zone = models.ForeignKey(Zone, on_delete=models.CASCADE, related_name="countries")

    class Meta:
        unique_together = ("name", "zone")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.zone})"


class District(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="districts"
    )

    class Meta:
        unique_together = ("name", "country")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.country})"


class Assembly(models.Model):
    name = models.CharField(max_length=150)
    district = models.ForeignKey(
        District, on_delete=models.CASCADE, related_name="assemblies"
    )
    city = models.CharField(max_length=150, blank=True)

    class Meta:
        unique_together = ("name", "district")
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.district})"
