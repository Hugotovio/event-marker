# Event Marker — Seguridad

## Objetivo

La seguridad es una propiedad del producto y forma parte de Definition of Done.

## Identidad

- Contraseñas nunca se almacenan en texto plano.
- Secretos fuera del repositorio.
- Sesiones/tokens con expiración y revocación según mecanismo elegido.
- Rate limiting en operaciones sensibles.

## Autorización y multi-tenancy

La autorización se ejecuta en backend:

```text
User
 ↓
Membership
 ↓
Account
 ↓
Resource
```

Debe prevenirse acceso horizontal entre Accounts.

## Public data boundary

Las invitaciones públicas reciben un DTO específico. No se serializan directamente entidades internas completas.

Nunca deben exponerse:

- password hashes;
- access token hashes;
- subscription/payment internals innecesarios;
- storage credentials;
- información privada de otros Guests.

## Guest tokens

- Aleatorios y no secuenciales.
- No contienen PII.
- Almacenamiento seguro del secreto/hash cuando sea aplicable.
- Revocables.
- No deben aparecer en logs.

## Media

Validar:

- tamaño;
- MIME/type permitido;
- autorización;
- cuota;
- asociación con Invitation/Account.

No aceptar archivos ejecutables como si fueran imágenes.

## Templates

Las Templates del sistema están controladas por administración. No se permite JavaScript, HTML o CSS arbitrario suministrado por usuarios en el MVP.

## Input validation

Todas las entradas externas se validan en backend con esquemas y reglas de dominio. La validación del frontend no sustituye la del backend.

## Dependencias

- `Bandit` para análisis estático de seguridad Python.
- `pip-audit` para vulnerabilidades de dependencias.
- Dependencias fijadas/revisadas de forma periódica.

## CI

GitHub Actions ejecutará controles automatizados apropiados. Durante la etapa actual, los tests funcionales se ejecutan principalmente en local y los controles de seguridad seleccionados en CI.

## Secretos

`.env` y credenciales reales no se versionan. CI utiliza secrets/variables del entorno cuando sean necesarios.

## Billing

Los webhooks de pago deben validar firma, evento, proveedor y unicidad antes de modificar una Subscription.

## Logging

No registrar contraseñas, tokens, contenido privado de invitaciones ni secretos. Los logs deben ser útiles para diagnóstico sin convertirse en una fuente de filtración.
