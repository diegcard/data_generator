"""
Script para generar visualizaciones adicionales a partir de los datos de televisiones.
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
        print(f"Error al cargar datos CSV: {e}")
        try:
            return pd.read_json(file_path)
        except Exception as e:
            print(f"Error al cargar datos JSON: {e}")
            return None

# Gráfico 1: Distribución tipo pastel (pie) de tecnologías de pantalla
def plot_display_tech_pie(data, output_path):
    plt.figure(figsize=(10, 8))
    tech_counts = data["DISPLAY_TECHNOLOGY"].value_counts()
    
    # Resaltar las tecnologías más populares
    explode = [0.1 if i == tech_counts.index[0] else 0.05 if i == tech_counts.index[1] else 0 for i in tech_counts.index]
    
    # Colores
    colors = plt.cm.viridis(np.linspace(0, 1, len(tech_counts)))
    
    # Crear gráfico de pastel
    plt.pie(tech_counts, labels=tech_counts.index, autopct='%1.1f%%', 
            startangle=90, explode=explode, colors=colors, shadow=True)
    
    plt.title("Distribución de Tecnologías de Pantalla", fontsize=16)
    plt.axis('equal')  # Aspecto igual para asegurar que sea circular
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfico 2: Distribución de marcas 
def plot_brand_distribution(data, output_path):
    plt.figure(figsize=(12, 8))
    brand_counts = data["BRAND"].value_counts()
    
    # Crear gráfico de barras horizontales
    ax = brand_counts.plot(kind='barh', color=plt.cm.plasma(np.linspace(0, 0.8, len(brand_counts))))
    
    # Agregar etiquetas con porcentajes
    total = brand_counts.sum()
    for i, count in enumerate(brand_counts):
        percentage = count / total * 100
        ax.text(count + 1, i, f"{percentage:.1f}%", va='center')
    
    plt.title("Distribución de Marcas de Televisores", fontsize=16)
    plt.xlabel("Número de Televisores", fontsize=14)
    plt.ylabel("Marca", fontsize=14)
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfico 3: Distribución de resoluciones
def plot_resolution_pie(data, output_path):
    plt.figure(figsize=(10, 8))
    resolution_counts = data["RESOLUTION"].value_counts()
    
    # Crear gráfico de pastel con formato de rosquilla (donut)
    _, ax = plt.subplots(figsize=(10, 8))
    
    # Crear el gráfico de pastel
    wedges, texts, autotexts = ax.pie(
        resolution_counts, 
        labels=resolution_counts.index, 
        autopct='%1.1f%%',
        textprops={'fontsize': 12, 'weight': 'bold'},
        colors=plt.cm.cool(np.linspace(0, 0.8, len(resolution_counts))),
        explode=[0.05] * len(resolution_counts),
        shadow=True,
        wedgeprops={'edgecolor': 'w', 'linewidth': 2}
    )
    
    # Convertir a donut (pastel con hueco)
    centre_circle = plt.Circle((0, 0), 0.5, fc='white')
    ax.add_patch(centre_circle)
    
    # Personalizar textos
    for autotext in autotexts:
        autotext.set_color('white')
    
    plt.title("Distribución de Resoluciones de Pantalla", fontsize=18)
    plt.axis('equal')
    plt.tight_layout()
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfico 4: Distribución de asistentes de voz
def plot_voice_assistant_distribution(data, output_path):
    plt.figure(figsize=(12, 6))
    voice_counts = data["VOICE_ASSISTANT"].value_counts()
    
    # Crear un gráfico de barras apiladas
    ax = voice_counts.plot(
        kind='bar', 
        color=plt.cm.Accent(np.linspace(0, 1, len(voice_counts))),
        edgecolor='black',
        linewidth=1.5
    )
    
    # Agregar etiquetas y valores
    for i, v in enumerate(voice_counts):
        ax.text(i, v/2, f"{v}", ha='center', fontsize=10, fontweight='bold', color='white')
    
    plt.title("Distribución de Asistentes de Voz", fontsize=16)
    plt.xlabel("Asistente de Voz", fontsize=14)
    plt.ylabel("Número de Televisores", fontsize=14)
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

# Gráfico 5: Distribución de TVs por año de fabricación (tendencia temporal)
def plot_manufacture_year_trend(data, output_path):
    plt.figure(figsize=(12, 6))
    
    # Agrupar por año de fabricación
    year_counts = data["MANUFACTURE_YEAR"].value_counts().sort_index()
    
    # Crear gráfico de línea con marcadores
    ax = year_counts.plot(
        kind='line', 
        marker='o', 
        linewidth=3, 
        markersize=10,
        color='#1f77b4',
        markerfacecolor='red',
        markeredgecolor='black'
    )
    
    # Añadir etiquetas de datos
    for i, v in enumerate(year_counts):
        ax.text(year_counts.index[i], v + max(year_counts)*0.02, f"{v}", 
                ha='center', fontsize=9, fontweight='bold')
    
    plt.title("Tendencia de Fabricación por Año", fontsize=16)
    plt.xlabel("Año de Fabricación", fontsize=14)
    plt.ylabel("Número de Televisores", fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig(output_path, dpi=300)
    plt.close()
    print(f"Gráfica guardada en {output_path}")

def main():
    # Crear directorio
    vis_dir = create_visualizations_dir()
    
    # Cargar datos (primero intenta CSV, luego JSON)
    data = load_data("television_data.csv")
    if data is None:
        data = load_data("television_data.json")
        if data is None:
            print("No se pudo cargar los datos. Verifique que existe el archivo television_data.csv o television_data.json")
            return
    
    # Imprimir información general
    print(f"Total de registros cargados: {len(data)}")
    
    # Generar gráficas
    plot_display_tech_pie(data, os.path.join(vis_dir, "display_tech_pie.png"))
    plot_brand_distribution(data, os.path.join(vis_dir, "brand_distribution.png"))
    plot_resolution_pie(data, os.path.join(vis_dir, "resolution_pie.png"))
    plot_voice_assistant_distribution(data, os.path.join(vis_dir, "voice_assistant_distribution.png"))
    plot_manufacture_year_trend(data, os.path.join(vis_dir, "manufacture_year_trend.png"))
    
    print("\nSe han generado todas las gráficas adicionales en el directorio 'visualizations'")

if __name__ == "__main__":
    main()
