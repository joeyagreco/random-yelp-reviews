from __future__ import annotations

from enum import unique, Enum


@unique
class YelpSearchTerm(Enum):
    """
    Yelp search terms.
    """
    BAR = "BAR"
    GROCERY = "GROCERY"
    GYM = "GYM"
    HIGHEST_REVIEWED = "HIGHEST_REVIEWED"
    LOWEST_REVIEWED = "LOWEST_REVIEWED"
    MECHANIC = "MECHANIC"
    RESTAURANT = "RESTAURANT"
    RETAIL = "RETAIL"
    HAIRCUT = "HAIRCUT"
    HOSPITAL = "HOSPITAL"
    PET = "PET"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
