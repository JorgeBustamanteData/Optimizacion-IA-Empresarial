import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Título principal
st.title("Optimización Empresarial con IA - Prototipo")
st.markdown("**Conectado con ERP como Odoo** | 🏢 Desarrollado con amor por Jorge Bustamante Data Science ❤️")

# Configuración de dos columnas
col1, col2 = st.columns(2)

# Datos iniciales
datasets = {
    'Freemium Comercio': 'freemium_comercio.csv',
    'Freemium Tecnología': 'freemium_tecnologia.csv',
    'Freemium Salud': 'freemium_salud.csv',
    'Freemium Finanzas': 'freemium_finanzas.csv'
}

tipo_datos = col1.radio("Selecciona la fuente de datos:", list(datasets.keys()) + ['Subir CSV'])

if tipo_datos == 'Subir CSV':
    archivo_subido = col1.file_uploader("Sube tu archivo CSV", type=['csv'])
    if archivo_subido is not None:
        try:
            df_total = pd.read_csv(archivo_subido)
            st.success("Archivo subido correctamente.")
        except Exception as e:
            st.error(f"Error al cargar el archivo: {e}")
            df_total = pd.DataFrame()
else:
    try:
        df_total = pd.read_csv(datasets[tipo_datos])
    except FileNotFoundError:
        col1.error(f"No se pudo encontrar el archivo {datasets[tipo_datos]}")
        df_total = pd.DataFrame()

# Visualización de los datos en la columna izquierda
if 'df_total' in locals() and not df_total.empty:
    col1.dataframe(df_total)

    # Sección derecha - Gráficos y opciones de optimización
    col2.subheader("Visualización de los Datos")
    columna_seleccionada = col2.selectbox("Selecciona la columna para graficar:", df_total.columns)
    tipo_grafico = col2.selectbox("Selecciona el tipo de gráfico:", ['Líneas', 'Barras', 'Histograma'])

    if tipo_grafico == 'Líneas':
        fig = px.line(df_total, x=df_total.index, y=columna_seleccionada, title=f"Gráfico de Líneas - {columna_seleccionada}")
    elif tipo_grafico == 'Barras':
        fig = px.bar(df_total, x=df_total.index, y=columna_seleccionada, title=f"Gráfico de Barras - {columna_seleccionada}")
    elif tipo_grafico == 'Histograma':
        fig = px.histogram(df_total, x=columna_seleccionada, title=f"Histograma - {columna_seleccionada}")

    col2.plotly_chart(fig)

    # Aplicar optimización con IA
    if col2.button("Aplicar IA para Optimizar"):
        try:
            # Preparación de los datos para el modelo predictivo
            df_numerico = df_total.select_dtypes(include=[np.number]).dropna()
            if not df_numerico.empty and columna_seleccionada in df_numerico.columns:
                X = df_numerico.drop(columns=[columna_seleccionada])
                y = df_numerico[columna_seleccionada]
                X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

                # Modelo de regresión lineal
                modelo = LinearRegression()
                modelo.fit(X_train, y_train)

                # Predicción
                predicciones = modelo.predict(X_test)

                # Mostrar resultados
                col2.success("Optimización completada con éxito.")
                col2.write(f"Predicciones para {columna_seleccionada}:")
                resultados = pd.DataFrame({
                    'Predicción': predicciones,
                    'Real': y_test.values
                })
                col2.write(resultados)

                # Explicación del análisis
                col2.markdown(f"**Análisis del Resultado:** La IA ha realizado una predicción basada en los datos históricos proporcionados. Esto te permitirá visualizar tendencias, identificar patrones y tomar decisiones estratégicas informadas para optimizar **{columna_seleccionada}**.")
            else:
                col2.error("No se encontraron suficientes columnas numéricas para aplicar la optimización con IA o la columna seleccionada no es numérica.")
        except Exception as e:
            col2.error(f"Error durante la optimización: {e}")

# Información sobre suscripciones
st.markdown("## 💡 Opciones de Suscripción")
st.markdown("**Freemium:** Acceso limitado a datasets públicos y funcionalidades básicas de optimización.")
st.markdown("**Premium:** Acceso completo a datasets avanzados, integración con ERP como Odoo, y análisis predictivos avanzados.")
st.markdown("**Enterprise:** Soluciones personalizadas, soporte dedicado y automatización completa de procesos empresariales.")

# Pie de página
st.markdown("---")
st.markdown("**Desarrollado con ❤️ por Jorge Bustamante Data Science**")