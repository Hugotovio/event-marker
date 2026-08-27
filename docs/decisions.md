# Event Marker — Decision Log

## ADR-001 — Monolito modular

**Estado:** Aprobado.

El MVP utilizará un monolito modular. Los módulos mantienen límites claros y podrán extraerse posteriormente si existe evidencia suficiente.

## ADR-002 — Account como tenant

**Estado:** Aprobado.

Account es la frontera lógica de aislamiento de recursos privados.

## ADR-003 — User separado de Account

**Estado:** Aprobado.

User representa identidad; Account representa espacio de trabajo. Membership conecta ambos.

## ADR-004 — SaaS por Account

**Estado:** Aprobado.

La suscripción pertenece a Account y permite múltiples eventos/invitaciones según límites.

## ADR-005 — Plan basado en capabilities y limits

**Estado:** Aprobado.

El código no debe depender repetidamente de nombres de planes. Las capacidades y límites son la abstracción.

## ADR-006 — Template separada de Invitation

**Estado:** Aprobado.

Template define diseño/estructura; Invitation contiene datos y media específicos.

## ADR-007 — Templates estructuradas

**Estado:** Aprobado.

No serán imágenes planas. Se compondrán de Components, Fields, Photo Slots, Theme y Variants.

## ADR-008 — Template versioning

**Estado:** Aprobado.

Una versión publicada no se modifica destructivamente. Los cambios generan una nueva versión.

## ADR-009 — Renderer común

**Estado:** Aprobado.

Preview y publicación utilizan el mismo Renderer lógico para reducir divergencias.

## ADR-010 — PostgreSQL + Object Storage

**Estado:** Aprobado.

PostgreSQL almacena datos estructurados y metadata; Object Storage almacena binarios.

## ADR-011 — Storage abstraction

**Estado:** Aprobado.

La aplicación utiliza un puerto/servicio de almacenamiento para desacoplar proveedor y facilitar desarrollo local.

## ADR-012 — JSONB para Invitation.data

**Estado:** Aprobado.

El contenido variable de una Invitation se almacena en JSONB y se valida contra el schema de su Template.

## ADR-013 — Public invitation sin login

**Estado:** Aprobado.

Una Invitation publicada es accesible mediante URL pública sin autenticación de User.

## ADR-014 — Guest token

**Estado:** Aprobado.

El acceso personalizado de Guest utiliza un token no predecible y revocable. No se considera equivalente a una identidad autenticada completa.

## ADR-015 — Sin código arbitrario en Templates

**Estado:** Aprobado.

No se permitirá JavaScript/CSS/HTML arbitrario de usuarios en el MVP.

## ADR-016 — Seguridad integrada

**Estado:** Aprobado.

Bandit, pip-audit, pruebas de seguridad y controles de autorización forman parte del SSDLC.

## ADR-017 — Tests funcionales principalmente en local durante la etapa actual

**Estado:** Aprobado.

CI ejecutará controles seleccionados; los tests de desarrollo seguirán ejecutándose localmente hasta que el proyecto requiera otra estrategia.

## ADR-018 — Evolución gradual

**Estado:** Aprobado.

No se introducirán microservicios, editor tipo Canva, marketplace o infraestructura avanzada hasta que una necesidad real lo justifique.
