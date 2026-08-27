# Event Marker — Documentación

## Propósito

Event Marker es una plataforma SaaS para crear, personalizar, publicar y compartir invitaciones digitales para eventos. La invitación es el primer producto de una plataforma que puede evolucionar hacia experiencias digitales alrededor de eventos.

## Perfiles de uso

- Personas que crean sus propias invitaciones.
- Diseñadores y profesionales de eventos que gestionan trabajos para clientes.
- Empresas que administran múltiples eventos, clientes e invitaciones.

## Arquitectura base

- Monolito modular durante el MVP.
- Multi-tenancy mediante `Account`.
- PostgreSQL para datos estructurados.
- Object Storage para archivos.
- Templates estructuradas y versionadas.
- Editor guiado y Renderer común para preview/publicación.
- Seguridad integrada al ciclo de desarrollo.

## Documentos

| Documento | Propósito |
|---|---|
| `product-overview.md` | Visión, usuarios y propuesta de valor |
| `scope-mvp.md` | Alcance del MVP |
| `user-flows.md` | Flujos principales |
| `functional-requirements.md` | Requisitos funcionales |
| `business-rules.md` | Reglas de negocio |
| `data-model.md` | Modelo de datos |
| `erd.md` | Relaciones entre entidades |
| `architecture.md` | Arquitectura técnica |
| `api.md` | Contratos y convenciones API |
| `security.md` | Seguridad |
| `testing.md` | Estrategia de pruebas |
| `ssdlc.md` | Desarrollo seguro |
| `roadmap.md` | Evolución del producto |
| `decisions.md` | Decisiones aprobadas |

## Estado

Especificación consolidada a partir de las decisiones aprobadas durante el rediseño del producto. Los valores comerciales concretos y algunos proveedores se consideran decisiones de implementación/comercialización posteriores.

## Principios

1. Spec-Driven Development.
2. Monolito modular antes que microservicios.
3. Seguridad desde el diseño.
4. Account como frontera de multi-tenancy.
5. Template separada de Invitation y de sus datos.
6. PostgreSQL separado de Object Storage.
7. Preview y publicación utilizan el mismo Renderer.
8. Versionado para evitar cambios destructivos.
9. No introducir complejidad empresarial antes de validar la necesidad.
