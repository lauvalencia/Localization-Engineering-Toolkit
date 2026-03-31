import re

# 1. Leer archivos
with open('en-US.json', 'r', encoding='utf-8') as f:
    json_original = f.read()

with open('textos_traducidos.txt', 'r', encoding='utf-8') as f:
    traducciones = [line.replace("[CONTIENE VARIABLES] ", "").strip() 
                    for line in f if line.strip()]

# 2. NUEVO REGEX: Capturamos la clave, los dos puntos y el valor
# Buscamos: (":\s*") seguido de ("texto original")
pattern = r'(:\s*")([^"]*)(")'

# 3. Iterador de traducciones
iterador_traducciones = iter(traducciones)

def reemplazar(match):
    try:
        inicio = match.group(1)
        original = match.group(2) # Texto en inglés
        cierre = match.group(3)
        
        nueva_version = next(iterador_traducciones)
        traduccion_limpia = nueva_version.replace("[[ ", "{").replace(" ]]", "}")
        
        # --- NUEVA LÓGICA DE VALIDACIÓN ---
        # Buscamos variables en el original y en la traducción
        vars_original = re.findall(r'\{[^}]+\}', original)
        vars_traduccion = re.findall(r'\{[^}]+\}', traduccion_limpia)
        
        if set(vars_original) != set(vars_traduccion):
            print(f"⚠️ ERROR DE QA: Las variables no coinciden.")
            print(f"   Original: {vars_original}")
            print(f"   Traducción: {vars_traduccion}")
            # Si hay error, podrías decidir dejar el original para no romper la app
            return f"{inicio}{original}{cierre}" 
        
        return f"{inicio}{traduccion_limpia}{cierre}"
    except StopIteration:
        return match.group(0)

# 4. Inyectar
nuevo_json = re.sub(pattern, reemplazar, json_original)

# 5. Guardar
with open('es-ES.json', 'w', encoding='utf-8') as f:
    f.write(nuevo_json)

print("¡Ahora sí! Proceso completado sin errores de Lookbehind.")