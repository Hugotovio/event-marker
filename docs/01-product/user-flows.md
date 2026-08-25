# Event Maker — Flujos de Usuario

## 1. Flujo principal

```text
Cliente
   │
   ▼
Inicio
   │
   ▼
Seleccionar tipo de evento
   │
   ▼
Seleccionar plantilla
   │
   ▼
Personalizar invitación
   │
   ▼
Previsualizar
   │
   ▼
¿Está satisfecho?
   │
   ├── No ──► Continuar personalizando
   │
   └── Sí
         │
         ▼
    Proporcionar contacto
         │
         ▼
      Iniciar pago
         │
         ▼
   Esperar confirmación
         │
    ┌────┴────┐
    │         │
    ▼         ▼
 Aprobado   Rechazado
    │         │
    ▼         ▼
  Publicar   Reintentar
    │
    ▼
Obtener enlace
    │
    ▼
Compartir