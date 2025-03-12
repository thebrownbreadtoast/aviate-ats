from app.base.routers import BaseRouter
from app.candidates.viewsets import CandidateViewSet

candidate_router = BaseRouter()

candidate_router.register("candidates", CandidateViewSet, basename="candidates-v1")
