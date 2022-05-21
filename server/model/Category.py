from dataclasses import dataclass

from server.model.Location import Location


@dataclass(frozen=True, kw_only=True)
class Category:
    alias: str
    title: str