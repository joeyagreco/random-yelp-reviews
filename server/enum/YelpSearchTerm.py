from __future__ import annotations

from enum import unique, Enum


@unique
class YelpSearchTerm(Enum):
    """
    Yelp search terms.
    """
    HIGHEST_REVIEWED = "HIGHEST_REVIEWED"
    LOWEST_REVIEWED = "LOWEST_REVIEWED"
    
    @classmethod
    def list(cls):
        return list(map(lambda c: c.value, cls))
