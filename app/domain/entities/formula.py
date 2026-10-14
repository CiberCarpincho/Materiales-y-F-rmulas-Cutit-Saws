from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class FormulaComponent:
    material_id: str
    percentage: float


@dataclass
class Formula:
    id: str
    code: str
    name: str
    technical_application: str
    version: int
    status: str
    components: list[FormulaComponent] = field(default_factory=list)
    patent_ticket_id: str | None = None
    conflicting_patents: list[str] = field(default_factory=list)
    created_at: datetime | None = None
    updated_at: datetime | None = None
