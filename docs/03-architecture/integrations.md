# Event Maker — Integraciones Externas

## 1. Objetivo

Definir los servicios externos que Event Maker podrá utilizar y
establecer claramente la responsabilidad de cada integración.

Las integraciones externas deben estar aisladas del dominio de
negocio para evitar que Event Maker dependa directamente de un
proveedor específico.

---

## 2. Integraciones previstas

Durante el MVP se contemplan las siguientes categorías:

```text
Event Maker
    │
    ├── Proveedor de pagos
    │
    ├── Object Storage
    │
    └── Proveedor de correo / OTP