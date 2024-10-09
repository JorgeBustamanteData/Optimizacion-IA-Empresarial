import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Función para generar un dataset ficticio
def generar_datos_ficticios(nombre_archivo, num_registros=100):
    fechas = [datetime(2023, 1, 1) + timedelta(days=i*30) for i in range(num_registros)]
    ventas = np.random.randint(5000, 50000, num_registros)
    costos_operativos = ventas * np.random.uniform(0.4, 0.8, num_registros)
    clientes_nuevos = np.random.randint(10, 100, num_registros)
    promociones = np.random.choice(['Sí', 'No'], num_registros)
    productos = np.random.choice(['Electrónicos', 'Alimentos', 'Textiles', 'Servicios'], num_registros)
    regiones = np.random.choice(['Norteamérica', 'Europa', 'Latinoamérica', 'Asia'], num_registros)
    utilidad_bruta = ventas - costos_operativos
    tasa_retencion = np.random.uniform(0.5, 0.95, num_registros)

    # Crear DataFrame
    df = pd.DataFrame({
        'Fecha': fechas,
        'Ventas_USD': ventas,
        'Costos_Operativos_USD': costos_operativos,
        'Clientes_Nuevos': clientes_nuevos,
        'Promociones': promociones,
        'Producto': productos,
        'Región': regiones,
        'Utilidad_Bruta_USD': utilidad_bruta,
        'Tasa_Retencion': tasa_retencion
    })

    # Guardar en CSV
    df.to_csv(nombre_archivo, index=False)
    print(f"Archivo '{nombre_archivo}' generado correctamente con {num_registros} registros.")

# Generar datasets ficticios para la versión freemium
generar_datos_ficticios('freemium_comercio.csv')
generar_datos_ficticios('freemium_tecnologia.csv')
generar_datos_ficticios('freemium_salud.csv')
generar_datos_ficticios('freemium_finanzas.csv')

def generar_datos_reales(nombre_archivo, fuente_datos_url):
    # Este código simula la descarga de datos desde una fuente pública y su procesamiento
    try:
        df = pd.read_csv(fuente_datos_url)
        df.to_csv(nombre_archivo, index=False)
        print(f"Archivo '{nombre_archivo}' generado a partir de datos reales de la fuente proporcionada.")
    except Exception as e:
        print(f"Error al intentar descargar los datos reales: {e}")

import os
import pandas as pd
import numpy as np
import requests
from io import StringIO

# Generar conjuntos de datos ficticios para la versión Freemium
def generar_datos_ficticios(nombre_archivo, num_registros):
    data = {
        'Fecha': pd.date_range(start='2023-01-01', periods=num_registros, freq='D'),
        'Ventas': np.random.randint(1000, 5000, size=num_registros),
        'Clientes': np.random.randint(50, 200, size=num_registros),
        'Satisfacción Cliente (%)': np.random.uniform(60, 100, size=num_registros).round(2),
        'Costos Operativos': np.random.randint(500, 3000, size=num_registros)
    }
    df = pd.DataFrame(data)
    df.to_csv(nombre_archivo, index=False)
    print(f"Archivo '{nombre_archivo}' generado correctamente con {num_registros} registros.")

# Descargar datos reales desde fuentes públicas
def descargar_datos_reales(url, nombre_archivo):
    try:
        response = requests.get(url)
        response.raise_for_status()
        df = pd.read_csv(StringIO(response.text), delimiter=",")
        df.to_csv(nombre_archivo, index=False)
        print(f"Archivo '{nombre_archivo}' descargado correctamente desde {url}.")
    except requests.exceptions.RequestException as e:
        print(f"Error al intentar descargar los datos reales: {e}")

# Generar archivos ficticios para la versión Freemium
sectores = ['comercio', 'tecnologia', 'salud', 'finanzas']
for sector in sectores:
    generar_datos_ficticios(f'freemium_{sector}.csv', 100)

# URLs para la descarga de datos reales
urls_reales = {
    'comercio': 'https://datahub.io/core/global-temp/r/annual.csv',
    'tecnologia': 'https://datahub.io/machine-learning/iris/r/iris.csv',
    'salud': 'https://datahub.io/core/covid-19/r/countries-aggregated.csv',
    'finanzas': 'https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv'
}

# Descargar archivos reales para la versión de pago
for sector, url in urls_reales.items():
    descargar_datos_reales(url, f'reales_{sector}.csv')