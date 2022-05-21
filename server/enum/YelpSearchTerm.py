from __future__ import annotations

from enum import unique, Enum


@unique
class YelpSearchTerm(Enum):
    """
    Yelp search terms.
    """
    AMUSEMENT = "AMUSEMENT"
    ARCADE = "ARCADE"
    ART = "ART"
    AUTO = "AUTO"
    BANK = "BANK"
    BAR = "BAR"
    BOWLING = "BOWLING"
    COMPUTER = "COMPUTER"
    CONVENIENCE = "CONVENIENCE"
    DEALERSHIP = "DEALERSHIP"
    FURNITURE = "FURNITURE"
    GAS = "GAS"
    GROCERY = "GROCERY"
    GYM = "GYM"
    HAIRCUT = "HAIRCUT"
    HIGHEST_REVIEWED = "HIGHEST_REVIEWED"
    HOME_IMPROVEMENT = "HOME_IMPROVEMENT"
    HOSPITAL = "HOSPITAL"
    HOTEL = "HOTEL"
    LIQUOR = "LIQUOR"
    LOWEST_REVIEWED = "LOWEST_REVIEWED"
    MARTIAL_ARTS = "MARTIAL_ARTS"
    MECHANIC = "MECHANIC"
    MUSIC = "MUSIC"
    RESTAURANT = "RESTAURANT"
    RETAIL = "RETAIL"
    PET = "PET"
    PLANT = "PLANT"
    SALON = "SALON"
    SCHOOL = "SCHOOL"
    SMOKE = "SMOKE"
    SPA = "SPA"
    THEATER = "THEATER"
    TRAVEL = "TRAVEL"
    VAPE = "VAPE"
    VET = "VET"
    YOGA = "YOGA"

    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
