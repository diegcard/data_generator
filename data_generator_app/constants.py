"""
Constantes utilizadas en la generación de datos de televisiones.
"""

# Marcas de televisores
BRANDS = [
    "Samsung", "LG", "Sony", "Panasonic", "Philips", "TCL", "Hisense", 
    "Sharp", "Vizio", "Toshiba", "JVC", "Xiaomi", "OnePlus", "Realme"
]

# Tipos de pantalla (tecnologías de display)
DISPLAY_TECHNOLOGIES = ["LED", "OLED", "QLED", "Mini-LED", "LCD", "Plasma", "MicroLED"]

# Resoluciones
RESOLUTIONS = ["HD", "Full HD", "4K UHD", "8K UHD"]

# Tamaños de pantalla (en pulgadas)
SCREEN_SIZES_INCHES = [32, 40, 43, 50, 55, 58, 65, 70, 75, 85, 98]

# Rangos de precio en USD (según combinaciones de marca/tamaño/tecnología)
PRICE_USD = {
    "Básico": (200, 500),
    "Medio": (500, 1500),
    "Premium": (1500, 3000),
    "Gama Alta": (3000, 10000)
}

# Clasificaciones de calidad (1-5 estrellas)
QUALITY_RATING = [1, 2, 3, 4, 5]

# Tasas de refresco (Hz)
REFRESH_RATES_HZ = [60, 75, 90, 120, 144, 240]

# Plataformas Smart TV
SMART_TV_PLATFORMS = [
    "Android TV", "Google TV", "WebOS", "Tizen", "Roku TV", 
    "Fire TV", "Vidaa", "SmartCast", "My Home Screen"
]

# Formatos HDR soportados
HDR_FORMATS_SUPPORTED = ["HDR10", "HDR10+", "Dolby Vision", "HLG", "None"]

# Número de puertos HDMI
NUMBER_OF_HDMI_PORTS = [1, 2, 3, 4, 5]

# Número de puertos USB
NUMBER_OF_USB_PORTS = [0, 1, 2, 3, 4]

# Potencia de salida de audio (Watts)
AUDIO_OUTPUT_WATTS = [10, 15, 20, 30, 40, 50, 60, 80]

# Asistentes de voz soportados
VOICE_ASSISTANT_SUPPORT = ["Alexa", "Google Assistant", "Bixby", "Siri", "None", "Multiple"]

# Tipos de sintonizador
TUNER_TYPE = ["ATSC", "DVB-T2", "ISDB-T", "DTMB", "Hybrid"]

# Países de origen
COUNTRY_OF_ORIGIN = [
    "China", "Corea del Sur", "Japón", "Estados Unidos", 
    "Malasia", "México", "Taiwán", "Vietnam", "Tailandia"
]

# Ubicaciones de almacén
WAREHOUSE_LOCATION = [
    "Los Angeles", "New York", "Chicago", "Houston", "Miami",
    "Seattle", "Dallas", "Atlanta", "Denver", "Boston",
    "Shanghái", "Shenzhen", "Tokio", "Seúl", "Ámsterdam"
]

# Años de garantía
WARRANTY_YEARS = [1, 2, 3, 5]

# Colores disponibles
COLOR = ["Negro", "Blanco", "Plateado", "Gris", "Azul", "Rojo"]

# Certificaciones ecológicas
ECO_FRIENDLY_CERTIFICATIONS = [
    "Energy Star", "EPEAT", "RoHS", "TCO Certified", 
    "Eco-Flower", "Blue Angel", "None"
]

# Años de fabricación
MANUFACTURE_YEAR = list(range(2018, 2026))

# Clasificaciones de eficiencia energética
ENERGY_STAR_RATING = ["A+++", "A++", "A+", "A", "B", "C", "D"]

# Nombres de las columnas para el DataFrame final
COLUMN_NAMES = [
    "PRODUCT_SKU",
    "BRAND",
    "MODEL",
    "DISPLAY_TECHNOLOGY",
    "SCREEN_SIZE_INCHES",
    "RESOLUTION",
    "PRICE_USD",
    "QUALITY_RATING",
    "REFRESH_RATE_HZ",
    "SMART_TV_PLATFORM",
    "HDR_FORMATS",
    "HDMI_PORTS",
    "USB_PORTS",
    "AUDIO_OUTPUT_WATTS",
    "HAS_WIFI",
    "HAS_BLUETOOTH",
    "VOICE_ASSISTANT",
    "TUNER_TYPE",
    "MANUFACTURE_YEAR",
    "ENERGY_RATING",
    "COUNTRY_OF_ORIGIN",
    "SUPPLIER_ID",
    "WAREHOUSE_LOCATION",
    "STOCK_QUANTITY",
    "CUSTOMER_RATING",
    "IS_CURVED",
    "WEIGHT_KG",
    "DIMENSIONS_CM",
    "WARRANTY_YEARS",
    "RELEASE_DATE",
    "COLOR",
    "ECO_CERTIFICATIONS",
    "POWER_CONSUMPTION_WATTS",
    "INPUT_LAG_MS",
]
