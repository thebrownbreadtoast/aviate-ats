from rest_framework import mixins, viewsets


class BaseViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    """Base ViewSet class to be inherited by other ViewSet classes."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class BaseModelViewSet(viewsets.ModelViewSet):
    """ModelViewSet class to be inherited by other ViewSet classes where CRUD
    operations on model are required."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
