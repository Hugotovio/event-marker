# Event Maker — Requisitos Funcionales

## RF-001 — Crear invitación

El sistema debe permitir iniciar la creación de una invitación sin
que el cliente tenga que registrarse previamente.

## RF-002 — Seleccionar tipo de evento

El sistema debe permitir seleccionar el tipo de evento antes de elegir
la plantilla.

## RF-003 — Seleccionar plantilla

El sistema debe mostrar las plantillas disponibles para el tipo de
evento seleccionado.

El cliente debe poder seleccionar una plantilla.

## RF-004 — Personalizar invitación

El sistema debe permitir modificar únicamente los campos definidos
por la plantilla seleccionada.

La personalización puede incluir, según la plantilla:

- textos;
- colores;
- tipografías;
- imágenes;
- elementos visuales;
- opciones configurables.

## RF-005 — Validar personalización

El sistema debe validar que los valores proporcionados por el cliente
cumplan las reglas definidas por la plantilla.

No se deben aceptar campos o configuraciones que no estén definidos
por la plantilla.

## RF-006 — Previsualizar invitación

El sistema debe permitir visualizar una representación de la
invitación antes de iniciar el pago.

El cliente debe poder regresar al proceso de personalización desde
la previsualización.

## RF-007 — Guardar borrador temporal

El sistema debe conservar temporalmente el progreso de una invitación
que todavía no ha sido completada.

Los borradores anónimos deben conservarse durante 24 horas desde su
última actividad.

## RF-008 — Informar expiración

El sistema debe informar al cliente que el borrador será conservado
solamente durante el período establecido.

Cuando el borrador expire, el sistema debe impedir su utilización
como invitación activa.

## RF-009 — Registrar datos de contacto

Antes de iniciar el pago, el sistema debe solicitar al menos uno de
los siguientes datos:

- correo electrónico;
- número de teléfono.

El sistema debe validar el formato del dato proporcionado.

## RF-010 — Asociar cliente

Cuando el cliente proporcione un medio de contacto válido, el sistema
debe poder asociar la invitación con un CUSTOMER.

## RF-011 — Recuperar invitación

El sistema debe permitir recuperar una invitación asociada a un
cliente mediante un mecanismo de autenticación OTP.

## RF-012 — Iniciar pago

El sistema debe permitir iniciar un proceso de pago mediante un
proveedor externo.

## RF-013 — Registrar intento de pago

Cada intento de pago debe registrarse como una operación independiente.

El sistema debe conservar los intentos rechazados y aprobados.

## RF-014 — Recibir confirmación de pago

El backend debe recibir y procesar la confirmación del pago enviada
por el proveedor.

El frontend no podrá determinar directamente que un pago fue aprobado.

## RF-015 — Procesar pagos de forma idempotente

El sistema no debe procesar dos veces la misma transacción del
proveedor.

La referencia proporcionada por el proveedor debe utilizarse para
garantizar la idempotencia.

## RF-016 — Actualizar estado de invitación

Cuando el pago sea aprobado, el sistema debe permitir que la
invitación pase al estado `PAID`.

Un pago rechazado no debe permitir que la invitación pase a `PAID`.

## RF-017 — Publicar invitación

El sistema debe permitir publicar una invitación únicamente cuando
exista un pago aprobado.

## RF-018 — Generar enlace público

Una invitación publicada debe disponer de un slug único para generar
su enlace público.

Ejemplo:

`eventmaker.com/e/juan-y-maria`

## RF-019 — Consultar invitación pública

El sistema debe permitir consultar una invitación mediante su slug.

La consulta pública debe devolver únicamente invitaciones cuyo estado
sea `PUBLISHED`.

## RF-020 — Impedir acceso público a invitaciones no publicadas

Las invitaciones en estado:

- `DRAFT`;
- `PENDING_PAYMENT`;
- `PAID`;
- `EXPIRED`;

no deben estar disponibles mediante el enlace público.

## RF-021 — Compartir invitación

Una vez publicada, el sistema debe mostrar al cliente el enlace
público de su invitación para que pueda compartirlo.

## RF-022 — Visualización sin registro

Los invitados deben poder visualizar una invitación publicada sin
crear una cuenta ni iniciar sesión.

## RF-023 — Estados de la invitación

El sistema debe manejar los siguientes estados:

- `DRAFT`;
- `PENDING_PAYMENT`;
- `PAID`;
- `PUBLISHED`;
- `EXPIRED`.

## RF-024 — Estados del pago

El sistema debe manejar los siguientes estados:

- `PENDING`;
- `APPROVED`;
- `DECLINED`;
- `CANCELLED`;
- `REFUNDED`.

## RF-025 — Información de estado

El sistema debe informar al cliente sobre los cambios relevantes en
el estado de su invitación y su proceso de pago.

## RF-026 — Gestión de imágenes

El sistema debe permitir cargar imágenes cuando la plantilla
seleccionada lo permita.

Las imágenes deben almacenarse fuera de la base de datos.

La invitación debe conservar únicamente la referencia necesaria para
recuperar la imagen.

## RF-027 — Plantillas activas

El sistema debe mostrar únicamente las plantillas disponibles para
nuevas invitaciones.

Una plantilla desactivada no debe aparecer como opción para nuevas
invitaciones.

Las invitaciones existentes que utilicen una plantilla desactivada
deben continuar funcionando.

## RF-028 — Validación de propiedad

Las operaciones privadas sobre una invitación deben verificar que
el cliente que las realiza tenga autorización sobre dicha invitación.

## RF-029 — Confirmación de asistencia

El sistema no debe registrar ni gestionar confirmaciones de
asistencia dentro del MVP.

La confirmación se realizará directamente entre el invitado y el
cliente.

## RF-030 — Comunicación con el cliente

El sistema debe proporcionar información clara sobre la siguiente
acción que el cliente debe realizar durante el proceso de creación,
pago y publicación.