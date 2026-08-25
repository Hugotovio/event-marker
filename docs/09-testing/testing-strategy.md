# Estrategia de Pruebas

Pendiente.
# Event Maker — Estrategia de Pruebas

## 1. Objetivo

Definir la estrategia de pruebas del MVP de Event Maker.

Las pruebas deben permitir comprobar que:

- las reglas de negocio funcionan;
- los datos mantienen su integridad;
- los usuarios solamente acceden a sus recursos;
- los pagos se procesan correctamente;
- las invitaciones se publican correctamente;
- los errores se manejan adecuadamente;
- las funcionalidades principales funcionan de extremo a extremo.

---

# 2. Principios

Las pruebas deben:

1. ejecutarse automáticamente cuando sea posible;
2. ser reproducibles;
3. detectar regresiones;
4. cubrir reglas críticas;
5. ser independientes de proveedores externos cuando corresponda;
6. ejecutarse durante el desarrollo y antes del despliegue.

---

# 3. Pirámide de pruebas

La estrategia seguirá una estructura aproximada:

```text
              ┌───────────────┐
              │      E2E      │
              └───────┬───────┘
                      │
             ┌────────┴────────┐
             │   Integration   │
             └────────┬────────┘
                      │
            ┌─────────┴─────────┐
            │       Unit        │
            └───────────────────┘