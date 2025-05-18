"""
Módulo principal para generar datos sintéticos de televisiones.
"""

import random
import pandas as pd
import numpy as np
import uuid
import os
from datetime import datetime, timedelta
from .constants import (
    BRANDS, DISPLAY_TECHNOLOGIES, RESOLUTIONS, SCREEN_SIZES_INCHES, 
    PRICE_USD, QUALITY_RATING, REFRESH_RATES_HZ, SMART_TV_PLATFORMS,
    HDR_FORMATS_SUPPORTED, NUMBER_OF_HDMI_PORTS, NUMBER_OF_USB_PORTS,
    AUDIO_OUTPUT_WATTS, VOICE_ASSISTANT_SUPPORT, TUNER_TYPE,
    COUNTRY_OF_ORIGIN, WAREHOUSE_LOCATION, WARRANTY_YEARS,
    COLOR, ECO_FRIENDLY_CERTIFICATIONS, MANUFACTURE_YEAR,
    ENERGY_STAR_RATING, COLUMN_NAMES
)


def generate_unique_sku(existing_skus):
    """
    Genera un SKU único para un producto de televisión.
    
    Args:
        existing_skus (set): Conjunto de SKUs existentes para evitar duplicados.
        
    Returns:
        str: SKU único generado.
    """
    while True:
        # Genera un prefijo de 2 letras mayúsculas
        prefix = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=2))
        
        # Genera un número de 6 dígitos
        number = random.randint(100000, 999999)
        
        # Combina para crear el SKU
        sku = f"{prefix}{number}"
        
        # Verifica si ya existe
        if sku not in existing_skus:
            return sku


def generate_tv_data_row(sku):
    """
    Genera una fila de datos para un televisor.
    
    Args:
        sku (str): SKU único para el producto.
        
    Returns:
        dict: Diccionario con datos del televisor.
    """
    # Seleccionar características base
    brand = random.choice(BRANDS)
    display_tech = random.choice(DISPLAY_TECHNOLOGIES)
    screen_size = random.choice(SCREEN_SIZES_INCHES)
    resolution = random.choice(RESOLUTIONS)
    
    # Generar modelo basado en la marca y características
    model = _generate_model_name(brand, screen_size, display_tech)
    
    # Generar precio con correlaciones realistas
    price = _generate_price(brand, screen_size, resolution, display_tech)
    
    # Generar año de fabricación
    manufacture_year = random.choice(MANUFACTURE_YEAR)
    
    # La fecha de lanzamiento debe ser consistente con el año de fabricación
    release_date = _generate_release_date(manufacture_year)
    
    # Generar calificación de calidad (correlacionada con marca y precio)
    quality_rating = _generate_quality_rating(brand, price)
    
    # Generar calificación de clientes (correlacionada con calidad)
    customer_rating = round(min(5.0, max(1.0, quality_rating + random.uniform(-0.8, 0.8))), 1)
    
    # Generar características técnicas
    refresh_rate = _get_refresh_rate(display_tech, price)
    smart_platform = random.choice(SMART_TV_PLATFORMS)
    
    # Generar formatos HDR (más probable en TVs premium)
    hdr_formats = _generate_hdr_formats(price, resolution)
    
    # Características de conectividad
    hdmi_ports = _get_ports(price, NUMBER_OF_HDMI_PORTS)
    usb_ports = _get_ports(price, NUMBER_OF_USB_PORTS)
    has_wifi = random.random() < 0.95  # 95% tienen WiFi
    has_bluetooth = random.random() < 0.75  # 75% tienen Bluetooth
    
    # Características de audio
    audio_watts = _get_audio_watts(screen_size, price)
    
    # Asistente de voz (más común en TVs premium)
    voice_assistant = _get_voice_assistant(price, smart_platform)
    
    # Características físicas
    is_curved = random.random() < 0.15  # 15% son curvos
    weight_kg = _calculate_weight(screen_size, display_tech)
    dimensions = _calculate_dimensions(screen_size)
    
    # Características energéticas
    energy_rating = random.choice(ENERGY_STAR_RATING)
    power_consumption = _calculate_power_consumption(screen_size, display_tech)
    
    # Información de juegos
    input_lag_ms = _calculate_input_lag(refresh_rate, display_tech)
    
    # Información de inventario y venta
    supplier_id = f"SUP{random.randint(1000, 9999)}"
    warehouse = random.choice(WAREHOUSE_LOCATION)
    stock = max(0, int(np.random.normal(50, 30)))
    
    # Características adicionales
    tuner = random.choice(TUNER_TYPE)
    warranty = random.choice(WARRANTY_YEARS)
    color = random.choice(COLOR)
    
    # Certificaciones ecológicas (más probables en marcas premium)
    eco_certs = _generate_eco_certifications(brand, price)
    
    # Crear y retornar el diccionario de datos
    return {
        "PRODUCT_SKU": sku,
        "BRAND": brand,
        "MODEL": model,
        "DISPLAY_TECHNOLOGY": display_tech,
        "SCREEN_SIZE_INCHES": screen_size,
        "RESOLUTION": resolution,
        "PRICE_USD": price,
        "QUALITY_RATING": quality_rating,
        "REFRESH_RATE_HZ": refresh_rate,
        "SMART_TV_PLATFORM": smart_platform,
        "HDR_FORMATS": ",".join(hdr_formats) if hdr_formats else "None",
        "HDMI_PORTS": hdmi_ports,
        "USB_PORTS": usb_ports,
        "AUDIO_OUTPUT_WATTS": audio_watts,
        "HAS_WIFI": has_wifi,
        "HAS_BLUETOOTH": has_bluetooth,
        "VOICE_ASSISTANT": voice_assistant,
        "TUNER_TYPE": tuner,
        "MANUFACTURE_YEAR": manufacture_year,
        "ENERGY_RATING": energy_rating,
        "COUNTRY_OF_ORIGIN": random.choice(COUNTRY_OF_ORIGIN),
        "SUPPLIER_ID": supplier_id,
        "WAREHOUSE_LOCATION": warehouse,
        "STOCK_QUANTITY": stock,
        "CUSTOMER_RATING": customer_rating,
        "IS_CURVED": is_curved,
        "WEIGHT_KG": weight_kg,
        "DIMENSIONS_CM": dimensions,
        "WARRANTY_YEARS": warranty,
        "RELEASE_DATE": release_date,
        "COLOR": color,
        "ECO_CERTIFICATIONS": ",".join(eco_certs) if eco_certs else "None",
        "POWER_CONSUMPTION_WATTS": power_consumption,
        "INPUT_LAG_MS": input_lag_ms
    }


