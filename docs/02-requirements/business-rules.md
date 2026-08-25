
# Event Maker — Reglas de Negocio

Las reglas de negocio definen comportamientos que el sistema debe
respetar independientemente de la tecnología utilizada para
implementarlos.

---

## RN-001 — Creación sin registro

Un cliente puede iniciar la creación de una invitación sin tener
una cuenta registrada.

---

## RN-002 — Borrador temporal

Una invitación que todavía no ha sido asociada a un cliente puede
mantenerse como borrador temporal.

El período inicial de conservación es de 24 horas desde la última
actividad.

---

## RN-003 — Expiración del borrador

Si un borrador anónimo permanece 24 horas sin actividad, debe pasar
a estado `EXPIRED`.

Una invitación `EXPIRED` no puede publicarse directamente.

---

## RN-004 — Medio de contacto

Antes de iniciar el proceso de pago, el cliente debe proporcionar
al menos uno de los siguientes medios:

- email;
- teléfono.

No es obligatorio proporcionar ambos.

---

## RN-005 — Identificación del cliente

Cuando el cliente proporciona un medio de contacto válido, la
invitación puede asociarse a un `CUSTOMER`.

El sistema debe evitar crear clientes duplicados para el mismo medio
de contacto normalizado.

---

## RN-006 — Recuperación mediante OTP

Una invitación asociada a un cliente puede recuperarse mediante un
mecanismo de autenticación OTP.

El OTP debe:

- tener una vigencia limitada;
- ser de un solo uso;
- no almacenarse en texto plano;
- tener un límite de intentos.

---

## RN-007 — Una invitación por evento

Durante el MVP, cada `EVENT` puede tener solamente una `INVITATION`.

La relación es:

```text
EVENT 1 ───────── 1 INVITATION