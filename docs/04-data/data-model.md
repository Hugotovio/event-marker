# Event Maker — Modelo de Datos

## 1. Objetivo

Este documento define el modelo de datos relacional del MVP de Event Maker.

El modelo debe representar:

- plantillas de invitaciones;
- variantes visuales;
- invitaciones creadas por los clientes;
- información personalizada de cada invitación;
- fotografías asociadas a las invitaciones;
- estados de las invitaciones;
- publicación mediante URL pública;
- integridad referencial;
- restricciones necesarias para mantener la consistencia de los datos.

El diseño mantiene una separación clara entre:

- Template
- Template Variant
- Invitation
- Photo

---

# 2. Entidades principales

El MVP utiliza cuatro entidades principales:

1. TEMPLATE
2. TEMPLATE_VARIANT
3. INVITATION
4. PHOTO

## Relación General

```text
TEMPLATE
   │
   ├─────────────── N TEMPLATE_VARIANT
   │
   └─────────────── N INVITATION
                         │
                         └─────────────── N PHOTO
```

---

# 3. TEMPLATE

Representa una plantilla reutilizable para crear invitaciones.

Las plantillas no almacenan información específica de un evento.

Su función es definir la estructura de una invitación.

## Campos

| Campo | Tipo | Restricciones |
|---------|---------|---------|
| id | UUID | PK |
| name | VARCHAR(100) | UNIQUE, NOT NULL |
| description | VARCHAR(500) | NULL permitido |
| version | VARCHAR(30) | NOT NULL |
| is_active | BOOLEAN | NOT NULL, DEFAULT TRUE |
| created_at | TIMESTAMPTZ | NOT NULL |
| updated_at | TIMESTAMPTZ | NOT NULL |

## Reglas

- El nombre debe ser único.
- Una plantilla puede tener múltiples variantes.
- Una plantilla puede utilizarse para múltiples invitaciones.
- Una plantilla inactiva no podrá utilizarse para nuevas invitaciones.
- Desactivar una plantilla no elimina invitaciones existentes.

---

# 4. TEMPLATE_VARIANT

Representa una variante visual de una plantilla.

Una variante modifica únicamente la apariencia visual.

## Campos

| Campo | Tipo | Restricciones |
|---------|---------|---------|
| id | UUID | PK |
| template_id | UUID | FK → TEMPLATE.id |
| name | VARCHAR(100) | NOT NULL |
| description | VARCHAR(300) | NULL permitido |
| css_path | VARCHAR(300) | NOT NULL |
| is_active | BOOLEAN | NOT NULL, DEFAULT TRUE |
| created_at | TIMESTAMPTZ | NOT NULL |

## Restricciones

```text
UNIQUE(template_id, name)
```

## Relación

```text
TEMPLATE 1 ───────── N TEMPLATE_VARIANT
```

---

# 5. INVITATION

Representa una invitación creada por un usuario utilizando una plantilla.

Es la entidad principal del sistema.

## Campos

| Campo | Tipo | Restricciones |
|---------|---------|---------|
| id | UUID | PK |
| url_slug | VARCHAR(16) | UNIQUE, NOT NULL |
| template_id | UUID | FK → TEMPLATE.id |
| data | JSONB | NOT NULL |
| selected_variant | VARCHAR(100) | NOT NULL |
| status | VARCHAR(20) | NOT NULL |
| created_at | TIMESTAMPTZ | NOT NULL |
| updated_at | TIMESTAMPTZ | NOT NULL |
| published_at | TIMESTAMPTZ | NULL permitido |

## url_slug

Identificador público de la invitación.

Ejemplo:

```text
https://eventmaker.com/invitations/a8K29LmP7xQ2Nz4R
```

### Reglas

- Longitud: 16 caracteres.
- Debe ser único.
- Solo caracteres alfanuméricos.

---

## data

Almacena los datos personalizados de la invitación.

Se utilizará JSONB para permitir flexibilidad entre plantillas.

Ejemplo:

```json
{
  "event": {
    "name": "Boda de Juan y María",
    "date": "2026-12-12",
    "time": "18:00",
    "timezone": "America/Bogota",
    "location": "Cartagena",
    "address": "Centro Histórico"
  },
  "host": {
    "name": "Juan y María"
  },
  "message": "Nos encantaría compartir este día contigo."
}
```