def generate_television_data(row_count: int) -> pd.DataFrame:
    """
    Genera un conjunto de datos de televisiones.
    
    Args:
        row_count (int): Número de filas a generar.
        
    Returns:
        pd.DataFrame: DataFrame con los datos generados.
    """
    data_rows = []
    generated_skus = set()
    
    for _ in range(row_count):
        # Generar SKU único
        sku = generate_unique_sku(generated_skus)
        generated_skus.add(sku)
        
        # Generar fila de datos
        row = generate_tv_data_row(sku)
        data_rows.append(row)
    
    # Crear DataFrame con columnas en el orden definido
    df = pd.DataFrame(data_rows)
    
    # Reorganizar las columnas según el orden definido en COLUMN_NAMES
    return df[COLUMN_NAMES]


# Funciones auxiliares para la generación realista de datos

def _generate_model_name(brand, screen_size, display_tech):
    """Genera un nombre de modelo realista basado en la marca."""
    letters = "ABCDEFGHJKLMNPQRSTUVWXYZ"
    numbers = "0123456789"
    
    if brand in ["Samsung", "LG", "Sony"]:
        # Formatos típicos: QN55Q80TAFXZA, OLED55C1PUB, XBR-55A8H
        prefix = ""
        if display_tech == "QLED" and brand == "Samsung":
            prefix = "QN"
        elif display_tech == "OLED" and brand == "LG":
            prefix = "OLED"
        elif brand == "Sony":
            prefix = "XBR-"
        
        series = random.choice(letters)
        model_num = f"{random.randint(1, 9)}{random.choice(numbers)}"
        suffix = "".join(random.choices(letters, k=2))
        
        return f"{prefix}{screen_size}{series}{model_num}{suffix}"
    else:
        # Formato genérico para otras marcas
        prefix = random.choice(letters) + random.choice(letters)
        numbers_part = "".join(random.choices(numbers, k=4))
        return f"{prefix}-{screen_size}{numbers_part}"


