from enum import IntEnum


class ChoiceMixin(IntEnum):
    """
    Inherit this class in the types of choice for choices attribute in
    models.IntegerField
    """

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]

    @classmethod
    def values_list(cls):
        """
        Helper method which can be used to fetch values of a ChoicMixin object
        """
        return [key.value for key in cls]
