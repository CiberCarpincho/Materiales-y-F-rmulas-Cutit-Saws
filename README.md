# Cutit - Materiales y Fórmulas

Servicio backend REST con FastAPI para administrar el catálogo técnico de materiales y el ciclo de vida de las fórmulas de Cutit. La estructura separa el dominio de la API, la persistencia y los servicios externos.

## Inicio local

1. Crear un entorno virtual e instalar el proyecto: `python -m pip install -e .`
2. Copiar `.env.example` a `.env` y ajustar la configuración de base de datos.
3. Ejecutar `uvicorn app.main:app --reload` desde esta carpeta.
4. Consultar OpenAPI en `/docs` y la verificación de disponibilidad en `/health`.

La configuración inicial usa SQLite como valor local para facilitar el arranque; el adaptador de persistencia se puede cambiar sin modificar el dominio. Las integraciones externas quedan configurables y deben habilitarse al implementar sus historias.

## Capas

- `api`: rutas HTTP, dependencias y traducción de solicitudes/respuestas.
- `schemas`: contratos Pydantic de entrada y salida.
- `application`: casos de uso y puertos que definen lo que requiere la aplicación.
- `domain`: entidades, reglas, estados y errores propios del negocio.
- `infrastructure`: base de datos, repositorios, clientes de Inventario/Patentes y observabilidad.
- `migrations`: evolución versionada del esquema de datos.
- `tests`: ubicación prevista para pruebas unitarias e integración.

Dirección de dependencias: `api -> application -> domain`; infraestructura implementa los puertos de aplicación. El dominio no depende de FastAPI, SQLAlchemy ni clientes HTTP.

## Alcance funcional inicial

HU-01 a HU-04 implementan materiales; HU-05 a HU-08 implementan fórmulas; HU-09 inicia la evaluación de patentes y HU-10 procesa/consulta el dictamen externo. HU-10 está priorizada como Should. El mapeo detallado está en `docs/backlog-mapping.md`.

Las carpetas contienen puntos de extensión, no la implementación completa de las historias. Las reglas de validación, mensajes, transacciones y contratos se deben implementar desde los criterios de aceptación del backlog.