def _generate_price(brand, screen_size, resolution, display_tech):
    """Genera un precio realista basado en varios factores."""
    # Base price determined by screen size
    base_price = screen_size * 10
    
    # Brand premium factor
    brand_factor = 1.0
    premium_brands = ["Samsung", "LG", "Sony"]
    mid_tier_brands = ["Panasonic", "Philips", "TCL"]
    
    if brand in premium_brands:
        brand_factor = 1.5
    elif brand in mid_tier_brands:
        brand_factor = 1.2
    
    # Resolution multiplier
    resolution_mult = {
        "HD": 0.7,
        "Full HD": 1.0,
        "4K UHD": 1.5,
        "8K UHD": 3.0
    }
    
    # Display technology multiplier
    tech_mult = {
        "LCD": 0.8,
        "LED": 1.0,
        "Plasma": 1.2,
        "QLED": 1.5,
        "Mini-LED": 1.8,
        "OLED": 2.0,
        "MicroLED": 3.0
    }
    
    # Calculate final price with some randomness
    price = base_price * brand_factor * resolution_mult[resolution] * tech_mult[display_tech]
    
    # Add noise (±15%)
    price *= random.uniform(0.85, 1.15)
    
    return round(price, 2)


def _generate_quality_rating(brand, price):
    """Genera una calificación de calidad correlacionada con la marca y el precio."""
    # Base rating influenced by brand
    premium_brands = ["Samsung", "LG", "Sony"]
    mid_tier_brands = ["Panasonic", "Philips", "TCL"]
    
    if brand in premium_brands:
        base_rating = random.uniform(3.5, 5.0)
    elif brand in mid_tier_brands:
        base_rating = random.uniform(3.0, 4.5)
    else:
        base_rating = random.uniform(2.0, 4.0)
    
    # Price influence - higher price often means better quality
    price_factor = min(1.0, price / 3000)  # Normalize price influence
    
    # Calculate final rating
    raw_rating = base_rating * 0.7 + price_factor * 1.5
    
    # Ensure rating is within 1-5 range and convert to integer
    return max(1, min(5, round(raw_rating)))


def _get_refresh_rate(display_tech, price):
    """Determina la tasa de refresco basada en tecnología y precio."""
    if price > 2000 or display_tech in ["OLED", "QLED", "MicroLED"]:
        # TVs premium tienen más probabilidad de tener tasas de refresco altas
        return random.choice([120, 144, 240] if random.random() < 0.8 else [60, 75])
    elif price > 1000:
        # TVs de gama media
        return random.choice([120, 144] if random.random() < 0.6 else [60, 75])
    else:
        # TVs económicas
        return random.choice([60, 75])


def _generate_hdr_formats(price, resolution):
    """Genera una lista de formatos HDR soportados basados en precio y resolución."""
    formats = []
    
    # Las TVs de menor resolución o precio tienen menos probabilidad de soportar HDR
    if resolution in ["HD", "Full HD"] and price < 500:
        if random.random() < 0.8:
            return []
    
    # HDR10 es el más común
    if random.random() < 0.9:
        formats.append("HDR10")
    
    # HDR10+ menos común
    if price > 700 and random.random() < 0.5:
        formats.append("HDR10+")
    
    # Dolby Vision en TVs premium
    if price > 1200 and random.random() < 0.7:
        formats.append("Dolby Vision")
    
    # HLG para contenido broadcast
    if price > 800 and random.random() < 0.6:
        formats.append("HLG")
    
    return formats


def _get_ports(price, ports_list):
    """Determina el número de puertos basado en el precio."""
    if price < 500:
        # TVs económicas tienen menos puertos
        return random.choice(ports_list[:2])
    elif price < 1500:
        # TVs de gama media
        return random.choice(ports_list[1:3])
    else:
        # TVs premium tienen más puertos
        return random.choice(ports_list[2:])


