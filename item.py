from dataclasses import dataclass
from datetime import datetime


@dataclass
class Item:
    title: str
    dt: datetime
    link: str
    description: str
