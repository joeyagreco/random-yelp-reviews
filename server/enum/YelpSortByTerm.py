from __future__ import annotations

from enum import unique, Enum


@unique
class YelpSortByTerm(Enum):
    """
    Yelp sort-by terms.
    https://www.yelp.com/developers/documentation/v3/business_search#:~:text=sort_by,a%20single%20review.
    """
    BEST_MATCH = "BEST_MATCH"
    DISTANCE = "DISTANCE"
    RATING = "RATING"
    REVIEW_COUNT = "REVIEW_COUNT"
