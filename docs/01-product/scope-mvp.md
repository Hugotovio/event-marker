
# Event Maker — Alcance del MVP

## 1. Objetivo

El MVP de Event Maker debe permitir completar el siguiente flujo:

Crear → Personalizar → Previsualizar → Pagar → Publicar → Compartir.

Toda funcionalidad que no sea necesaria para completar este flujo queda
fuera del alcance inicial.

---

## 2. Funcionalidades incluidas

### 2.1 Creación de invitación

El cliente podrá:

- seleccionar el tipo de evento;
- seleccionar una plantilla;
- comenzar la personalización.

No será necesario crear una cuenta antes de comenzar.

### 2.2 Personalización

El cliente podrá modificar los campos definidos por la plantilla.

La personalización podrá incluir:

- textos;
- colores;
- tipografías;
- imágenes;
- elementos visuales disponibles;
- opciones habilitadas por la plantilla.

El cliente no tendrá un editor completamente libre.

### 2.3 Previsualización

El cliente podrá visualizar cómo quedará la invitación antes de
realizar el pago.

### 2.4 Contacto

Antes de iniciar el proceso de pago, el cliente deberá proporcionar
al menos uno de los siguientes medios:

- correo electrónico;
- número de teléfono.

### 2.5 Pago

El sistema permitirá iniciar un proceso de pago mediante un proveedor
externo.

El backend será responsable de verificar la confirmación del pago.

El frontend no podrá determinar por sí mismo que un pago fue aprobado.

### 2.6 Publicación

Después de confirmar el pago, el cliente podrá publicar la invitación.

Una invitación publicada tendrá un enlace público.

Ejemplo:

`eventmaker.com/e/juan-y-maria`

### 2.7 Visualización pública

Un invitado podrá acceder al enlace sin:

- registrarse;
- iniciar sesión;
- proporcionar datos personales.

Podrá visualizar la invitación publicada.

### 2.8 Borradores

Los usuarios podrán comenzar una invitación sin registrarse.

Los borradores anónimos serán temporales.

El período inicial definido es de 24 horas desde la última actividad.

El sistema deberá informar al cliente sobre este período.

### 2.9 Recuperación

Una invitación asociada a un medio de contacto podrá recuperarse
mediante autenticación OTP.

La implementación inicial priorizará correo electrónico.

WhatsApp podrá incorporarse posteriormente.

---

# 3. Funcionalidades excluidas

Las siguientes funcionalidades NO forman parte del MVP.

## 3.1 Gestión de invitados

No se implementará:

- creación de listas de invitados;
- registro de invitados;
- importación de invitados;
- eliminación de invitados;
- grupos de invitados.

## 3.2 RSVP

No se implementará:

- confirmación de asistencia;
- rechazo de asistencia;
- número de acompañantes;
- estado de asistencia;
- estadísticas de asistencia.

Los invitados podrán confirmar directamente con el cliente.

## 3.3 Cuentas tradicionales

No se implementará inicialmente:

- usuario + contraseña;
- recuperación de contraseña;
- perfiles completos;
- roles de usuario para clientes.

La autenticación se realizará mediante OTP cuando sea necesaria.

## 3.4 Editor avanzado

No se implementará un editor libre tipo Canva.

El cliente solamente podrá modificar los campos definidos por la
plantilla.

## 3.5 Marketplace avanzado

No se implementará inicialmente:

- marketplace de diseñadores;
- plantillas creadas por usuarios;
- venta de plantillas;
- sistema de calificaciones;
- sistema de favoritos.

## 3.6 Notificaciones avanzadas

No se implementará inicialmente un sistema completo de:

- campañas;
- recordatorios automáticos;
- marketing por correo;
- campañas de WhatsApp;
- notificaciones a invitados.

El sistema sí deberá informar al cliente sobre los estados
fundamentales de su proceso dentro de la aplicación.

---

# 4. Reglas de alcance

## Regla 1

Toda funcionalidad nueva debe evaluarse frente al objetivo principal
del MVP.

## Regla 2

Si una funcionalidad no es necesaria para:

Crear → Personalizar → Previsualizar → Pagar → Publicar → Compartir,

debe considerarse para una versión posterior.

## Regla 3

El MVP debe priorizar un flujo completo y funcional sobre una gran
cantidad de funcionalidades.

## Regla 4

No se implementará una funcionalidad solamente porque pueda ser útil
en el futuro.

---

# 5. Resultado esperado

Al finalizar el MVP, un cliente deberá poder:

1. Entrar a Event Maker.
2. Crear una invitación.
3. Seleccionar una plantilla.
4. Personalizarla.
5. Previsualizarla.
6. Proporcionar su contacto.
7. Pagar.
8. Recibir confirmación del pago.
9. Publicar la invitación.
10. Obtener un enlace.
11. Compartir el enlace con sus invitados.

Un invitado deberá poder:

1. Recibir el enlace.
2. Abrirlo.
3. Visualizar la invitación.

No será necesario que el invitado interactúe con Event Maker más allá
de visualizar la invitación.