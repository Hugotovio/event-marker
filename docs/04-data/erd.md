# Event Maker — ERD

## 1. Diagrama entidad-relación

El MVP de Event Maker está compuesto por cinco entidades principales:

- CUSTOMER
- EVENT
- TEMPLATE
- INVITATION
- PAYMENT

```text
                         ┌──────────────────────┐
                         │       CUSTOMER       │
                         ├──────────────────────┤
                         │ PK id UUID           │
                         │ name                 │
                         │ email UNIQUE         │
                         │ phone UNIQUE         │
                         │ created_at           │
                         │ updated_at           │
                         └──────────┬───────────┘
                                    │
                                    │ 1:N
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │        EVENT         │
                         ├──────────────────────┤
                         │ PK id UUID           │
                         │ FK customer_id       │
                         │ name                 │
                         │ event_type           │
                         │ event_date           │
                         │ event_time           │
                         │ timezone             │
                         │ location             │
                         │ address              │
                         │ created_at           │
                         │ updated_at           │
                         └──────────┬───────────┘
                                    │
                       ┌────────────┴────────────┐
                       │                         │
                       │ 1:1                     │ 1:N
                       ▼                         ▼
             ┌──────────────────────┐   ┌──────────────────────┐
             │     INVITATION      │   │       PAYMENT        │
             ├──────────────────────┤   ├──────────────────────┤
             │ PK id UUID           │   │ PK id UUID           │
             │ FK event_id UNIQUE   │   │ FK event_id          │
             │ FK template_id       │   │ provider             │
             │ slug UNIQUE          │   │ provider_reference   │
             │ customization JSONB  │   │ amount               │
             │ status               │   │ currency             │
             │ published_at         │   │ status               │
             │ created_at           │   │ created_at           │
             │ updated_at           │   │ updated_at           │
             └──────────┬───────────┘   │ updated_at           │
                        │               └──────────────────────┘
                        │ N:1
                        ▼
             ┌──────────────────────┐
             │       TEMPLATE       │
             ├──────────────────────┤
             │ PK id UUID           │
             │ name                 │
             │ event_type           │
             │ preview_image        │
             │ configuration JSONB  │
             │ status               │
             │ created_at           │
             │ updated_at           │
             └──────────────────────┘