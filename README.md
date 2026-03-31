# 🌐 Localization Engineering Toolkit (Python)

**Rol:** Localization Engineer  
**Proyecto:** Automatización de Extracción y Validación de Strings

## 📝 El Problema
Los archivos JSON de software contienen metadatos y claves técnicas críticas. Cuando un traductor humano manipula estos archivos directamente, existe un alto riesgo de alterar la sintaxis, provocando errores de compilación o "crashes" en la aplicación.

## 🛠️ La Solución (Scripts en Python)
Desarrollé un flujo de trabajo automatizado utilizando **Expresiones Regulares (Regex)** para:
1. **Extractor:** Aislar el contenido lingüístico de las claves técnicas.
2. **Protector:** Identificar y "blindar" variables como `{user_name}`.
3. **Inyector & QA:** Reinsertar las traducciones y validar que las variables coincidan exactamente con el original.

## 🚀 Impacto
* **Reducción del 100%** en errores de sintaxis JSON post-traducción.
* **Optimización de tiempo** en la preparación de archivos para equipos lingüísticos.
* **Garantía de Integridad:** El software nunca se rompe por un error de traducción.

---
*Proyecto desarrollado como parte de mi especialización en Ingeniería de Localización e IA.*