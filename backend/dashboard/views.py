from rest_framework.views import APIView
from rest_framework.response import Response

from members.models import Member
from departments.models import Department
from assignments.models import Assignment


class DashboardView(APIView):

    def get(self, request):

        data = {
            "members_total": Member.objects.count(),
            "members_active": Member.objects.filter(status="ACTIVE").count(),
            "members_inactive": Member.objects.filter(status="INACTIVE").count(),
            "departments_total": Department.objects.count(),
            "assignments_total": Assignment.objects.count(),
        }

        return Response(data)
