from enum import StrEnum


class MaterialStatus(StrEnum):
    ACTIVE = "ACTIVO"
    INACTIVE = "INACTIVO"


class FormulaStatus(StrEnum):
    DRAFT = "BORRADOR"
    PATENT_REVIEW = "EVALUANDO_PATENTE"
    APPROVED = "APROBADA"
    REJECTED = "RECHAZADA_POR_INFRACCION"
    DISCONTINUED = "DESCONTINUADA"