---

## selected_variant

Variante visual seleccionada para renderizar la invitación.

Ejemplos:

```text
elegant
modern
classic
```

---

## Estados

```text
DRAFT
PUBLISHED
```

### Flujo

```text
DRAFT
  │
  ▼
PUBLISHED
```

### DRAFT

La invitación:

- puede editarse;
- puede cambiar de variante;
- puede recibir fotografías;
- puede visualizarse en preview.

### PUBLISHED

La invitación:

- está disponible públicamente;
- conserva la versión publicada;
- no permite cambios de variante en el MVP.

---

# 6. PHOTO

Representa una fotografía asociada a una invitación.

Los archivos físicos se almacenarán en S3 compatible.

La base de datos únicamente almacena metadatos.

## Campos

| Campo | Tipo | Restricciones |
|---------|---------|---------|
| id | UUID | PK |
| invitation_id | UUID | FK → INVITATION.id |
| slot_name | VARCHAR(100) | NOT NULL |
| s3_path | VARCHAR(500) | NOT NULL |
| upload_date | TIMESTAMPTZ | NOT NULL |

## Relación

```text
INVITATION 1 ───────── N PHOTO
```

## Reglas

- Una fotografía pertenece a una invitación.
- No puede existir sin una invitación.
- Debe tener un slot_name.
- Debe tener una ruta válida en almacenamiento.

### Restricciones de tamaño

```text
Máximo por archivo: 10 MB

Máximo por invitación: 50 MB
```

---

# 7. Integridad Referencial

## TEMPLATE → TEMPLATE_VARIANT

```text
ON DELETE CASCADE
```

Si se elimina una plantilla, se eliminan sus variantes.

---

## TEMPLATE → INVITATION

```text
ON DELETE RESTRICT
```

No se permite eliminar una plantilla utilizada por invitaciones.

---

## INVITATION → PHOTO

```text
ON DELETE CASCADE
```

Si se elimina una invitación, se eliminan sus fotografías asociadas.

---

# 8. Reglas de Negocio

## Estados

```text
DRAFT → PUBLISHED
```

No se permite:

```text
PUBLISHED → DRAFT
```

en el MVP.

---

## Variantes

Una variante podrá seleccionarse únicamente si:

1. Pertenece a la plantilla.
2. Está activa.
3. La invitación está en estado DRAFT.

---

## Fotografías

Las fotografías solamente podrán cargarse cuando la invitación esté en:

```text
DRAFT
```

---

# 9. Fuera del Alcance del MVP

Las siguientes entidades quedan reservadas para versiones futuras:

```text
CUSTOMER
USER
PAYMENT
SUBSCRIPTION
RSVP
ANALYTICS
MESSAGING
```

No se implementarán en la primera versión del sistema.

---

# 10. Modelo Final

```text
┌──────────────────────┐
│       TEMPLATE       │
├──────────────────────┤
│ id                   │
│ name                 │
│ description          │
│ version              │
│ is_active            │
│ created_at           │
│ updated_at           │
└──────────┬───────────┘
           │
           │ 1:N
           ▼
┌──────────────────────┐
│   TEMPLATE_VARIANT   │
├──────────────────────┤
│ id                   │
│ template_id FK       │
│ name                 │
│ description          │
│ css_path             │
│ is_active            │
│ created_at           │
└──────────────────────┘


┌──────────────────────┐
│       TEMPLATE       │
└──────────┬───────────┘
           │
           │ 1:N
           ▼
┌──────────────────────┐
│      INVITATION      │
├──────────────────────┤
│ id                   │
│ url_slug UNIQUE      │
│ template_id FK       │
│ data JSONB           │
│ selected_variant     │
│ status               │
│ created_at           │
│ updated_at           │
│ published_at         │
└──────────┬───────────┘
           │
           │ 1:N
           ▼
┌──────────────────────┐
│        PHOTO         │
├──────────────────────┤
│ id                   │
│ invitation_id FK     │
│ slot_name            │
│ s3_path              │
│ upload_date          │
└──────────────────────┘
```
