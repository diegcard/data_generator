"""
Tests para el módulo de generación de datos.
"""

import unittest
import pandas as pd
import numpy as np
import os
import tempfile
from datetime import datetime
from data_generator_app.constants import (
    BRANDS, DISPLAY_TECHNOLOGIES, RESOLUTIONS, SCREEN_SIZES_INCHES, 
    COLUMN_NAMES, REFRESH_RATES_HZ, COUNTRY_OF_ORIGIN, HDR_FORMATS_SUPPORTED,
    SMART_TV_PLATFORMS, NUMBER_OF_HDMI_PORTS, NUMBER_OF_USB_PORTS
)
import data_generator_app.data_generator as dg

# Renombrar las funciones importadas para mayor claridad
generate_unique_sku = dg.generate_unique_sku
generate_tv_data_row = dg.generate_tv_data_row
generate_television_data = dg.generate_television_data
TelevisionDataGenerator = dg.TelevisionDataGenerator


class TestDataGenerator(unittest.TestCase):
    """Clase de prueba para el generador de datos de televisiones."""
    
    def setUp(self):
        """Configuración inicial para las pruebas."""
        self.sample_size = 10
    
    def test_generate_unique_sku(self):
        """Prueba la generación de SKUs únicos."""
        # Verificar que devuelve un string
        sku = generate_unique_sku(set())
        self.assertIsInstance(sku, str)
        
        # Verificar que genera SKUs únicos
        existing_skus = set()
        for _ in range(100):
            sku = generate_unique_sku(existing_skus)
            self.assertNotIn(sku, existing_skus)
            existing_skus.add(sku)
        
        # Verificar que evita SKUs existentes
        test_sku = generate_unique_sku(set())
        existing_skus = {test_sku}
        new_sku = generate_unique_sku(existing_skus)
        self.assertNotEqual(test_sku, new_sku)
    
    def test_generate_tv_data_row(self):
        """Prueba la generación de una fila de datos."""
        # Generar SKU de muestra
        sample_sku = "AB123456"
        
        # Generar fila
        row = generate_tv_data_row(sample_sku)
        
        # Verificar que es un diccionario
        self.assertIsInstance(row, dict)
        
        # Verificar que tiene todas las columnas esperadas
        for column in COLUMN_NAMES:
            self.assertIn(column, row)
        
        # Verificar que el SKU coincide
        self.assertEqual(row["PRODUCT_SKU"], sample_sku)
        
        # Verificar que algunos valores están en los rangos/listas esperados
        self.assertIn(row["BRAND"], BRANDS)
        self.assertIn(row["DISPLAY_TECHNOLOGY"], DISPLAY_TECHNOLOGIES)
        self.assertIn(row["RESOLUTION"], RESOLUTIONS)
        self.assertIn(row["SCREEN_SIZE_INCHES"], SCREEN_SIZES_INCHES)
        self.assertIn(row["REFRESH_RATE_HZ"], REFRESH_RATES_HZ)
        
        # Verificar tipos de datos
        self.assertIsInstance(row["PRICE_USD"], float)
        self.assertIsInstance(row["QUALITY_RATING"], int)
        self.assertIsInstance(row["HAS_WIFI"], bool)
        self.assertIsInstance(row["HAS_BLUETOOTH"], bool)
    
    def test_generate_television_data_row_count(self):
        """Prueba el recuento de filas en el DataFrame generado."""
        # Probar con diferentes tamaños
        for size in [10, 50, 100]:
            df = generate_television_data(size)
            self.assertEqual(len(df), size)
    
    def test_generate_television_data_column_names(self):
        """Prueba que las columnas del DataFrame coincidan con las esperadas."""
        df = generate_television_data(5)
        
        # Verificar que todas las columnas están presentes y en el orden correcto
        self.assertListEqual(list(df.columns), COLUMN_NAMES)
    
    def test_generate_television_data_unique_key(self):
        """Prueba que los SKUs generados sean únicos."""
        df = generate_television_data(100)
        
        # Extraer columna SKU
        skus = df["PRODUCT_SKU"].values
        
        # Verificar que todos los SKUs son únicos
        self.assertEqual(len(skus), len(set(skus)))
    
    def test_data_types_and_constraints(self):
        """Prueba tipos de datos y restricciones en detalle."""
        df = generate_television_data(50)
        
        # Verificar tipos de datos
        self.assertTrue(df["BRAND"].dtype == object)  # string
        self.assertTrue(df["SCREEN_SIZE_INCHES"].dtype in [int, np.int64])
        self.assertTrue(df["PRICE_USD"].dtype in [float, np.float64])
        self.assertTrue(df["HAS_WIFI"].dtype == bool)
        self.assertTrue(df["HAS_BLUETOOTH"].dtype == bool)
        self.assertTrue(df["QUALITY_RATING"].dtype in [int, np.int64])
        self.assertTrue(df["HDMI_PORTS"].dtype in [int, np.int64])
        self.assertTrue(df["STOCK_QUANTITY"].dtype in [int, np.int64])
        self.assertTrue(df["CUSTOMER_RATING"].dtype in [float, np.float64])
        
        # Verificar que los valores están dentro de las restricciones
        self.assertTrue(all(brand in BRANDS for brand in df["BRAND"]))
        self.assertTrue(all(tech in DISPLAY_TECHNOLOGIES for tech in df["DISPLAY_TECHNOLOGY"]))
        self.assertTrue(all(res in RESOLUTIONS for res in df["RESOLUTION"]))
        self.assertTrue(all(size in SCREEN_SIZES_INCHES for size in df["SCREEN_SIZE_INCHES"]))
        self.assertTrue(all(refresh in REFRESH_RATES_HZ for refresh in df["REFRESH_RATE_HZ"]))
        self.assertTrue(all(country in COUNTRY_OF_ORIGIN for country in df["COUNTRY_OF_ORIGIN"]))
        self.assertTrue(all(platform in SMART_TV_PLATFORMS for platform in df["SMART_TV_PLATFORM"]))
        
        # Verificar rangos
        self.assertTrue(all(0 < price < 20000 for price in df["PRICE_USD"]))
        self.assertTrue(all(1 <= rating <= 5 for rating in df["QUALITY_RATING"]))
        self.assertTrue(all(1 <= rating <= 5.0 for rating in df["CUSTOMER_RATING"]))
        self.assertTrue(all(0 <= stock < 200 for stock in df["STOCK_QUANTITY"]))
        self.assertTrue(all(ports in NUMBER_OF_HDMI_PORTS for ports in df["HDMI_PORTS"]))
        self.assertTrue(all(ports in NUMBER_OF_USB_PORTS for ports in df["USB_PORTS"]))
        
        # Verificar formatos HDR
        for hdr_list in df["HDR_FORMATS"]:
            if hdr_list != "None":
                for format in hdr_list.split(","):
                    self.assertIn(format, HDR_FORMATS_SUPPORTED)
    
    def test_original_tv_generator_class(self):
        """Prueba la clase TelevisionDataGenerator original."""
        generator = TelevisionDataGenerator(seed=42)
        data = generator.generate_tv_data(num_records=self.sample_size)
        
        # Verificar que es un DataFrame
        self.assertIsInstance(data, pd.DataFrame)
        
        # Verificar que tiene el número correcto de registros
        self.assertEqual(len(data), self.sample_size)
        
        # Verificar que tiene todas las columnas esperadas
        for col in COLUMN_NAMES:
            self.assertIn(col, data.columns)
    
    def test_save_data(self):
        """Prueba la funcionalidad de guardar datos."""
        generator = TelevisionDataGenerator()
        data = generator.generate_tv_data(num_records=self.sample_size)
        
        # Crear directorios temporales para las pruebas
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_file = os.path.join(temp_dir, "test_data")
            
            # Probar formato CSV
            csv_path = generator.save_data(data, format="csv", filename=temp_file)
            self.assertTrue(os.path.exists(csv_path))
            
            # Probar formato JSON
            json_path = generator.save_data(data, format="json", filename=temp_file)
            self.assertTrue(os.path.exists(json_path))
            
            # Verificar que se lanza error con formato no soportado
            with self.assertRaises(ValueError):
                generator.save_data(data, format="invalid", filename=temp_file)
    
    def test_data_correlations(self):
        """Prueba que existan correlaciones realistas en los datos."""
        df = generate_television_data(200)
        
        # Verificar correlación entre tamaño y precio
        size_price_corr = df["SCREEN_SIZE_INCHES"].corr(df["PRICE_USD"])
        self.assertGreater(size_price_corr, 0.3, "Debería haber correlación positiva entre tamaño y precio")
        
        # Verificar correlación entre calidad y precio
        quality_price_corr = df["QUALITY_RATING"].corr(df["PRICE_USD"])
        self.assertGreater(quality_price_corr, 0.3, "Debería haber correlación positiva entre calidad y precio")
        
        # Los televisores OLED deberían ser más caros en promedio
        oled_df = df[df["DISPLAY_TECHNOLOGY"] == "OLED"]
        non_oled_df = df[df["DISPLAY_TECHNOLOGY"] != "OLED"]
        
        if len(oled_df) > 0 and len(non_oled_df) > 0:
            mean_oled_price = oled_df["PRICE_USD"].mean()
            mean_non_oled_price = non_oled_df["PRICE_USD"].mean()
            self.assertGreater(mean_oled_price, mean_non_oled_price, 
                              "Los televisores OLED deberían ser más caros en promedio")
    
    def test_field_format_validation(self):
        """Prueba la validación del formato de los campos."""
        df = generate_television_data(50)
        
        # Verificar formato de SKU (ej: AB123456)
        sku_pattern = r'^[A-Z]{2}\d{6}$'
        self.assertTrue(all(df["PRODUCT_SKU"].str.match(sku_pattern)))
        
        # Verificar formato de dimensiones
        dim_pattern = r'^\d+W x \d+H x \d+\.?\d*D$'
        self.assertTrue(all(df["DIMENSIONS_CM"].str.match(dim_pattern)))
        
        # Verificar formato de fecha
        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
        self.assertTrue(all(df["RELEASE_DATE"].str.match(date_pattern)))
        
        # Verificar que todas las fechas son válidas
        for date_str in df["RELEASE_DATE"]:
            try:
                datetime.strptime(date_str, '%Y-%m-%d')
                valid_date = True
            except ValueError:
                valid_date = False
            self.assertTrue(valid_date, f"Fecha inválida: {date_str}")


if __name__ == "__main__":
    unittest.main()
