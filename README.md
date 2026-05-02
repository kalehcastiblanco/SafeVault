# SafeVault - Secure Web Application

## Objetivo
Sistema seguro para manejo de usuarios con protección contra vulnerabilidades comunes.

---

## Funcionalidades implementadas

- Validación de entrada de usuario
- Prevención de SQL Injection mediante consultas seguras
- Sanitización contra XSS
- Autenticación de usuarios con hashing SHA-256
- Control de acceso basado en roles (RBAC)
- Pruebas de seguridad automatizadas

---

## Vulnerabilidades tratadas

- SQL Injection → mitigado con consultas parametrizadas
- XSS → mitigado con sanitización de entrada
- Acceso no autorizado → controlado con RBAC

---

## Herramientas utilizadas

- Python
- SQLite
- Microsoft Copilot
- VS Code

---

## Pruebas realizadas

- Inyección SQL simulada
- Ataques XSS simulados
- Intentos de acceso inválido
- Validación de roles

---

## Conclusión

El sistema implementa una arquitectura básica de seguridad en capas:
entrada segura → autenticación → autorización → validación → pruebas.
