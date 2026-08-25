# Event Maker — Arquitectura Backend

## 1. Objetivo

Definir la arquitectura interna del backend de Event Maker para
mantener separadas las responsabilidades de API, aplicación,
dominio e infraestructura.

El backend será la autoridad sobre las reglas de negocio.

---

# 2. Arquitectura

El backend utilizará una arquitectura modular basada en:

```text
API
 │
 ▼
Application
 │
 ▼
Domain
 │
 ▼
Infrastructure
