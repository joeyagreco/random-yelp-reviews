from dataclasses import dataclass
from datetime import datetime

from server.model.User import User


@dataclass(frozen=True, kw_only=True)
class Review:
    id: str
    url: str
    text: str
    rating: int
    timeCreated: datetime
    user: User
