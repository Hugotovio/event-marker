# Event Maker — Product Overview

## 1. Descripción

Event Maker es una plataforma web que permite a un cliente crear,
personalizar, pagar y publicar una invitación digital para un evento.

Una vez publicada, el cliente obtiene un enlace que puede compartir
directamente con sus invitados.

## 2. Objetivo del MVP

Permitir que una persona pueda crear una invitación digital sin
necesidad de registrarse previamente, personalizarla, realizar el
pago y obtener un enlace público para compartirla.

## 3. Flujo principal

1. El cliente ingresa a Event Maker.
2. Selecciona el tipo de evento.
3. Selecciona una plantilla.
4. Personaliza la invitación.
5. Visualiza una previsualización.
6. Proporciona un medio de contacto.
7. Realiza el pago.
8. El sistema confirma el pago.
9. El cliente publica la invitación.
10. Event Maker genera/activa el enlace público.
11. El cliente comparte el enlace con sus invitados.
12. El invitado visualiza la invitación.

## 4. Acceso del cliente

El cliente no necesita crear una cuenta con contraseña para comenzar.

El sistema podrá identificar y recuperar al cliente mediante un medio
de contacto y autenticación OTP.

El mecanismo de OTP se implementará posteriormente como parte de la
arquitectura de autenticación.

## 5. Invitación

Una invitación pertenece a un evento.

La invitación permite:

- seleccionar una plantilla;
- modificar los campos permitidos por la plantilla;
- personalizar colores;
- personalizar tipografías;
- agregar imágenes;
- configurar elementos visuales;
- visualizar una previsualización;
- publicar la invitación después del pago.

## 6. Enlace público

Cada invitación publicada tendrá un enlace público.

Ejemplo:

`eventmaker.com/e/juan-y-maria`

El invitado no necesita registrarse ni autenticarse para visualizar
una invitación publicada.

## 7. Pago

El cliente debe realizar el pago antes de publicar la invitación.

La aprobación del pago será determinada por el backend mediante la
integración con el proveedor de pagos.

El frontend nunca podrá declarar por sí mismo que un pago fue aprobado.

## 8. Invitados

El MVP no implementará:

- registro de invitados;
- lista de invitados;
- RSVP;
- confirmación de asistencia;
- número de acompañantes;
- gestión de asistentes.

Si un invitado desea confirmar su asistencia, lo hará directamente
con el cliente por el medio que ambos acuerden.

## 9. Borradores

Un usuario puede comenzar a crear una invitación sin registrarse.

Los borradores anónimos serán temporales.

El sistema conservará temporalmente el progreso y deberá informar al
cliente sobre el período disponible para continuar.

El período inicial definido para el MVP es de 24 horas desde la última
actividad.

## 10. Comunicación con el cliente

El sistema debe informar al cliente sobre el estado de su proceso.

Como mínimo deberá comunicar:

- invitación en construcción;
- invitación pendiente de pago;
- pago confirmado;
- pago rechazado;
- invitación publicada;
- invitación expirada.

## 11. Alcance del MVP

El MVP se concentra en:

Crear → Personalizar → Previsualizar → Pagar → Publicar → Compartir.

Las funcionalidades que no sean necesarias para este flujo se
consideran fuera del alcance inicial.

## 12. Principio del producto

Event Maker debe mantener al cliente informado sobre el estado de su
invitación y sobre cualquier acción necesaria para completar el proceso.