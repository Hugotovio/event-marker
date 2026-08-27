# Event Marker — Estrategia de Testing

## Objetivo

Detectar errores temprano, proteger contratos y evitar regresiones.

## Desarrollo local

Durante la etapa actual, los tests funcionales se ejecutan principalmente en local.

Backend:

```powershell
python -m pytest backend\tests -v
```

## Capas

### Unit tests

Para dominio, validaciones, reglas, servicios puros y transformaciones.

### Integration tests

Para PostgreSQL, repositorios, migraciones y colaboración entre módulos.

### API tests

Para endpoints, DTOs, autenticación y autorización.

### Security tests

Para aislamiento multi-tenant, acceso indebido, validación de archivos, tokens y límites.

### E2E

Se incorporarán progresivamente para los flujos críticos del usuario.

## Casos críticos

Como mínimo se deben cubrir:

- creación de Account;
- aislamiento entre Accounts;
- creación de Event;
- creación de Invitation;
- edición de datos;
- cambio de Variant sin pérdida de datos;
- upload de Media;
- validación antes de publicación;
- publicación y URL pública;
- Guest token;
- RSVP;
- aplicación de limits;
- Templates versionadas.

## Fixtures

Los tests deben utilizar datos controlados y aislados. No depender de servicios productivos.

## Migraciones

Las migraciones Alembic deben poder ejecutarse sobre una base limpia y sobre una base existente de prueba.

## Coverage

Coverage es una métrica auxiliar, no el único criterio de calidad. Se prioriza cubrir reglas críticas y caminos de seguridad.

## CI

GitHub Actions puede ejecutar:

```text
lint / checks
security scan
pip-audit
pytest
```

La composición exacta podrá separarse en workflows conforme crezca el proyecto.