def _get_audio_watts(screen_size, price):
    """Determina la potencia de audio basada en tamaño y precio."""
    base_watts = 10
    
    # TVs más grandes tienen altavoces más potentes
    size_factor = screen_size / 50
    
    # TVs más caras suelen tener mejor audio
    price_factor = price / 1000
    
    watts = base_watts * size_factor * (0.5 + 0.5 * price_factor)
    
    # Redondear a múltiplos de 5 para realismo
    return int(round(watts / 5) * 5)


def _get_voice_assistant(price, smart_platform):
    """Determina el asistente de voz basado en plataforma y precio."""
    # TVs económicas pueden no tener asistente
    if price < 400 and random.random() < 0.7:
        return "None"
    
    # Mapeo de plataformas a asistentes típicos
    platform_assistants = {
        "Android TV": "Google Assistant",
        "Google TV": "Google Assistant",
        "WebOS": "Alexa" if random.random() < 0.5 else "Google Assistant",
        "Tizen": "Bixby" if random.random() < 0.7 else "Alexa",
        "Roku TV": "Alexa" if random.random() < 0.5 else "Google Assistant",
        "Fire TV": "Alexa",
        "Vidaa": "Alexa",
        "SmartCast": "Google Assistant" if random.random() < 0.5 else "Alexa",
        "My Home Screen": "Google Assistant" if random.random() < 0.5 else "Alexa"
    }
    
    # TVs premium pueden tener múltiples asistentes
    if price > 1500 and random.random() < 0.3:
        return "Multiple"
    
    # Usar el asistente típico de la plataforma
    return platform_assistants.get(smart_platform, random.choice(VOICE_ASSISTANT_SUPPORT))


def _calculate_weight(screen_size, display_tech):
    """Calcula el peso basado en tamaño y tecnología."""
    # Base weight with correlation to screen size (Non-linear)
    base_weight = 0.01 * (screen_size ** 1.5)
    
    # Technology factor
    tech_factor = 1.0
    if display_tech in ["OLED", "LED"]:
        tech_factor = 0.8  # Más ligeros
    elif display_tech in ["LCD", "QLED"]:
        tech_factor = 1.0
    elif display_tech in ["Plasma", "MicroLED"]:
        tech_factor = 1.2  # Más pesados
    
    weight = base_weight * tech_factor
    
    # Add some noise (±10%)
    weight *= random.uniform(0.9, 1.1)
    
    return round(weight, 1)


def _calculate_dimensions(screen_size):
    """Calcula las dimensiones basadas en el tamaño de pantalla."""
    # Aproximación de dimensiones para una relación de aspecto 16:9
    # Diagonal (pulgadas) a ancho y alto (cm)
    width_cm = screen_size * 2.54 * 0.87  # 87% de la diagonal en horizontal
    height_cm = screen_size * 2.54 * 0.49  # 49% de la diagonal en vertical
    
    # Profundidad correlacionada con tamaño pero no linealmente
    depth_cm = 5 + (screen_size / 50)
    
    # Añadir algo de variación
    width_cm *= random.uniform(0.98, 1.02)
    height_cm *= random.uniform(0.98, 1.02)
    depth_cm *= random.uniform(0.95, 1.05)
    
    return f"{round(width_cm)}W x {round(height_cm)}H x {round(depth_cm, 1)}D"


def _calculate_power_consumption(screen_size, display_tech):
    """Calcula el consumo energético basado en tamaño y tecnología."""
    # Consumo base según tamaño
    base_consumption = screen_size * 1.5
    
    # Factor de tecnología
    tech_factor = 1.0
    if display_tech == "OLED":
        tech_factor = 0.9  # Más eficiente en escenas oscuras
    elif display_tech == "LED":
        tech_factor = 1.0
    elif display_tech == "LCD":
        tech_factor = 1.1
    elif display_tech in ["QLED", "Mini-LED"]:
        tech_factor = 1.2
    elif display_tech == "Plasma":
        tech_factor = 1.5  # Menos eficiente
    
    consumption = base_consumption * tech_factor
    
    # Añadir algo de variación
    consumption *= random.uniform(0.9, 1.1)
    
    return round(consumption)


