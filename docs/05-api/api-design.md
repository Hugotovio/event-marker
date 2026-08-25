# Event Maker — Diseño de API

## 1. Objetivo

Definir la estructura general de la API REST de Event Maker.

La API será utilizada por el frontend para:

- crear eventos;
- crear y modificar invitaciones;
- consultar plantillas;
- gestionar personalización;
- iniciar pagos;
- consultar estados;
- publicar invitaciones;
- recuperar invitaciones;
- consultar invitaciones públicas.

---

# 2. Versión de la API

La API utilizará versionamiento mediante URL.

```text
/api/v1/