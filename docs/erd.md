# Event Marker — ERD conceptual

```text
USER
  │
  └──< MEMBERSHIP >── ACCOUNT
                         │
          ┌──────────────┼─────────────────┐
          │              │                 │
          ▼              ▼                 ▼
       CLIENT         EVENT           SUBSCRIPTION
                         │                 │
                         │                 ▼
                         │               PLAN
                         │
          ┌──────────────┼───────────────┐
          │              │               │
          ▼              ▼               ▼
      INVITATION       GUEST          other event data
          │              │
   ┌──────┼──────┐       └── RSVP
   │      │      │
   ▼      ▼      ▼
TEMPLATE VARIANT MEDIA
   │
   ▼
TEMPLATE VERSION
   │
   ├── COMPONENT
   │      └── FIELD
   │
   └── ASSET

INVITATION
   ├── data JSONB
   ├── template_version_id
   ├── selected_variant_id
   └── public_slug

MEDIA
   └── storage_key ───────► OBJECT STORAGE

TEMPLATE ASSET
   └── storage_key ───────► OBJECT STORAGE
```

## Relaciones principales

- User N:M Account mediante Membership.
- Account 1:N Client.
- Account 1:N Event.
- Event 1:N Invitation.
- Event 1:N Guest.
- Guest 1:1 RSVP en el modelo inicial.
- Template 1:N TemplateVersion.
- TemplateVersion 1:N Component.
- Component 1:N Field.
- TemplateVersion 1:N Variant.
- TemplateVersion 1:N Asset.
- Invitation N:1 TemplateVersion.
- Invitation N:1 Variant.
- Invitation 1:N Media.
- Account 1:N Subscription históricamente, con una sola activa según regla comercial.
- Subscription N:1 Plan.
