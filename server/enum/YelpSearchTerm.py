from __future__ import annotations

from enum import unique, Enum


@unique
class YelpSearchTerm(Enum):
    """
    Yelp search terms.
    """
    ARCADE = "ARCADE"
    ART = "ART"
    BAR = "BAR"
    BOWLING = "BOWLING"
    COMPUTER = "COMPUTER"
    CONVENIENCE = "CONVENIENCE"
    FURNITURE = "FURNITURE"
    GAS = "GAS"
    GROCERY = "GROCERY"
    GYM = "GYM"
    HIGHEST_REVIEWED = "HIGHEST_REVIEWED"
    LOWEST_REVIEWED = "LOWEST_REVIEWED"
    MARTIAL_ARTS = "MARTIAL_ARTS"
    MECHANIC = "MECHANIC"
    MUSIC = "MUSIC"
    RESTAURANT = "RESTAURANT"
    RETAIL = "RETAIL"
    HAIRCUT = "HAIRCUT"
    HOSPITAL = "HOSPITAL"
    PET = "PET"
    PLANT = "PLANT"
    SALON = "SALON"
    SCHOOL = "SCHOOL"
    SPA = "SPA"
    YOGA = "YOGA"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
