from typing import Protocol


class InventoryGateway(Protocol):
    """Puerto para crear/actualizar artículo en el servicio Inventario."""

    def register_raw_material(self, *, name: str, unit: str) -> str: ...
    def update_article(self, *, sku: str, name: str, unit: str) -> None: ...
