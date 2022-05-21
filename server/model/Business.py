from dataclasses import dataclass
from typing import List

from server.model.Category import Category
from server.model.Location import Location


@dataclass(frozen=True, kw_only=True)
class Business:
    id: str
    name: str
    imageUrl: str
    url: str
    categories: List[Category]
    rating: float
    location: Location
    phone: str
