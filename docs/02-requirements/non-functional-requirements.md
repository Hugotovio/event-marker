
# Event Maker — Requisitos No Funcionales

## RNF-001 — Seguridad

El sistema debe proteger los datos del cliente y evitar accesos no
autorizados a las operaciones privadas.

Las operaciones de administración de una invitación deben verificar
que el usuario tenga autorización sobre el recurso.

## RNF-002 — Protección de credenciales y secretos

Las claves, tokens, secretos de proveedores y credenciales no deben
estar almacenados directamente en el código fuente.

Los secretos deben ser proporcionados mediante configuración segura
del entorno.

## RNF-003 — Seguridad del pago

La aplicación no debe confiar en información enviada únicamente por
el frontend para determinar si un pago fue aprobado.

La confirmación debe ser validada por el backend mediante el
mecanismo proporcionado por el proveedor de pagos.

## RNF-004 — Idempotencia

Las operaciones que puedan ser recibidas más de una vez, especialmente
las relacionadas con pagos y webhooks, deben poder procesarse de forma
idempotente.

Una misma transacción no debe generar múltiples efectos.

## RNF-005 — Integridad de datos

La base de datos debe utilizar restricciones para garantizar la
integridad de la información.

Se deben utilizar, cuando corresponda:

- claves primarias;
- claves foráneas;
- restricciones UNIQUE;
- restricciones NOT NULL;
- restricciones CHECK.

## RNF-006 — Validación de entrada

Toda información recibida desde el cliente debe validarse en el
backend.

La validación del frontend no reemplaza la validación del backend.

## RNF-007 — Protección contra archivos maliciosos

Las imágenes cargadas por los clientes deben validarse antes de ser
almacenadas.

El sistema debe controlar como mínimo:

- tipo de archivo;
- extensión;
- tamaño máximo;
- nombre del archivo.

Los archivos no deben utilizar directamente el nombre proporcionado
por el usuario como nombre físico de almacenamiento.

## RNF-008 — Protección de datos

El sistema debe evitar exponer información interna innecesaria a
través de las APIs públicas.

La consulta pública de una invitación debe devolver únicamente la
información necesaria para visualizarla.

## RNF-009 — Manejo de errores

Los errores deben ser controlados por el backend y devolver respuestas
consistentes.

Las respuestas no deben revelar:

- credenciales;
- secretos;
- información interna de la infraestructura;
- stack traces;
- información sensible de otros clientes.

## RNF-010 — Trazabilidad

Las operaciones importantes deben poder ser rastreadas mediante
información de auditoría y registros técnicos.

Como mínimo, las entidades principales deben conservar:

- fecha de creación;
- fecha de actualización.

Las operaciones críticas deberán poder relacionarse con un
identificador de correlación cuando la arquitectura lo requiera.

## RNF-011 — Observabilidad

El sistema debe proporcionar mecanismos para identificar errores y
problemas operativos.

La arquitectura deberá contemplar:

- logs estructurados;
- identificación de solicitudes;
- métricas básicas;
- monitoreo de errores.

## RNF-012 — Protección de información sensible en logs

No se deben registrar en logs:

- contraseñas;
- tokens;
- claves API;
- secretos;
- información completa de medios de pago;
- códigos OTP.

## RNF-013 — Rendimiento

Las operaciones habituales de la aplicación deben responder en un
tiempo adecuado para una aplicación web.

Las consultas públicas de invitaciones deben estar optimizadas para
su utilización frecuente mediante enlaces compartidos.

Los objetivos numéricos definitivos de rendimiento se establecerán
cuando se conozca la infraestructura de producción.

## RNF-014 — Disponibilidad

La aplicación debe estar diseñada para continuar funcionando ante
fallos controlables de componentes externos.

Los servicios externos, como el proveedor de pagos, no deben provocar
que el sistema pierda la información de una invitación o de una
transacción.

## RNF-015 — Recuperación ante fallos

Las operaciones críticas deben poder recuperarse de errores sin
generar estados inconsistentes.

Especialmente:

- procesamiento de pagos;
- publicación de invitaciones;
- actualización de estados.

## RNF-016 — Consistencia transaccional

Las operaciones que modifiquen varias entidades relacionadas deben
utilizar transacciones cuando sea necesario para mantener la
consistencia de los datos.

## RNF-017 — Escalabilidad

La arquitectura debe permitir aumentar la capacidad de la aplicación
sin modificar completamente el modelo de dominio.

El diseño inicial debe evitar dependencias innecesarias que impidan
posteriormente escalar los componentes.

## RNF-018 — Mantenibilidad

El código debe organizarse separando responsabilidades.

La implementación debe evitar acoplar directamente:

- lógica de negocio;
- acceso a datos;
- proveedores externos;
- presentación.

## RNF-019 — Configuración

Los valores dependientes del entorno no deben estar escritos
directamente en el código.

Ejemplos:

- URL de base de datos;
- URL de servicios externos;
- claves de proveedores;
- configuración de almacenamiento;
- configuración de correo.

## RNF-020 — Compatibilidad

La aplicación debe funcionar correctamente en navegadores web
modernos utilizados habitualmente por los usuarios.

## RNF-021 — Accesibilidad

La interfaz debe seguir buenas prácticas de accesibilidad web,
incluyendo:

- contraste adecuado;
- navegación mediante teclado;
- etiquetas apropiadas;
- mensajes de error comprensibles;
- estructura semántica.

## RNF-022 — Privacidad

El sistema debe recopilar únicamente la información necesaria para
cumplir las funciones del MVP.

No se deben almacenar datos de invitados que no sean necesarios para
la funcionalidad definida.

## RNF-023 — Evolución

Los requisitos no funcionales deben considerarse restricciones
arquitectónicas.

Las decisiones de implementación posteriores deben respetar estos
requisitos o documentar explícitamente cualquier excepción.

## RNF-024 — Calidad

El proyecto debe contar con pruebas automatizadas para las partes
críticas del sistema.

Como mínimo deberán cubrirse:

- reglas de negocio;
- transiciones de estados;
- procesamiento de pagos;
- validaciones;
- autorización;
- endpoints principales.