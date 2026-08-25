# Event Maker — Arquitectura

## 1. Objetivo

Definir la arquitectura técnica del MVP de Event Maker, estableciendo
las responsabilidades principales de cada componente y la forma en
que se comunican.

La arquitectura debe permitir desarrollar inicialmente el MVP de forma
simple, pero dejando una base adecuada para evolucionar el producto.

---

## 2. Arquitectura general

Event Maker utilizará una arquitectura web cliente-servidor.

```text
┌──────────────────────────────┐
│          FRONTEND            │
│                              │
│  Interfaz de Event Maker     │
└──────────────┬───────────────┘
               │
               │ HTTPS / REST API
               ▼
┌──────────────────────────────┐
│           BACKEND            │
│                              │
│  API + reglas de negocio     │
└───────┬──────────┬───────────┘
        │          │
        │          │
        ▼          ▼
┌─────────────┐  ┌─────────────────┐
│ PostgreSQL  │  │ Servicios       │
│             │  │ externos        │
│ Datos       │  │                 │
└─────────────┘  │ - Pagos         │
                 │ - Storage       │
                 │ - OTP           │
                 └─────────────────┘