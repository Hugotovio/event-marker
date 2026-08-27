# Event Marker — Product Overview

## 1. Visión

Event Marker será una plataforma SaaS que permite crear experiencias digitales alrededor de eventos, comenzando con invitaciones digitales profesionales, rápidas de personalizar y fáciles de compartir.

El producto no se limita a vender una invitación individual. El usuario dispone de un espacio (`Account`) donde puede crear y administrar múltiples eventos e invitaciones según las capacidades y límites de su plan.

## 2. Problema

Crear una invitación profesional puede exigir conocimientos de diseño, herramientas especializadas o contratar a un tercero. Event Marker busca reducir esa fricción mediante un flujo guiado basado en plantillas estructuradas.

## 3. Propuesta de valor

El usuario puede:

1. Crear un evento.
2. Elegir una plantilla.
3. Personalizar datos y fotografías.
4. Cambiar variantes visuales sin perder contenido.
5. Previsualizar.
6. Publicar.
7. Compartir mediante URL, WhatsApp o QR.

## 4. Usuarios

### Particular
Crea invitaciones para sus propios eventos.

### Profesional
Diseñadores u organizadores que gestionan múltiples clientes y eventos.

### Empresa
Organizaciones que necesitan administrar múltiples usuarios, eventos y trabajos.

Los tres perfiles utilizan la misma plataforma. Las diferencias comerciales se expresan mediante capacidades, límites y roles.

## 5. Producto central

El núcleo está formado por:

```text
Account
  ↓
Event
  ↓
Invitation
  ↓
Template + Variant
  ↓
Data + Media
  ↓
Renderer
  ↓
Public Invitation
  ↓
Guest / RSVP
```

## 6. Templates

Una Template es un diseño estructurado compuesto por componentes, campos editables, slots de fotografías, temas y variantes. No es una simple imagen y no permite código arbitrario del usuario.

## 7. Modelo de negocio

La dirección aprobada es SaaS por suscripción: la suscripción pertenece a la `Account`, no a una invitación individual. El plan determina capacidades y límites. Los precios definitivos se validarán comercialmente.

## 8. Evolución

La invitación es el primer producto. La arquitectura permitirá incorporar posteriormente RSVP avanzado, gestión de invitados, analítica, galerías, itinerarios, experiencias corporativas, marketplace de templates y capacidades para equipos.
