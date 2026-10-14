from typing import Protocol


class PatentGateway(Protocol):
    """Puerto para solicitar evaluación legal al servicio de Patentes."""

    def request_formula_review(self, *, formula_id: str, components: list[dict[str, object]]) -> str: ...
