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
    CHURCH = "CHURCH"
    CINEMA = "CINEMA"
    COMPUTER = "COMPUTER"
    CONVENIENCE = "CONVENIENCE"
    DEALERSHIP = "DEALERSHIP"
    DELI = "DELI"
    DRY_CLEANING = "DRY_CLEANING"
    FESTIVAL = "FESTIVAL"
    FURNITURE = "FURNITURE"
    GAS = "GAS"
    GROCERY = "GROCERY"
    GYM = "GYM"
    HAIRCUT = "HAIRCUT"
    HOME_IMPROVEMENT = "HOME_IMPROVEMENT"
    HOSPITAL = "HOSPITAL"
    HOTEL = "HOTEL"
    LANDMARK = "LANDMARK"
    LANDSCAPING = "LANDSCAPING"
    LAUNDROMAT = "LAUNDROMAT"
    LIBRARY = "LIBRARY"
    LIQUOR = "LIQUOR"
    MARTIAL_ARTS = "MARTIAL_ARTS"
    MECHANIC = "MECHANIC"
    MUSEUM = "MUSEUM"
    MUSIC = "MUSIC"
    RESTAURANT = "RESTAURANT"
    RETAIL = "RETAIL"
    PET = "PET"
    PLANT = "PLANT"
    REAL_ESTATE = "REAL_ESTATE"
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
        return list(map(lambda c: c, cls))
