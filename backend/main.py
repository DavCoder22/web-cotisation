from valores import cotizar, solicitar_dato

def main():
    print("--- Cotizador de Impresión 3D ---")
    
    # Solicitar datos al usuario
    largo = solicitar_dato("Ingresa el largo del modelo (cm): ", float, lambda x: x > 0)
    ancho = solicitar_dato("Ingresa el ancho del modelo (cm): ", float, lambda x: x > 0)
    alto = solicitar_dato("Ingresa el alto del modelo (cm): ", float, lambda x: x > 0)
    densidad = solicitar_dato("Ingresa la densidad del infill (%): ", float, lambda x: 0 < x <= 100)
    tipo_filamento = solicitar_dato("Ingresa el tipo de filamento (pla, ptge, tpu, abs): ", str, lambda x: x in ["pla", "ptge", "tpu", "abs"])
    requiere_acabados = solicitar_dato("¿Requiere acabados? (sí/no): ", str, lambda x: x.lower() in ["sí", "no"]) == "sí"
    entrega_local = solicitar_dato("¿La entrega es en la universidad? (sí/no): ", str, lambda x: x.lower() in ["sí", "no"]) == "sí"

    # Calcular datos derivados
    volumen_total = largo * ancho * alto * (densidad / 100)
    peso_material = volumen_total * 1.24  # Densidad del PLA en g/cm³
    tiempo_impresion = volumen_total / 100  # Supuesto: 100 cm³ por hora

    # Calcular cotización
    factura = cotizar(volumen_total, peso_material, tiempo_impresion, tipo_filamento, requiere_acabados, entrega_local)

    # Mostrar resultados
    print("\n--- Factura de Cotización ---")
    for clave, valor in factura.items():
        print(f"{clave.replace('_', ' ').capitalize()}: ${valor:.2f}")
    print("-------------------------------")

if __name__ == "__main__":
    main()
