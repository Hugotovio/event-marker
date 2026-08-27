# Event Marker — Arquitectura

## 1. Decisión principal

Event Marker utilizará un **Monolito Modular** durante el MVP. No se implementarán microservicios prematuramente.

## 2. Stack

### Frontend
- Next.js.
- TypeScript.
- React.
- Responsive/mobile-first.

### Backend
- Python.
- FastAPI.
- Pydantic.
- SQLAlchemy.
- Alembic.

### Datos
- PostgreSQL.
- JSONB para datos variables de Invitation.
- Object Storage para archivos.

### Calidad y CI
- pytest.
- GitHub Actions.
- Bandit.
- pip-audit.

## 3. Capas

```text
HTTP/API
   ↓
Application
   ↓
Domain
   ↓
Ports
   ↓
Adapters / Infrastructure
   ├── PostgreSQL
   ├── Object Storage
   ├── Billing Provider
   └── Email/External Providers
```

El dominio no debe depender directamente de FastAPI, PostgreSQL ni proveedores concretos.

## 4. Módulos

```text
backend/app/modules/
├── identity/
├── accounts/
├── clients/
├── events/
├── invitations/
├── templates/
├── media/
├── guests/
├── rsvp/
├── billing/
└── administration/
```

Los límites de módulo son lógicos; no implican microservicios.

## 5. Multi-tenancy

```text
User
 ↓
Membership
 ↓
Account
 ↓
Private Resource
```

Cada operación privada debe resolver y verificar el tenant en backend.

## 6. Template System

```text
Template
 └── Version
      ├── Components
      │    └── Fields
      ├── Variants
      └── Assets
```

Una Invitation referencia una versión de Template y una Variant, y guarda sus datos independientes.

## 7. Renderer

```text
TemplateVersion
   + Variant
   + Invitation.data
   + Media
        ↓
     Renderer
        ↓
 Preview / Public
```

El Renderer debe ser común para evitar divergencia entre preview y publicación.

## 8. Storage

Se utilizará una abstracción `StorageService`.

```text
Application
    ↓
Storage Port
    ↓
Storage Adapter
    ├── Local (desarrollo)
    └── Object Storage (producción)
```

No se acoplará el dominio a un proveedor específico.

## 9. Upload

Cuando sea conveniente, el backend podrá emitir una URL firmada temporal para que el frontend suba directamente al Object Storage. La autorización y cuota se validan antes de emitirla.

## 10. Versionado

Templates publicadas son inmutables. Una modificación genera una nueva versión. Esto evita alterar invitaciones históricas accidentalmente.

## 11. Evolución

Si un módulo alcanza una escala o necesidad operacional que lo justifique, podrá extraerse posteriormente como servicio independiente. Esa decisión deberá basarse en evidencia, no en anticipación.
