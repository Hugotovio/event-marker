# Event Marker — SSDLC

## Objetivo

Integrar seguridad en todas las etapas del desarrollo y no como una revisión final.

## Flujo

```text
Idea
 ↓
Specification
 ↓
Threat / Security Considerations
 ↓
Design
 ↓
Implementation
 ↓
Local Tests
 ↓
Security Checks
 ↓
Code Review
 ↓
CI
 ↓
Deploy
 ↓
Monitor / Improve
```

## Security gates

### Requirements

Identificar desde la especificación:

- datos públicos/privados;
- autenticación;
- autorización;
- multi-tenancy;
- archivos;
- pagos;
- límites de abuso.

### Design

Definir trust boundaries y controles antes de implementar.

### Implementation

Aplicar validación, autorización server-side, manejo seguro de secretos y dependencias actualizadas.

### Verification

- pytest;
- pruebas de autorización;
- Bandit;
- pip-audit;
- revisión de cambios.

### CI/CD

GitHub Actions actúa como gate automatizado para controles configurados.

## GitHub Actions actual

El workflow de seguridad ejecuta:

```text
checkout
 ↓
setup Python
 ↓
install dependencies
 ↓
Bandit
 ↓
pip-audit
```

Conforme crezca el proyecto, se recomienda separar workflows de test, seguridad y deployment cuando hacerlo reduzca tiempos o facilite mantenimiento.

## Principio de cambio mínimo

No todos los controles tienen que ejecutarse ante cada cambio. Los workflows pueden utilizar filtros por rutas cuando exista una justificación clara, sin sacrificar controles esenciales.
