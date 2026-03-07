from django.contrib import admin
from .models import Assignment


@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):

    list_display = (
        "member",
        "role",
        "department",
        "assembly",
        "district",
        "country",
        "zone",
        "continent",
    )

    list_filter = (
        "department",
        "assembly",
        "district",
        "country",
    )

    search_fields = (
        "member__first_name",
        "member__last_name",
        "role",
    )
