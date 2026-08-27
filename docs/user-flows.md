# Event Marker — User Flows

## 1. Registro y onboarding

```text
Usuario
 ↓
Registro
 ↓
User
 ↓
Account automática
 ↓
Membership(OWNER)
 ↓
Plan Free
 ↓
Dashboard
```

El onboarding será progresivo: se solicita información cuando es necesaria y no mediante un formulario inicial excesivo.

## 2. Crear evento

```text
Dashboard
 ↓
Crear evento
 ↓
Nombre + fecha + datos básicos
 ↓
Event
```

## 3. Crear invitation

```text
Event
 ↓
Crear invitation
 ↓
Catálogo de Templates
 ↓
Seleccionar Template/Variant
 ↓
Invitation DRAFT
```

## 4. Personalizar

```text
Invitation DRAFT
 ↓
Editor
 ├── Datos
 ├── Fotografías
 ├── Variante
 └── Opciones visuales permitidas
 ↓
Auto-save / Guardar
 ↓
Preview
```

## 5. Publicar

```text
Preview
 ↓
Validación
 ↓
¿Campos obligatorios completos?
 ├── No → Mostrar errores
 └── Sí
      ↓
   Publish
      ↓
 Public URL
```

## 6. Compartir

```text
Public URL
 ├── Copiar enlace
 ├── WhatsApp
 └── QR
```

## 7. Guest / RSVP

```text
Guest URL/token
 ↓
Resolver Guest
 ↓
Mostrar invitation pública/personalizada
 ↓
RSVP
 ├── CONFIRMED
 └── DECLINED
```

## 8. Variants

```text
Invitation Data + Media
          ↓
     Variant A/B/C
          ↓
       Renderer
```

Cambiar variant no obliga a introducir nuevamente datos ni fotografías.

## 9. Upgrade

```text
Límite alcanzado
 ↓
Mostrar plan/capacidad
 ↓
Upgrade
 ↓
Payment Provider
 ↓
Subscription ACTIVE
 ↓
Nuevas capabilities/limits
```

## 10. Diseñador profesional

```text
Account Professional
 ↓
Clientes
 ↓
Eventos
 ↓
Invitaciones
```

La gestión avanzada de equipos y marketplace queda fuera del MVP.
