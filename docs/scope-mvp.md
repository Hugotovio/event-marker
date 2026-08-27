# Event Marker — Alcance del MVP

## Objetivo

Construir una primera versión funcional de la plataforma SaaS que permita crear, personalizar, publicar y compartir invitaciones digitales.

## Incluido

### Account e identidad
- Registro e inicio de sesión.
- Creación automática de Account.
- Membership y rol OWNER.
- Perfil básico.
- Recuperación de acceso según mecanismo implementado.

### Eventos
- Crear, consultar y editar eventos.
- Asociación opcional de Client.
- Estado básico del evento.

### Templates
- Catálogo de templates publicadas.
- Templates estructuradas.
- Components y Fields.
- Photo Slots.
- Themes y Variants.
- Versionado básico.
- Template Manager administrativo básico.

### Invitation Editor
- Crear invitation draft.
- Edición guiada.
- Carga de fotografías.
- Cambio de variant sin perder datos.
- Preview.
- Guardado de draft.
- Validación antes de publicar.

### Publicación
- URL pública no secuencial.
- Renderizado de invitation publicada.
- Metadata básica para compartir.
- Compartir enlace y generación de QR.

### Guests / RSVP
- Guest básico asociado a Event.
- Acceso mediante token no predecible.
- RSVP `PENDING`, `CONFIRMED`, `DECLINED`.
- Actualización de respuesta.

### SaaS
- Planes conceptuales Free, Personal y Professional.
- Capabilities y Limits.
- Subscription desacoplada del proveedor de pagos.
- Control básico de usage.
- Upgrade/downgrade preparado arquitectónicamente.

### Seguridad y calidad
- Autenticación y autorización.
- Aislamiento multi-tenant.
- Validación de entradas y archivos.
- Gestión segura de secretos.
- Bandit.
- pip-audit.
- Tests locales como práctica principal durante la etapa actual.
- GitHub Actions para controles automatizados seleccionados.

## Fuera del MVP

- Marketplace de templates de terceros.
- Editor drag-and-drop tipo Canva.
- JavaScript/CSS/HTML arbitrario por usuarios.
- Equipos empresariales avanzados.
- White-label completo.
- Billing internacional complejo.
- Analítica avanzada.
- Campañas masivas.
- Aplicación móvil nativa.
- Microservicios.

## Criterio

Toda funcionalidad nueva debe justificarse frente al flujo principal y documentarse antes de implementarse.
