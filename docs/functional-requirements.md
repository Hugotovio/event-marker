# Event Marker — Requisitos Funcionales

## Identidad y Account

- FR-001: El sistema MUST permitir registrar un User.
- FR-002: El sistema MUST autenticar usuarios para recursos privados.
- FR-003: El sistema MUST crear una Account durante el onboarding inicial.
- FR-004: El sistema MUST crear Membership con OWNER para el propietario inicial.
- FR-005: El sistema MUST soportar aislamiento por Account.

## Multi-tenancy

- FR-010: Todo recurso privado MUST pertenecer directa o indirectamente a una Account.
- FR-011: El backend MUST validar ownership/tenant antes de operar sobre un recurso privado.
- FR-012: Un usuario MUST NOT acceder a recursos privados de otra Account.
- FR-013: La autorización MUST ejecutarse en backend.

## Events y Invitations

- FR-020: El sistema MUST permitir crear y editar Events.
- FR-021: El sistema MUST permitir crear Invitation en estado DRAFT.
- FR-022: Una Invitation MUST conservar referencia a Template y Variant.
- FR-023: Los datos de Invitation MUST mantenerse separados de la definición de Template.

## Templates

- FR-030: El sistema MUST listar Templates publicadas disponibles.
- FR-031: Una Template MUST definir componentes y schema de campos.
- FR-032: Una Template MUST poder definir Photo Slots.
- FR-033: Una Template MAY tener múltiples Variants.
- FR-034: Cambiar Variant MUST conservar datos y media compatibles.
- FR-035: Las Templates MUST estar versionadas para evitar cambios destructivos.
- FR-036: Solo administración autorizada MAY publicar o archivar Templates.

## Editor

- FR-040: El sistema MUST generar el editor a partir del schema de la Template.
- FR-041: El usuario MUST poder editar los campos marcados como editables.
- FR-042: El usuario MUST poder cargar fotografías en Photo Slots permitidos.
- FR-043: El sistema MUST validar campos obligatorios antes de publicar.
- FR-044: El sistema MUST proporcionar Preview.
- FR-045: Preview y publicación MUST utilizar el mismo Renderer lógico.

## Publicación

- FR-050: Cada Invitation publicada MUST tener un identificador/slug público no secuencial.
- FR-051: Una Invitation publicada MUST poder visualizarse sin autenticación de User.
- FR-052: Una Invitation DRAFT MUST NOT estar disponible mediante URL pública.
- FR-053: La respuesta pública MUST excluir información privada interna.

## Guest y RSVP

- FR-060: El sistema MUST permitir Guest asociado a Event.
- FR-061: El sistema MUST permitir acceso personalizado mediante token no predecible.
- FR-062: RSVP MUST soportar PENDING, CONFIRMED y DECLINED.
- FR-063: El sistema MUST impedir que un Guest modifique el RSVP de otro Guest.

## Media

- FR-070: Los archivos MUST tener metadata persistida.
- FR-071: El contenido binario SHOULD almacenarse en Object Storage.
- FR-072: Las cargas MUST validar tipo, tamaño y autorización.
- FR-073: Media de una Account MUST permanecer aislada de otras Accounts.

## SaaS

- FR-080: La Subscription MUST pertenecer a una Account.
- FR-081: El Plan MUST definir capabilities y limits.
- FR-082: El backend MUST aplicar los límites independientemente del frontend.
- FR-083: Downgrade MUST NOT borrar automáticamente recursos del usuario.

## Administración

- FR-090: El sistema MUST proporcionar una forma administrativa de gestionar Templates.
- FR-091: Una Template MUST poder pasar por DRAFT, PUBLISHED y ARCHIVED.
- FR-092: La publicación MUST ejecutar validaciones estructurales.
