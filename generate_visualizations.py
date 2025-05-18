"""
Script para generar visualizaciones a partir de los datos de televisiones.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np

# Crear directorio para gráficos si no existe
def create_visualizations_dir():
    vis_dir = "visualizations"
    if not os.path.exists(vis_dir):
        os.makedirs(vis_dir)
    return vis_dir

# Cargar datos
def load_data(file_path="television_data.csv"):
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        print(f"Error al cargar datos: {e}")
        return None

# Gráfica 1: Distribución de precios por marca
def plot_price_by_brand(data, output_path):
    plt.figure(figsize=(14, 8))
    sns.boxplot(x="BRAND", y="PRICE_USD", data=data, palette="viridis")
    plt.title("Distribución de Precios por Marca", fontsize=16)
    plt.xlabel("Marca", fontsize=14)
    plt.ylabel("Precio (USD)", fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfica 2: Distribución de tamaños de pantalla
def plot_screen_size_distribution(data, output_path):
    plt.figure(figsize=(12, 6))
    screen_size_counts = data["SCREEN_SIZE_INCHES"].value_counts().sort_index()
    ax = screen_size_counts.plot(kind="bar", color="skyblue")
    
    # Añadir etiquetas de datos
    for i, v in enumerate(screen_size_counts):
        ax.text(i, v + 1, str(v), ha='center', fontsize=9)
        
    plt.title("Distribución de Tamaños de Pantalla", fontsize=16)
    plt.xlabel("Tamaño de Pantalla (pulgadas)", fontsize=14)
    plt.ylabel("Número de Televisores", fontsize=14)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfica 3: Relación entre precio y calificación
def plot_price_vs_rating(data, output_path):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(
        x="PRICE_USD", 
        y="QUALITY_RATING", 
        hue="DISPLAY_TECHNOLOGY", 
        size="SCREEN_SIZE_INCHES",
        sizes=(20, 200),
        alpha=0.7,
        data=data
    )
    plt.title("Relación entre Precio y Calificación de Calidad", fontsize=16)
    plt.xlabel("Precio (USD)", fontsize=14)
    plt.ylabel("Calificación de Calidad", fontsize=14)
    plt.grid(linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfica 4: Tecnologías de pantalla por segmento de precio
def plot_display_tech_by_price_segment(data, output_path):
    # Crear segmentos de precio
    price_bins = [0, 500, 1000, 2000, 5000, 20000]
    price_labels = ['Económico', 'Básico', 'Medio', 'Premium', 'Gama Alta']
    data['PRICE_SEGMENT'] = pd.cut(data['PRICE_USD'], bins=price_bins, labels=price_labels)
    
    # Crear tabla cruzada
    tech_segment = pd.crosstab(data['DISPLAY_TECHNOLOGY'], data['PRICE_SEGMENT'])
    
    # Graficar
    plt.figure(figsize=(12, 8))
    tech_segment.plot(kind='bar', stacked=True, colormap='viridis')
    plt.title("Tecnologías de Pantalla por Segmento de Precio", fontsize=16)
    plt.xlabel("Tecnología de Pantalla", fontsize=14)
    plt.ylabel("Número de Televisores", fontsize=14)
    plt.legend(title="Segmento de Precio")
    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfica 5: Mapa de calor de correlación entre variables numéricas
def plot_correlation_heatmap(data, output_path):
    # Seleccionar variables numéricas
    numeric_cols = ['PRICE_USD', 'QUALITY_RATING', 'SCREEN_SIZE_INCHES', 
                    'REFRESH_RATE_HZ', 'HDMI_PORTS', 'USB_PORTS', 
                    'AUDIO_OUTPUT_WATTS', 'CUSTOMER_RATING', 'WEIGHT_KG',
                    'POWER_CONSUMPTION_WATTS', 'INPUT_LAG_MS']
    
    numeric_data = data[numeric_cols]
    
    # Calcular matriz de correlación
    corr_matrix = numeric_data.corr()
    
    # Graficar
    plt.figure(figsize=(12, 10))
    mask = np.triu(np.ones_like(corr_matrix, dtype=bool))
    cmap = sns.diverging_palette(230, 20, as_cmap=True)
    
    sns.heatmap(corr_matrix, mask=mask, cmap=cmap, vmax=1, vmin=-1, center=0,
                square=True, linewidths=.5, cbar_kws={"shrink": .5}, annot=True, fmt=".2f")
    
    plt.title("Mapa de Calor de Correlación entre Variables", fontsize=16)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

def main():
    # Crear directorio
    vis_dir = create_visualizations_dir()
    
    # Cargar datos
    data = load_data()
    if data is None:
        return
    
    # Imprimir información general
    print(f"Total de registros: {len(data)}")
    print(f"Columnas disponibles: {data.columns.tolist()}")
    
    # Generar gráficas
    plot_price_by_brand(data, os.path.join(vis_dir, "price_by_brand.png"))
    plot_screen_size_distribution(data, os.path.join(vis_dir, "screen_size_distribution.png"))
    plot_price_vs_rating(data, os.path.join(vis_dir, "price_vs_rating.png"))
    plot_display_tech_by_price_segment(data, os.path.join(vis_dir, "tech_by_price_segment.png"))
    plot_correlation_heatmap(data, os.path.join(vis_dir, "correlation_heatmap.png"))
    
    print("\nSe han generado todas las gráficas en el directorio 'visualizations'")

if __name__ == "__main__":
    main()
