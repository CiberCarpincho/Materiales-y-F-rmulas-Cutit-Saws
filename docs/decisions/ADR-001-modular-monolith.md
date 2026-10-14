# ADR-001: Servicio modular por capas con puertos y adaptadores

- Estado: Aceptada para el esqueleto inicial.
- Contexto: Cutit requiere evolucionar desde el hub heredado, atender demanda variable y facilitar integraciones futuras.
- Decisión: Iniciar con un servicio FastAPI modular, dominio aislado y adaptadores intercambiables para base de datos y dependencias HTTP.
- Consecuencias: Menor complejidad operativa inicial; los límites de módulos y contratos permiten separar servicios cuando exista una necesidad medida. La separación actual no equivale todavía a microservicios desplegados.