def _calculate_input_lag(refresh_rate, display_tech):
    """Calcula el lag de entrada basado en tasa de refresco y tecnología."""
    # Base lag inversamente proporcional a refresh rate
    base_lag = 40 - (refresh_rate / 8)
    
    # Technology factor
    tech_factor = 1.0
    if display_tech == "OLED":
        tech_factor = 0.8  # Menor lag
    elif display_tech in ["QLED", "Mini-LED"]:
        tech_factor = 0.9
    elif display_tech == "LED":
        tech_factor = 1.0
    elif display_tech == "LCD":
        tech_factor = 1.2
    elif display_tech == "Plasma":
        tech_factor = 1.3
    
    lag = base_lag * tech_factor
    
    # Add some noise
    lag *= random.uniform(0.85, 1.15)
    
    return max(1, round(lag))


def _generate_release_date(year):
    """Genera una fecha de lanzamiento basada en el año de fabricación."""
    # Los modelos suelen lanzarse en el primer semestre del año
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 6, 30)
    
    # Número de días entre las fechas
    days_between = (end_date - start_date).days
    
    # Fecha aleatoria dentro del rango
    random_days = random.randint(0, days_between)
    release_date = start_date + timedelta(days=random_days)
    
    return release_date.strftime("%Y-%m-%d")


def _generate_eco_certifications(brand, price):
    """Genera certificaciones ecológicas basadas en la marca y el precio."""
    certifications = []
    
    # Probabilidad base
    base_prob = 0.3
    
    # Las marcas premium suelen tener más certificaciones
    premium_brands = ["Samsung", "LG", "Sony", "Panasonic", "Philips"]
    if brand in premium_brands:
        base_prob += 0.3
    
    # Las TVs más caras suelen tener más certificaciones
    price_factor = min(0.3, price / 5000)
    prob = base_prob + price_factor
    
    # Generar certificaciones
    for cert in ECO_FRIENDLY_CERTIFICATIONS:
        if cert != "None" and random.random() < prob:
            certifications.append(cert)
    
    # Si no hay certificaciones, devolver "None"
    return certifications


# Mantener la funcionalidad del código original
class TelevisionDataGenerator:
    """
    Clase para generar datos sintéticos de televisiones con diferentes atributos.
    """
    
    def __init__(self, seed=None):
        """
        Inicializa el generador de datos.
        
        Args:
            seed (int, optional): Semilla para reproducibilidad. Por defecto None.
        """
        if seed is not None:
            random.seed(seed)
            np.random.seed(seed)
    
    def generate_tv_data(self, num_records=100):
        """
        Genera datos sintéticos para televisores.
        
        Args:
            num_records (int): Número de registros a generar.
            
        Returns:
            pandas.DataFrame: DataFrame con los datos generados.
        """
        return generate_television_data(num_records)
    
    def save_data(self, data, format="csv", filename="tv_data"):
        """
        Guarda los datos generados en el formato especificado.
        
        Args:
            data (pandas.DataFrame): DataFrame con los datos a guardar.
            format (str): Formato de salida. Opciones: 'csv', 'json', 'excel'.
            filename (str): Nombre base del archivo (sin extensión).
            
        Returns:
            str: Ruta del archivo guardado.
        """
        if format.lower() == "csv":
            file_path = f"{filename}.csv"
            data.to_csv(file_path, index=False)
        elif format.lower() == "json":
            file_path = f"{filename}.json"
            data.to_json(file_path, orient="records", indent=4)
        elif format.lower() == "excel":
            file_path = f"{filename}.xlsx"
            data.to_excel(file_path, index=False)
        else:
            raise ValueError(f"Formato no soportado: {format}. Use 'csv', 'json', o 'excel'.")
        
        return file_path


if __name__ == "__main__":
    # Ejemplo de uso
    generator = TelevisionDataGenerator(seed=42)
    tv_data = generator.generate_tv_data(num_records=100)
    
    # Guardar datos en diferentes formatos
    csv_path = generator.save_data(tv_data, format="csv")
    json_path = generator.save_data(tv_data, format="json")
    
    print(f"Datos generados y guardados en {csv_path} y {json_path}")
    
    # Mostrar primeras filas
    print("\nPrimeras 5 filas de datos generados:")
    print(tv_data.head(5))
