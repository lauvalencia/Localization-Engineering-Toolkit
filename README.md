# 🌐 Localization Engineering Toolkit (Python)

Este proyecto demuestra un flujo de trabajo automatizado para la localización de software, diseñado para prevenir errores comunes en la traducción de archivos JSON.

## 🛠️ Tecnologías utilizadas
* **Python 3.13**
* **RegEx** (Expresiones Regulares)
* **JSON** (Estructura de datos de software)

## 🚀 Funcionalidades
1. **Extracción:** Aísla el texto traducible del código técnico.
2. **Protección de Variables:** Identifica automáticamente `{placeholders}` para evitar que el traductor los modifique.
3. **Validación (QA):** Compara el archivo original con la traducción para asegurar que no se perdieron variables críticas.
4. **Inyección:** Reconstruye el archivo original con las nuevas traducciones manteniendo la sintaxis perfecta.

## 📈 Impacto
Este flujo reduce el riesgo de "crashes" en aplicaciones por errores de sintaxis y optimiza el tiempo de preparación de archivos para equipos lingüísticos.
