# Event Marker — Reglas de Negocio

## Account

- RN-001: Account es la frontera lógica de multi-tenancy.
- RN-002: User puede pertenecer a una o más Accounts mediante Membership si la evolución del producto lo requiere.
- RN-003: La primera Membership creada para el propietario es OWNER.
- RN-004: Los recursos privados deben resolverse dentro del contexto de Account.

## Client

- RN-010: Client pertenece a una Account.
- RN-011: Client no requiere una cuenta de acceso.
- RN-012: Un Client puede estar asociado a múltiples Events de su Account según el modelo implementado.

## Event

- RN-020: Event pertenece obligatoriamente a una Account.
- RN-021: Event puede asociarse opcionalmente a Client de la misma Account.
- RN-022: No se permite asociación cross-tenant.

## Invitation

- RN-030: Invitation pertenece a un Event y, por derivación, a una Account.
- RN-031: Invitation inicia como DRAFT.
- RN-032: Solo Invitation válida puede publicarse.
- RN-033: Una Invitation publicada tiene URL pública no predecible.
- RN-034: Cambios en draft no deben exponer datos incompletos como versión publicada.

## Template

- RN-040: Template es propiedad de la plataforma, no del cliente final.
- RN-041: Solo Templates PUBLISHED aparecen en el catálogo normal.
- RN-042: Template define estructura; Invitation contiene datos.
- RN-043: Componentes permitidos son conocidos por el sistema.
- RN-044: No se permite código ejecutable arbitrario dentro de una Template de usuario.
- RN-045: Las versiones publicadas son inmutables; cambios generan nueva versión.

## Media

- RN-050: Media de cliente pertenece al contexto de Invitation/Account.
- RN-051: La base de datos guarda metadata y referencia de almacenamiento; el archivo reside en Object Storage.
- RN-052: El acceso a Media privada requiere autorización.
- RN-053: Un Guest solo recibe Media que forma parte de una Invitation publicada.

## Guest / RSVP

- RN-060: Guest pertenece a un Event.
- RN-061: El token de Guest debe ser no predecible y revocable.
- RN-062: RSVP inicia en PENDING.
- RN-063: Guest solo puede modificar su propia respuesta mediante su mecanismo de acceso.

## SaaS

- RN-070: Subscription pertenece a Account.
- RN-071: Plan define capabilities y limits; no se debe dispersar lógica basada en nombres de plan por el código.
- RN-072: Exceder un límite bloquea la acción que incrementaría el uso, salvo política explícita.
- RN-073: Downgrade no elimina automáticamente datos.
- RN-074: Provider de pagos queda detrás de una abstracción de Billing.
