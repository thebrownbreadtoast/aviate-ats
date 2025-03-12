from app.base.serializers import BaseModelSerializer
from app.candidates.models import Candidate


class CandidateSerializer(BaseModelSerializer):
    class Meta:
        model = Candidate
        fields = "__all__"
