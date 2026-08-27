# AGENT_INSTRUCTIONS.md

# Event Marker — Instrucciones para agentes de código

Este archivo define las reglas de trabajo para agentes de código de IA que trabajen sobre el repositorio de Event Marker.

---

## 1. Fuente de verdad

La carpeta `docs/` es la **fuente de verdad (Source of Truth)** de Event Marker.

Antes de implementar una funcionalidad o realizar un cambio arquitectónico:

1. Leer `docs/README.md`.
2. Leer la documentación directamente relacionada con la tarea.
3. Consultar `docs/architecture.md`, `docs/data-model.md`, `docs/api.md`, `docs/security.md` y `docs/testing.md` cuando sean relevantes.
4. Respetar la terminología y las decisiones definidas en la documentación.
5. No inventar requisitos que no estén respaldados por la especificación.

Si la implementación existente del repositorio entra en conflicto con la documentación, no se debe modificar silenciosamente la especificación.

Primero se debe informar del conflicto y proponer la modificación mínima y segura.

---

## 2. Ambigüedades y contradicciones

Si dos documentos contienen requisitos contradictorios, o si una decisión de implementación puede modificar de manera importante la arquitectura:

**detener la implementación de esa decisión y consultar al propietario del proyecto.**

No se deben resolver mediante suposiciones las decisiones importantes de negocio o arquitectura.

Los detalles menores de implementación pueden resolverse utilizando las convenciones existentes del proyecto siempre que no cambien el comportamiento especificado.

---

## 3. Arquitectura

Respetar la arquitectura definida en:

`docs/architecture.md`

No introducir:

- microservicios;
- infraestructura innecesaria;
- nuevos proveedores externos;
- nuevas bases de datos;
- nuevos patrones arquitectónicos;

a menos que la documentación lo requiera o el propietario del proyecto lo apruebe explícitamente.

La arquitectura preferida es la arquitectura modular existente, manteniendo una separación clara de responsabilidades.

No sobrearquitectar el proyecto.

---

## 4. Seguridad

Los requisitos de seguridad son obligatorios.

Seguir:

- `docs/security.md`
- `docs/ssldc.md`

Prestar especial atención a:

- autenticación;
- autorización;
- aislamiento multi-tenant;
- propiedad de los recursos;
- validación de entradas;
- manejo seguro de archivos;
- secretos;
- seguridad de dependencias;
- acceso a invitaciones públicas;
- acceso de invitados;
- RSVP;
- prevención de escalamiento horizontal de privilegios.

Nunca confiar únicamente en identificadores, permisos o datos enviados desde el frontend.

El backend debe validar siempre que el usuario tenga autorización sobre el recurso solicitado.

---

## 5. Multi-tenancy

Event Marker utiliza un modelo multi-tenant basado en `Account`.

Todo recurso perteneciente a una Account debe accederse dentro del contexto correcto de esa Account.

Nunca asumir que conocer un `resource_id` significa tener autorización para acceder al recurso.

La cadena conceptual de autorización es:

`usuario autenticado -> Account -> recurso`

Debe evitarse cualquier posibilidad de acceso entre tenants.

Ejemplo:

```text
Usuario
   ↓
Account
   ↓
Event
   ↓
Invitation