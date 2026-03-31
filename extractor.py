import re

# 1. Leer el archivo
with open('en-US.json', 'r', encoding='utf-8') as file:
    data = file.read()

# 2. Regex para extraer el contenido de las comillas
pattern_strings = r':\s*"([^"]*)"'
textos_sucios = re.findall(pattern_strings, data)

# 3. Regex para encontrar variables dentro de llaves {variable}
pattern_vars = r'\{[^}]+\}'

print("--- REPORTE DE CALIDAD LINGÜÍSTICA ---")

with open('texto_para_traducir_protegido.txt', 'w', encoding='utf-8') as out_file:
    for original in textos_sucios:
        # Buscamos si el texto tiene variables
        variables = re.findall(pattern_vars, original)
        
        if variables:
            print(f"Alerta: Protegiendo variables {variables} en: '{original}'")
            # Podríamos envolverlas o marcarlas
            marcado = original.replace("{", "[[ ").replace("}", " ]]")
            out_file.write(f"[CONTIENE VARIABLES] {marcado}\n")
        else:
            # Si es texto limpio, solo lo escribimos (filtrando IDs técnicos cortos)
            if len(original) > 3 and " " in original:
                out_file.write(original + '\n')

print("\n¡Listo! Revisa 'texto_para_traducir_protegido.txt'")