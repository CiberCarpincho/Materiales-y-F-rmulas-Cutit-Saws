# Arquitectura inicial

## Contexto y objetivo

Este servicio cubre el subdominio Materiales y Fórmulas. Sustituye una parte del hub heredado por un servicio modular, desplegable y escalable de forma incremental, en línea con la decisión SOA del caso Cutit.

## Estilo

Monolito modular por capas con puertos y adaptadores. Cada módulo puede evolucionar y desplegarse como servicio independiente si la demanda lo exige. La API REST versionada es la frontera de entrada; Inventario y Patentes son dependencias externas detrás de adaptadores HTTP.

## Capas y responsabilidades

| Capa | Ubicación | Responsabilidad |
|---|---|---|
| Presentación | `app/api` | Rutas, dependencias y códigos HTTP; no contiene reglas de negocio. |
| Contratos | `app/schemas` | Validación y serialización de DTOs Pydantic. |
| Aplicación | `app/application` | Casos de uso, transacciones y puertos de salida. |
| Dominio | `app/domain` | Entidades, estados, invariantes y transiciones. |
| Infraestructura | `app/infrastructure` | SQLAlchemy, repositorios, clientes externos y telemetría. |
| Base de datos | `migrations` | Cambios versionados y reproducibles del esquema. |
| Operación | raíz, `.github/workflows` | Configuración, contenedor y automatización de CI/CD. |

## Integraciones críticas

- Inventario: al crear un material, solicitar la materia prima y guardar el SKU retornado. El backlog advierte que un fallo local posterior puede dejar un artículo huérfano en Inventario; se debe registrar SKU y `traceId` para conciliación. En actualizaciones, coordinar con Inventario según el contrato acordado.
- Patentes: solicitar evaluación de una fórmula aprobable y guardar el ticket; aceptar el dictamen con validación de estado/ticket y registrar patentes en conflicto.
- Aplicar timeout de 5 s a ambas integraciones, mapear fallas a errores de servicio y evitar guardar transiciones parciales. Definir reintentos/idempotencia con los equipos externos antes de activarlos.

## Persistencia y transacciones

La configuración local usa SQLite para arranque rápido; `DATABASE_URL` permite configurar el motor de despliegue. El esquema definitivo, índices, restricciones, estrategia de concurrencia y respaldo deben decidirse con requisitos de operación. Las operaciones locales deben ser transaccionales y hacer rollback ante fallas.

## Trazabilidad y seguridad

Generar/propagar `traceId` por solicitud, incluirlo en respuestas de error aplicables y logs estructurados; nunca registrar secretos. Configurar autenticación/autorización y gestión de secretos antes de producción, pues no están especificadas en el backlog recibido.

## Entrega y operación

El Dockerfile sirve como base de empaquetado. Añadir CI para instalación, análisis estático y pruebas; desplegar por ambientes con configuración externa, migraciones controladas, health checks y métricas/logs. La automatización queda como estructura, no como pipeline implementado todavía.

## Decisiones pendientes

Motor productivo, autenticación, versionado de API, contrato real de Inventario/Patentes, política de idempotencia/reintentos, retención de auditoría y objetivos SLO. No se inventan decisiones que el backlog/caso no fijan.
