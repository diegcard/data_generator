# Generador de Datos para Televisiones

Un proyecto para generar datos sintéticos de televisiones, incluyendo características como marca, precio, calidad, tamaño y más. Diseñado para crear conjuntos de datos realistas que pueden ser utilizados en proyectos de análisis, visualización y aprendizaje automático.

## Requisitos Mínimos

- Python 3.8 o superior
- Pandas
- NumPy
- OpenPyXL (para exportación a Excel)
- Coverage (para pruebas)

## Puntos Extra

- Más del 90% de cobertura de pruebas
- Visualización de datos generados
- Exportación a múltiples formatos (CSV, JSON, Excel)
- Correlaciones realistas entre atributos

## Público Objetivo

- Estudiantes de la clase de algoritmos
- Desarrolladores de aplicaciones de comercio electrónico
- Analistas de datos que necesiten conjuntos de datos de prueba
- Estudiantes de ciencia de datos que busquen datos para prácticas

## Instrucciones de Configuración

1. Clonar el repositorio
```bash
git clone https://github.com/[usuario]/data_generator.git
cd data_generator
```

2. Crear y activar un entorno virtual (opcional pero recomendado)
```bash
python -m venv venv
# En Windows
venv\Scripts\activate
# En Unix o MacOS
source venv/bin/activate
```

3. Instalar las dependencias
```bash
pip install -r requirements.txt
```

## Cómo Ejecutar

### Usando el script principal

```bash
python main.py --rows 1000 --output televisions.csv --format csv
```

Opciones disponibles:
- `--rows`: Número de filas a generar (por defecto: 100)
- `--output`: Nombre del archivo de salida (por defecto: television_data.csv)
- `--format`: Formato del archivo (opciones: csv, json, excel; por defecto: csv)

### Usando como módulo

```python
from data_generator_app.data_generator import generate_television_data

# Generar 100 registros
data = generate_television_data(100)

# Guardar a CSV
data.to_csv("television_data.csv", index=False)
```

## Ejecutar Pruebas

Para ejecutar todas las pruebas:

```bash
python -m unittest discover -s tests
```

Para ejecutar pruebas con cobertura:

```bash
coverage run -m unittest discover -s tests
coverage report
coverage html  # Genera informe HTML detallado
```

## Descripción de las Columnas

El conjunto de datos generado incluye las siguientes columnas (aproximadamente 30):

1. **PRODUCT_SKU**: Identificador único del producto (clave primaria)
2. **BRAND**: Marca del televisor (Samsung, LG, Sony, etc.)
3. **MODEL**: Número de modelo específico 
4. **DISPLAY_TECHNOLOGY**: Tecnología de pantalla (LED, OLED, QLED, etc.)
5. **SCREEN_SIZE_INCHES**: Tamaño diagonal de la pantalla en pulgadas
6. **RESOLUTION**: Resolución de la pantalla (HD, Full HD, 4K UHD, 8K UHD)
7. **PRICE_USD**: Precio en dólares estadounidenses
8. **QUALITY_RATING**: Calificación de calidad (1-5)
9. **REFRESH_RATE_HZ**: Tasa de refresco en Hz (60, 120, 144, etc.)
10. **SMART_TV_PLATFORM**: Plataforma de Smart TV (Android TV, WebOS, Tizen, etc.)
11. **HDR_FORMATS**: Formatos HDR soportados (HDR10, Dolby Vision, etc.)
12. **HDMI_PORTS**: Número de puertos HDMI
13. **USB_PORTS**: Número de puertos USB
14. **AUDIO_OUTPUT_WATTS**: Potencia de salida de audio en watts
15. **HAS_WIFI**: Indica si el televisor tiene WiFi (booleano)
16. **HAS_BLUETOOTH**: Indica si el televisor tiene Bluetooth (booleano)
17. **VOICE_ASSISTANT**: Asistente de voz soportado (Alexa, Google Assistant, etc.)
18. **TUNER_TYPE**: Tipo de sintonizador (ATSC, DVB-T2, etc.)
19. **MANUFACTURE_YEAR**: Año de fabricación
20. **ENERGY_RATING**: Clasificación de eficiencia energética (A+++, A++, etc.)
21. **COUNTRY_OF_ORIGIN**: País de fabricación
22. **SUPPLIER_ID**: Identificador del proveedor
23. **WAREHOUSE_LOCATION**: Ubicación del almacén
24. **STOCK_QUANTITY**: Cantidad en inventario
25. **CUSTOMER_RATING**: Calificación promedio de clientes (1-5)
26. **IS_CURVED**: Indica si la pantalla es curva (booleano)
27. **WEIGHT_KG**: Peso en kilogramos
28. **DIMENSIONS_CM**: Dimensiones en centímetros (AnchoxAltoxProfundidad)
29. **WARRANTY_YEARS**: Años de garantía
30. **RELEASE_DATE**: Fecha de lanzamiento
31. **COLOR**: Color del televisor
32. **ECO_CERTIFICATIONS**: Certificaciones ecológicas
33. **POWER_CONSUMPTION_WATTS**: Consumo de energía en watts
34. **INPUT_LAG_MS**: Retardo de entrada en milisegundos (importante para gaming)

## Requisitos Cumplidos

- ✅ Repositorio público en GitHub
- ✅ Desarrollo basado en pruebas (TDD) con más del 90% de cobertura
- ✅ Una tabla con aproximadamente 30 columnas
- ✅ Número variable de filas
- ✅ Clave única (PRODUCT_SKU)
- ✅ Semejanza mínima con datos del mundo real
