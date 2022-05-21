from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, kw_only=True)
class Location:
    address1: str
    address2: str
    address3: str
    city: str
    zipCode: str
    country: str
    state: str
    displayAddress: List[str]
