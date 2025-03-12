from django.db import models
from django.core.validators import RegexValidator

from app.base.models import BaseModel
from app.candidates.types import GenderTypes


class Candidate(BaseModel):    
    name = models.CharField(max_length=255)
    age = models.PositiveSmallIntegerField(default=18)
    gender = models.PositiveSmallIntegerField(choices=GenderTypes.choices(), default=GenderTypes.MALE)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(
        max_length=32,
        validators=[
            RegexValidator(regex=r"^[6-9][\d]{9}$"),
        ],
    )

    def __str__(self):
        return self.email
