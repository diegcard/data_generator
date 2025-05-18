"""
Funciones auxiliares para el generador de datos.
"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os


def create_output_dir(dir_name="output"):
    """
    Crea un directorio para guardar los resultados si no existe.
    
    Args:
        dir_name (str): Nombre del directorio a crear.
        
    Returns:
        str: Ruta del directorio creado.
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    return dir_name


def plot_price_distribution(data, output_file=None):
    """
    Genera un gráfico de distribución de precios por marca.
    
    Args:
        data (pandas.DataFrame): DataFrame con los datos.
        output_file (str, optional): Ruta para guardar el gráfico. Si es None, solo muestra el gráfico.
    """
    plt.figure(figsize=(12, 8))
    sns.boxplot(x="brand", y="price", data=data)
    plt.title("Distribución de Precios por Marca")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    if output_file:
        plt.savefig(output_file)
        plt.close()
    else:
        plt.show()


def plot_quality_by_segment(data, output_file=None):
    """
    Genera un gráfico de calidad por segmento.
    
    Args:
        data (pandas.DataFrame): DataFrame con los datos.
        output_file (str, optional): Ruta para guardar el gráfico. Si es None, solo muestra el gráfico.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x="segment", y="quality_rating", data=data)
    plt.title("Calidad Promedio por Segmento")
    plt.tight_layout()
    
    if output_file:
        plt.savefig(output_file)
        plt.close()
    else:
        plt.show()


def generate_summary_stats(data):
    """
    Genera estadísticas resumidas del conjunto de datos.
    
    Args:
        data (pandas.DataFrame): DataFrame con los datos.
        
    Returns:
        dict: Diccionario con estadísticas resumidas.
    """
    summary = {
        "total_records": len(data),
        "brands_count": data["brand"].nunique(),
        "avg_price": data["price"].mean(),
        "median_price": data["price"].median(),
        "min_price": data["price"].min(),
        "max_price": data["price"].max(),
        "avg_quality": data["quality_rating"].mean(),
        "size_distribution": data["screen_size"].value_counts().to_dict(),
        "resolution_distribution": data["resolution"].value_counts().to_dict(),
        "segment_distribution": data["segment"].value_counts().to_dict()
    }
    
    return summary


def export_summary(summary, output_file="summary.txt"):
    """
    Exporta el resumen a un archivo de texto.
    
    Args:
        summary (dict): Diccionario con estadísticas resumidas.
        output_file (str): Ruta del archivo de salida.
    """
    with open(output_file, "w") as f:
        f.write("RESUMEN DE DATOS GENERADOS DE TELEVISIONES\n")
        f.write("=========================================\n\n")
        
        f.write(f"Total de registros: {summary['total_records']}\n")
        f.write(f"Número de marcas: {summary['brands_count']}\n")
        f.write(f"Precio promedio: ${summary['avg_price']:.2f}\n")
        f.write(f"Precio mediano: ${summary['median_price']:.2f}\n")
        f.write(f"Precio mínimo: ${summary['min_price']:.2f}\n")
        f.write(f"Precio máximo: ${summary['max_price']:.2f}\n")
        f.write(f"Calificación de calidad promedio: {summary['avg_quality']:.2f}/5\n\n")
        
        f.write("Distribución por tamaño de pantalla:\n")
        for size, count in summary["size_distribution"].items():
            f.write(f"  {size}\": {count} ({count/summary['total_records']*100:.1f}%)\n")
        
        f.write("\nDistribución por resolución:\n")
        for res, count in summary["resolution_distribution"].items():
            f.write(f"  {res}: {count} ({count/summary['total_records']*100:.1f}%)\n")
        
        f.write("\nDistribución por segmento:\n")
        for seg, count in summary["segment_distribution"].items():
            f.write(f"  {seg}: {count} ({count/summary['total_records']*100:.1f}%)\n")
