# Event Marker — Modelo de Datos

## User

Representa a una persona autenticada.

Campos conceptuales: `id`, `email`, `password_hash` o credencial equivalente, `name`, `status`, timestamps.

## Account

Tenant lógico y espacio de trabajo.

Campos: `id`, `name`, `status`, timestamps.

## Membership

Relaciona User con Account y define su rol.

Campos: `id`, `user_id`, `account_id`, `role`, timestamps.

## Client

Contacto/cliente gestionado por una Account. No requiere autenticación.

Campos: `id`, `account_id`, `name`, `email`, `phone`, timestamps.

## Event

Representa el evento del mundo real.

Campos conceptuales: `id`, `account_id`, `client_id?`, `name`, `description`, `event_date`, `event_time`, `location`, `status`, timestamps.

## Template

Diseño estructurado administrado por Event Marker.

Campos: `id`, `name`, `description`, `category`, `status`, `current_version`, timestamps.

## TemplateVersion

Versión inmutable de una Template publicada o en preparación.

Campos: `id`, `template_id`, `version`, `schema`, `renderer_configuration`, timestamps.

## TemplateComponent

Componente de una versión de Template.

Campos: `id`, `template_version_id`, `type`, `position`, `configuration`.

## TemplateField

Campo editable o interno definido por un componente.

Campos: `id`, `component_id`, `key`, `type`, `label`, `editable`, `required`, `validation`, `configuration`.

## TemplateVariant

Alternativa visual de una TemplateVersion.

Campos: `id`, `template_version_id`, `name`, `theme`, `configuration`.

## TemplateAsset

Metadata de recursos pertenecientes a una Template.

Campos: `id`, `template_version_id`, `storage_key`, `asset_type`, `mime_type`, `size_bytes`, timestamps.

## Invitation

Instancia de una Template asociada a un Event.

Campos: `id`, `account_id`, `event_id`, `template_version_id`, `selected_variant_id`, `data JSONB`, `status`, `public_slug`, timestamps, `published_at`.

## Media

Metadata de fotografías/archivos del cliente.

Campos: `id`, `account_id`, `invitation_id`, `slot_name`, `storage_key`, `mime_type`, `size_bytes`, `width`, `height`, `status`, timestamps.

## Guest

Invitado de un Event.

Campos: `id`, `event_id`, `name`, `email`, `token_hash`, `status`, timestamps.

## RSVP

Respuesta de un Guest.

Campos: `id`, `guest_id`, `status`, timestamps.

## Plan

Define capacidades y límites comerciales.

Campos: `id`, `code`, `name`, `capabilities`, `limits`, `status`.

## Subscription

Suscripción de una Account.

Campos: `id`, `account_id`, `plan_id`, `status`, period dates, provider reference, timestamps.

## Usage

Métricas necesarias para aplicar límites, por ejemplo `storage_bytes`, `active_events`, `active_invitations` y otras que se definan.

## Payment

Registro de transacciones o referencias de pago. No debe acoplar el dominio al proveedor.

## Persistencia de Invitation.data

`JSONB` permite que diferentes Templates tengan diferentes campos sin alterar el esquema relacional cada vez. La estructura válida de ese JSON está gobernada por el schema de la Template.

## Almacenamiento de archivos

PostgreSQL almacena metadata y `storage_key`; Object Storage contiene el binario.
