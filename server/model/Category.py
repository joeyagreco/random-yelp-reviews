from dataclasses import dataclass


@dataclass(frozen=True, kw_only=True)
class Category:
    alias: str
    title: str
