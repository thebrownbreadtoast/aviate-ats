from django.db.models import Case, IntegerField, Value, When

from app.base.viewsets import BaseModelViewSet
from app.candidates.models import Candidate
from app.candidates.serializers import CandidateSerializer


class CandidateViewSet(BaseModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        search_query = self.request.query_params.get("search", "")

        if search_query:
            words = [word.strip() for word in search_query.split() if word.strip()]

            if not words:
                return Candidate.objects.none()

            relevancy_expr = Value(0, output_field=IntegerField())

            for word in words:
                case_expr = Case(
                    When(name__icontains=word, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )

                relevancy_expr += case_expr

            queryset = (
                queryset.annotate(relevancy=relevancy_expr)
                .filter(relevancy__gt=0)
                .order_by("-relevancy", "name")
            )

        return queryset
