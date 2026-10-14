# Mapeo de backlog a componentes

| Historias | Funcionalidad | API prevista | Componentes principales |
|---|---|---|---|
| HU-01 | Registrar material y crear artículo asociado | `POST /api/v1/materiales` | `api/v1/endpoints/materials.py`, `schemas/material.py`, `application/use_cases/materials.py`, puerto `InventoryGateway`, entidad `Material`, repositorio y cliente Inventario. |
| HU-02 | Consultar material y filtrar catálogo | `GET /api/v1/materiales`, `GET /api/v1/materiales/{id}` | Endpoint, schemas, caso de uso de consulta, `MaterialRepository`. |
| HU-03 | Modificar material activo y sincronizar Inventario | `PUT /api/v1/materiales/{id}` | Caso de uso, reglas de estado, repositorio y `InventoryGateway`. |
| HU-04 | Desactivar material (borrado lógico) | `PATCH /api/v1/materiales/{id}/desactivar` | Caso de uso, entidad/estado y repositorio. |
| HU-05 | Crear fórmula borrador | `POST /api/v1/formulas` | `formulas.py`, `schemas/formula.py`, caso de uso, entidades `Formula` y `FormulaComponent`, validación de materiales activos. |
| HU-06 | Listar/consultar fórmula y composición | `GET /api/v1/formulas`, `GET /api/v1/formulas/{id}` | Endpoint, schemas, consultas/repositorio y paginación/filtros. |
| HU-07 | Modificar componentes de fórmula editable | `PUT /api/v1/formulas/{id}` | Caso de uso, invariantes de porcentajes/estado, repositorio y versionado. |
| HU-08 | Descontinuar fórmula | `PATCH /api/v1/formulas/{id}/descontinuar` | Caso de uso, transición de estado y repositorio. |
| HU-09 | Solicitar evaluación legal | `POST /api/v1/formulas/{id}/evaluacion-patente` | Caso de uso, puerto `PatentGateway`, cliente Patentes, ticket y transición transaccional. |
| HU-10 (Should) | Recibir/consultar dictamen legal | `POST /api/v1/formulas/{id}/dictamen-patente` y consulta del detalle | Validación de ticket/estado, persistencia de resultado y códigos en conflicto. |

## Reglas transversales del backlog

- Validar y normalizar nombres antes de persistir; unicidad de materiales sin distinguir mayúsculas/minúsculas.
- Materiales y fórmulas usan borrado lógico/estados; la consulta admite los estados especificados.
- Validar reglas de composición (al menos dos materiales activos y porcentajes que sumen exactamente 100%).
- Respuestas distinguen errores de validación, duplicados/conflictos, inexistencia, dependencia no disponible y falla de persistencia conforme a cada criterio de aceptación.
- Timeout externo: 5 segundos; los errores técnicos registran `traceId`. Persistencia local transaccional con rollback.
- El servicio de materiales no administra existencias ni descuenta insumos; eso pertenece a Inventario.
