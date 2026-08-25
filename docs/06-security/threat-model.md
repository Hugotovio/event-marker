# Modelo de Amenazas

Pendiente.
# Event Maker — Modelo de Amenazas

## 1. Objetivo

Identificar las principales amenazas de seguridad que pueden afectar
a Event Maker durante el MVP y definir los controles que deberán
mitigarlas.

El modelo se utilizará como referencia durante:

- diseño;
- desarrollo;
- pruebas;
- revisión de código;
- despliegue.

---

# 2. Activos que debemos proteger

Los principales activos de Event Maker son:

| Activo | Importancia |
|---|---|
| Datos del cliente | Alta |
| Datos del evento | Alta |
| Invitaciones | Alta |
| Personalizaciones | Media |
| Pagos | Crítica |
| Credenciales / OTP | Crítica |
| Archivos e imágenes | Alta |
| Plantillas | Media |
| Base de datos | Crítica |
| Secretos de infraestructura | Crítica |

---

# 3. Actores potenciales

## 3.1 Cliente legítimo

Puede intentar acceder o modificar recursos que no le pertenecen.

## 3.2 Invitado

Tiene acceso legítimo a invitaciones publicadas, pero no debe obtener
información privada del cliente.

## 3.3 Usuario no autenticado

Puede intentar acceder directamente a APIs privadas.

## 3.4 Atacante externo

Puede intentar:

- acceder a recursos;
- manipular solicitudes;
- explotar vulnerabilidades;
- abusar de endpoints;
- subir archivos maliciosos;
- atacar autenticación;
- manipular pagos.

## 3.5 Dependencia comprometida

Una librería vulnerable o comprometida podría introducir una
vulnerabilidad en la aplicación.

---

# 4. Amenaza — Acceso no autorizado a otra invitación

## Escenario

Un cliente modifica una solicitud para utilizar el ID de una
invitación perteneciente a otro cliente.

Ejemplo:

```text
Cliente A
   │
   ▼
PATCH /invitations/{ID-de-B}