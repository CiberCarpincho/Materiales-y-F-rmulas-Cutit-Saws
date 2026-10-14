from dataclasses import dataclass
from datetime import datetime


@dataclass
class Material:
    id: str
    sku: str
    name: str
    category: str
    unit: str
    density: float
    purity: float
    status: str
    created_at: datetime
    updated_at: datetime
