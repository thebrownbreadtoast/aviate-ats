from app.base.viewsets import BaseModelViewSet
from app.candidates.models import Candidate
from app.candidates.serializers import CandidateSerializer


class CandidateViewSet(BaseModelViewSet):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer
