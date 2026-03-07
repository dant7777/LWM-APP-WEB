from rest_framework import viewsets
from .models import Member
from .serializers import MemberSerializer


class MemberViewSet(viewsets.ModelViewSet):

    queryset = Member.objects.all()
    serializer_class = MemberSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        assembly = self.request.query_params.get("assembly")
        district = self.request.query_params.get("district")
        country = self.request.query_params.get("country")
        zone = self.request.query_params.get("zone")
        continent = self.request.query_params.get("continent")

        if assembly:
            queryset = queryset.filter(assembly_id=assembly)

        if district:
            queryset = queryset.filter(assembly__district_id=district)

        if country:
            queryset = queryset.filter(assembly__district__country_id=country)

        if zone:
            queryset = queryset.filter(assembly__district__country__zone_id=zone)

        if continent:
            queryset = queryset.filter(
                assembly__district__country__zone__continent_id=continent
            )

        return queryset
