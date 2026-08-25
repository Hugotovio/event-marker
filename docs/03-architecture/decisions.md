# ADR-011 — Stack tecnológico del MVP

### Estado

Aprobado.

### Contexto

Event Maker necesita un stack moderno, mantenible y adecuado para
una aplicación web con:

- editor de invitaciones;
- API REST;
- PostgreSQL;
- autenticación;
- pagos;
- almacenamiento de archivos;
- pruebas automatizadas.

Además, el stack debe ser suficientemente sencillo para que el MVP
pueda desarrollarse y mantenerse sin una complejidad innecesaria.

### Decisión

El MVP utilizará:

#### Frontend

```text
Next.js
TypeScript
Tailwind CSS