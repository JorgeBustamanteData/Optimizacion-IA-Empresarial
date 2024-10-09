# **Optimizacion-IA-Empresarial**

## Descripción del Proyecto

Este repositorio contiene el desarrollo del MVP de una herramienta de **Optimización Empresarial con Inteligencia Artificial**. Esta aplicación está diseñada para ayudar a las empresas a mejorar sus procesos y la toma de decisiones mediante el análisis predictivo y la simulación optimizada. Utiliza técnicas de **Machine Learning** y una interfaz interactiva construida en **Streamlit** para ofrecer recomendaciones que maximicen la eficiencia y rentabilidad empresarial.

## Estructura del Proyecto

- **src/**: Contiene todos los archivos de código fuente.
  - `ingreso_datos.py`: Módulo para la carga y validación de datos de los usuarios.
  - `simulacion.py`: Realiza la simulación y el análisis optimizado a partir de los datos ingresados.
  - `visualizacion.py`: Módulo que maneja la visualización de los resultados.
  - `funciones_premium.py`: Contiene la funcionalidad avanzada para la versión premium de la herramienta.
- **data/**: Carpeta destinada a almacenar archivos CSV con datos de prueba.
- **models/**: Carpeta para guardar los modelos de Machine Learning entrenados.
- **assets/**: Carpeta para las imágenes y otros recursos visuales utilizados en la interfaz.
- **app.py**: Archivo principal de la aplicación en Streamlit, que une los módulos y crea la interfaz para el usuario.
- **requirements.txt**: Archivo con las dependencias necesarias para ejecutar el proyecto.

## Características Principales

- **Interfaz Interactiva**: La aplicación está construida con **Streamlit**, lo que permite una experiencia fácil de usar, donde los usuarios pueden cargar sus propios datos y observar resultados en tiempo real.
- **Modelos de Machine Learning**: Utilizamos modelos de regresión lineal para predecir resultados y optimizar las decisiones.
- **Funcionalidad Freemium/Premium**: El MVP incluirá una versión gratuita y una versión premium con funcionalidades avanzadas, como el uso de técnicas complejas y modelos avanzados de aprendizaje.

## Requisitos

Para ejecutar este proyecto, asegúrate de tener **Python 3.7+** instalado y luego instala las dependencias usando:

```sh
pip install -r requirements.txt
```

## Ejecución de la Aplicación

Para correr la aplicación localmente, usa el siguiente comando:

```sh
streamlit run app.py
```

Esto abrirá la aplicación en tu navegador, donde podrás interactuar con ella cargando datos y observando los resultados optimizados.

## Contribuir

Este proyecto está en sus etapas iniciales y cualquier contribución es bienvenida. Si encuentras un problema o tienes sugerencias, por favor abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más información.

