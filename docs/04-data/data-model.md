
# Event Maker — Modelo de Datos

## 1. Objetivo

Este documento define el modelo de datos relacional del MVP de
Event Maker.

El modelo debe representar:

- clientes;
- eventos;
- plantillas;
- invitaciones;
- pagos;
- relaciones entre estas entidades;
- integridad referencial;
- estados;
- restricciones necesarias para mantener la consistencia.

---

# 2. Entidades principales

El MVP utiliza cinco entidades principales:

1. CUSTOMER
2. EVENT
3. TEMPLATE
4. INVITATION
5. PAYMENT

---

# 3. CUSTOMER

Representa al cliente que crea una invitación.

## Campos

| Campo | Tipo | Restricciones |
|---|---|---|
| id | UUID | PK |
| name | VARCHAR(100) | NULL permitido |
| email | VARCHAR(255) | UNIQUE, NULL permitido |
| phone | VARCHAR(20) | UNIQUE, NULL permitido |
| created_at | TIMESTAMPTZ | NOT NULL |
| updated_at | TIMESTAMPTZ | NOT NULL |

## Reglas

Debe existir al menos uno de:

- email;
- phone.

No se utilizará contraseña en el MVP.

---

# 4. EVENT

Representa el evento para el cual se crea la invitación.

## Campos

| Campo | Tipo | Restricciones |
|---|---|---|
| id | UUID | PK |
| customer_id | UUID | FK, NOT NULL |
| name | VARCHAR(150) | NOT NULL |
| event_type | VARCHAR(30) | NOT NULL |
| event_date | DATE | NOT NULL |
| event_time | TIME | NOT NULL |
| timezone | VARCHAR(50) | NOT NULL |
| location | VARCHAR(200) | NOT NULL |
| address | VARCHAR(300) | NULL permitido |
| created_at | TIMESTAMPTZ | NOT NULL |
| updated_at | TIMESTAMPTZ | NOT NULL |

## Relación

```text
CUSTOMER 1 ───────── N EVENT