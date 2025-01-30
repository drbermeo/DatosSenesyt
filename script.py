import pandas as pd
import json
import os

def excel_a_json(ruta_excel, ruta_json):
    try:
        # Leer el archivo Excel
        df = pd.read_excel(ruta_excel, dtype=str)
        
        # Convertir NaN a cadenas vacías y normalizar datos
        df = df.fillna('')
        datos = df.to_dict(orient='records')
        
        # Convertir todos los valores a strings y manejar vacíos
        registros = []
        for registro in datos:
            limpio = {str(k): str(v).strip() if pd.notnull(v) else '' for k, v in registro.items()}
            registros.append(limpio)
        
        # Guardar como JSON
        with open(ruta_json, 'w', encoding='utf-8') as f:
            json.dump(registros, f, indent=4, ensure_ascii=False)
        
        return True
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return False

if __name__ == "__main__":
    # Rutas
    directorio = r"C:\Users\Diana Bermeo C\Downloads\captchat"
    archivo_excel = os.path.join(directorio, "Titulos.xls")
    archivo_json = os.path.join(directorio, "InformacionTitulos.json")
    
    # Validar existencia del archivo Excel
    if not os.path.exists(archivo_excel):
        print(f"Error: El archivo {archivo_excel} no existe")
    else:
        # Convertir y guardar JSON
        if excel_a_json(archivo_excel, archivo_json):
            print(f"Archivo JSON generado con éxito en:\n{archivo_json}")
            print(f"Registros procesados: {len(pd.read_excel(archivo_excel))}")
        else:
            print("Error en la conversión")