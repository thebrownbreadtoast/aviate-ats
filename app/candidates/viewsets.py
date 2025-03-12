from django.db.models import Case, IntegerField, Value, When
from rest_framework.decorators import action

from app.base import responses
from app.base.viewsets import BaseModelViewSet
from app.candidates.models import Candidate
from app.candidates.serializers import CandidateSerializer


class CandidateViewSet(BaseModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    def get_relevant_candidates(self, query):
        queryset = self.get_queryset()

        words = [word.strip() for word in query.split() if word.strip()]

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

    def list(self, request):
        return responses.NotImplemented(
            {"error": "List API not implemented for this resource."}
        )

    @action(detail=False, methods=["GET"])
    def search(self, request):
        query = request.query_params.get("q", "")

        if not query:
            return responses.BadRequest({"error": "Please enter valid search query."})

        relevant_candidates_qs = self.get_relevant_candidates(query)

        serializer = self.get_serializer(relevant_candidates_qs, many=True)

        return responses.Ok(serializer.data)
