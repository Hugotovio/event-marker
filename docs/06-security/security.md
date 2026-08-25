# Seguridad

Pendiente.
# Event Maker — Seguridad

## 1. Objetivo

La seguridad debe formar parte del diseño de Event Maker desde el
inicio del proyecto.

No se considera una actividad que deba agregarse después de terminar
el desarrollo.

El sistema debe proteger:

- clientes;
- invitaciones;
- pagos;
- información de contacto;
- archivos;
- autenticación;
- APIs;
- infraestructura.

---

# 2. Principios de seguridad

Event Maker seguirá estos principios:

1. No confiar en el cliente.
2. Validar toda entrada en el backend.
3. Aplicar mínimo privilegio.
4. Separar autenticación de autorización.
5. No almacenar secretos en el código.
6. No exponer información sensible.
7. Registrar eventos relevantes sin registrar secretos.
8. Utilizar HTTPS.
9. Aplicar seguridad tanto en frontend como en backend.
10. Considerar seguridad durante todo el ciclo de desarrollo.

---

# 3. Autenticación

El MVP no utilizará usuario y contraseña.

El mecanismo inicial será OTP.

El flujo será:

```text
Cliente
   │
   ▼
Solicita OTP
   │
   ▼
Backend
   │
   ▼
Genera código
   │
   ▼
Proveedor de correo
   │
   ▼
Cliente recibe código
   │
   ▼
Introduce código
   │
   ▼
Backend valida
   │
   ▼
Sesión / Token