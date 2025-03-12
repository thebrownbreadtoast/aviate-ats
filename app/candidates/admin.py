from django.contrib import admin

from app.base.admin import BaseAdmin
from app.candidates.models import Candidate


@admin.register(Candidate)
class CandidateAdmin(BaseAdmin):
    pass
