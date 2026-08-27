# Event Marker — API

## Base

```text
/api/v1
```

REST + JSON, salvo cargas de archivos multipart cuando sea necesario.

## Autenticación

Las rutas privadas requieren autenticación. Las rutas públicas de invitaciones no requieren autenticación de User.

La implementación puede utilizar access token/sesión segura; el mecanismo concreto debe mantenerse detrás de un servicio de identidad.

## Recursos

```text
/api/v1/auth
/api/v1/accounts
/api/v1/memberships
/api/v1/clients
/api/v1/events
/api/v1/templates
/api/v1/invitations
/api/v1/media
/api/v1/guests
/api/v1/rsvp
/api/v1/plans
/api/v1/subscriptions
/api/v1/billing
/api/v1/admin/templates
```

## Contratos principales

### Templates

```text
GET /api/v1/templates
GET /api/v1/templates/{id}
```

Solo Templates disponibles para el catálogo se exponen a usuarios normales.

### Invitations

```text
POST /api/v1/invitations
GET /api/v1/invitations/{id}
PUT /api/v1/invitations/{id}
PATCH /api/v1/invitations/{id}
PUT /api/v1/invitations/{id}/variant
POST /api/v1/invitations/{id}/preview
POST /api/v1/invitations/{id}/publish
```

### Media

```text
POST /api/v1/invitations/{id}/media
DELETE /api/v1/media/{id}
```

El mecanismo puede evolucionar a signed upload URLs sin cambiar el contrato de dominio.

### Public Invitation

```text
GET /i/{public_slug}
```

Debe resolver únicamente una Invitation publicada y devolver una representación pública.

### Guest / RSVP

```text
GET /g/{guest_token}
POST /g/{guest_token}/rsvp
```

Los tokens son secretos de acceso y no deben registrarse en logs.

## Problem Details

Los errores utilizarán una estructura consistente basada en Problem Details. Nunca se expondrán stack traces ni secretos.

## Autorización

Nunca debe utilizarse un ID recibido del cliente como prueba de pertenencia. La operación debe comprobar:

```text
Authenticated User
 ↓
Membership
 ↓
Account
 ↓
Resource ownership
```

## PUT / PATCH

- PUT: reemplazo completo del conjunto de campos permitidos.
- PATCH: actualización parcial.
- IDs, ownership y timestamps administrados por sistema son inmutables.

## Idempotencia

Operaciones sensibles a reintentos, especialmente billing/webhooks, deberán soportar idempotency keys o identificadores únicos del proveedor.
